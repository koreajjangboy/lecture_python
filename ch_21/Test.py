from db_module import (
    add_expense_db,
    calculate_by_category_db,
    calculate_total_db,
    get_expenses_db,
)


def add_expense_cli():
  date = input("날짜(YYYY-MM-DD): ").strip()
  category = input("카테고리: ").strip()
  description = input("내용: ").strip()

  if not date or not category or not description:
    print("날짜, 카테고리, 내용은 비워 둘 수 없습니다.")
    return

  try:
    amount = int(input("금액: "))
  except ValueError:
    print("금액은 정수로 입력해 주세요.")
    return

  if amount <= 0:
    print("금액은 0보다 큰 값으로 입력해 주세요.")
    return

  if add_expense_db(date, category, description, amount):
    print("지출 내역을 DB에 추가했습니다.")


def show_expenses_cli():
  expenses = get_expenses_db()
  if not expenses:
    print("등록된 지출이 없습니다.")
    return

  print("\n=============== 지출 내역 ===============")
  number = 1
  columns = expenses[0].keys()
  print(f"{' | '.join(columns)}")
  print("-" * 40)

  for expense in expenses:
    print(
        f"{number}. {expense['date']} | "
        f"{expense['category']} | "
        f"{expense['description']} | "
        f"{expense['amount']:,}원"
    )
    number += 1


# 메인 실행 루프
if __name__ == "__main__":
  while True:
    print("\n=== 개인 지출 관리 (콘솔 버전) ===")
    print("1. 지출 추가")
    print("2. 지출 목록")
    print("3. 지출 요약")
    print("0. 종료")

    choice = input("메뉴 선택: ").strip()

    if choice == "1":
      add_expense_cli()
    elif choice == "2":
      show_expenses_cli()
    elif choice == "3":
      print(f"전체 지출: {calculate_total_db():,}원")

      es = calculate_by_category_db()
      # SQL에서 이미 정렬되어 넘어오므로 sorted() 생략 가능
      for category, total in es.items():
        print(f"{category}: {total:,}원")
    elif choice == "0":
      print("프로그램을 종료합니다.")
      break
    else:
      print("메뉴 번호를 다시 선택해 주세요.")