import csv
import os
import pandas as pd
import streamlit as st

# 1. 페이지 설정 (가장 처음에 위치)
st.set_page_config(
    page_title="개인 지출 관리 웹 서비스", page_icon="💰", layout="wide"
)

# 2. 우측 상단 Deploy 버튼, 헤더, 푸터 및 기본 메뉴 숨기기 + 탭 스타일 반응형 CSS 주입
hide_streamlit_style = """
    <style>
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    .stDeployButton {display:none;}
    
    /* 탭(Tab) 스타일 커스텀: 글자 크기 확대 및 흰색 텍스트 적용 */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: transparent;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: transparent;
        border-radius: 4px;
        color: #FFFFFF !important;
        font-size: 25px !important;
        font-weight: 500;
        padding: 0px 20px;
    }
    .stTabs [aria-selected="true"] {
        background-color: rgba(255, 255, 255, 0.1) !important;
        border-bottom: 2px solid #FFFFFF !important;
    }
    
    /* 모바일 환경 대응 */
    @media (max-width: 768px) {
        .stTabs [data-baseweb="tab"] {
            font-size: 20px !important;
            padding: 0px 10px;
        }
    }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

FILE_PATH = "sample_expenses.csv"


# 파일 로드 함수
def load_expenses(file_path):
  expenses = []
  if not os.path.exists(file_path):
    return expenses
  try:
    with open(file_path, "r", encoding="utf-8-sig", newline="") as file:
      reader = csv.DictReader(file)
      for row in reader:
        try:
          row["amount"] = int(row["amount"])
        except ValueError:
          continue
        expenses.append(row)
  except Exception:
    return []
  return expenses


# 파일 저장 함수
def save_expenses(file_path, expenses):
  fieldnames = ["date", "category", "description", "amount"]
  with open(file_path, "w", encoding="utf-8-sig", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(expenses)


# 앱 타이틀
st.title("개인 지출 관리 웹 서비스")

# 데이터 로드 (세션 상태 유지)
if "expenses" not in st.session_state:
  st.session_state.expenses = load_expenses(FILE_PATH)

# 상단 탭 메뉴 구성 (모바일에서도 화면 상단에 고정되어 항상 보입니다)
tab1, tab2, tab3 = st.tabs(["지출 목록 보기", "지출 추가하기", "지출 요약"])

# 1. 지출 목록 보기 탭
with tab1:
  st.subheader("등록된 지출 내역")

  if not st.session_state.expenses:
    st.info("등록된 지출 내역이 없습니다.")
  else:
    df = pd.DataFrame(st.session_state.expenses)
    df["amount"] = df["amount"].apply(lambda x: f"{x:,}원")
    st.dataframe(df, use_container_width=True)

    if st.button("변경사항 파일로 저장"):
      save_expenses(FILE_PATH, st.session_state.expenses)
      st.success("파일에 성공적으로 저장되었습니다!")

# 2. 지출 추가하기 탭
with tab2:
  st.subheader("새로운 지출 내역 추가")

  with st.form("expense_form"):
    date = st.date_input("날짜")
    category = st.text_input("카테고리 (예: 식비, 교통비, 주거)")
    description = st.text_input("내용 (예: 점심값, 지하철)")
    amount = st.number_input("금액 (원)", min_value=0, step=1000)

    submitted = st.form_submit_button("지출 추가")

    if submitted:
      if not category.strip() or not description.strip():
        st.error("카테고리와 내용은 비워 둘 수 없습니다.")
      elif amount <= 0:
        st.error("금액은 0보다 큰 값이어야 합니다.")
      else:
        new_item = {
            "date": str(date),
            "category": category.strip(),
            "description": description.strip(),
            "amount": int(amount),
        }
        st.session_state.expenses.append(new_item)
        save_expenses(FILE_PATH, st.session_state.expenses)
        st.success("지출 내역이 추가되고 저장되었습니다!")

# 3. 지출 요약 탭
with tab3:
  st.subheader("지출 요약 및 통계")

  if not st.session_state.expenses:
    st.info("요약할 지출 내역이 없습니다.")
  else:
    df = pd.DataFrame(st.session_state.expenses)

    total_spent = df["amount"].sum()
    st.metric(label="총 지출 금액", value=f"{total_spent:,}원")

    st.markdown("---")
    st.markdown("### 카테고리별 지출 현황")

    category_df = df.groupby("category")["amount"].sum().reset_index()
    category_df["amount_formatted"] = category_df["amount"].apply(
        lambda x: f"{x:,}원"
    )

    st.table(category_df[["category", "amount_formatted"]])