import mysql.connector
from datetime import datetime

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="@Krishna9",
        database="marketing_agent"
    )

# ✅ SAVE PLAN
def save_plan(goal, plan):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO plans (goal, plan, created_at)
    VALUES (%s, %s, %s)
    """

    cursor.execute(query, (goal, plan, datetime.now()))

    conn.commit()   # ✅ CRITICAL
    cursor.close()
    conn.close()

# ✅ LOAD PLANS
def load_plans():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT id, goal, plan, created_at
        FROM plans
        ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows

# ✅ DELETE PLAN (BY ID)
def delete_plan(plan_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = "DELETE FROM plans WHERE id = %s"
    cursor.execute(query, (plan_id,))

    conn.commit()
    cursor.close()
    conn.close()

# ✅ CLEAR HISTORY
def clear_history():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM plans")

    conn.commit()
    cursor.close()
    conn.close()