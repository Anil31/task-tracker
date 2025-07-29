import sqlite3
from task import Task

def get_connection():
    return sqlite3.connect("tasks.db")

def setup_database():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                completed INTEGER DEFAULT 0
            )
        """)
        conn.commit()

def add_task(title, description):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (title, description))
        conn.commit()

def get_all_tasks():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, title, description, completed FROM tasks")
        rows = cursor.fetchall()
        return [Task(*row) for row in rows]

def mark_task_completed(task_id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        conn.commit()
