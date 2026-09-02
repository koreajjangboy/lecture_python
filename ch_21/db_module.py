import psycopg2
from psycopg2.extras import RealDictCursor

# PostgreSQL 데이터베이스 연결 정보 설정
DB_CONFIG = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "MyPostgres123!",
    "host": "localhost",
    "port": "5432",
}


def get_db_connection():
  """데이터베이스 연결 및 expenses 스키마 설정 헬퍼 함수"""
  conn = psycopg2.connect(**DB_CONFIG)
  with conn.cursor() as cursor:
    cursor.execute("SET search_path TO expenses;")
  return conn


def add_expense_db(date, category, description, amount):
  """새로운 지출 내역을 DB에 추가"""
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    query = """
            INSERT INTO expenses (date, category, description, amount)
            VALUES (%s, %s, %s, %s)
        """
    cursor.execute(query, (date, category, description, amount))
    conn.commit()
    cursor.close()
    conn.close()
    return True
  except Exception as e:
    print(f"데이터 추가 중 오류 발생: {e}")
    return False


def get_expenses_db():
  """DB에서 모든 지출 내역 조회"""
  try:
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute(
        "SELECT id, date, category, description, amount FROM expenses ORDER BY"
        " id ASC"
    )
    expenses = cursor.fetchall()
    cursor.close()
    conn.close()
    return [
        {
            "id": row["id"],
            "date": str(row["date"]),
            "category": row["category"],
            "description": row["description"],
            "amount": int(row["amount"]),
        }
        for row in expenses
    ]
  except Exception as e:
    print(f"데이터 조회 중 오류 발생: {e}")
    return []


def calculate_total_db():
  """전체 지출 총액 계산"""
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(amount) FROM expenses")
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result[0] if result and result[0] is not None else 0
  except Exception as e:
    print(f"총액 계산 중 오류 발생: {e}")
    return 0


def calculate_by_category_db():
  """카테고리별 지출 요약 계산"""
  category_totals = {}
  try:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT category, SUM(amount) as total_amount FROM expenses GROUP BY category ORDER BY total_amount DESC"
    )
    rows = cursor.fetchall()
    for row in rows:
      category_totals[row[0]] = row[1]
    cursor.close()
    conn.close()
  except Exception as e:
    print(f"카테고리별 요약 중 오류 발생: {e}")
  return category_totals