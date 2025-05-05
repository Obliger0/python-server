import sqlite3

DB_NAME = 'todos.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_all_todos():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todos')
    todos = cursor.fetchall()
    conn.close()
    return todos

def add_todo(content):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (content) VALUES (?)', (content,))
    conn.commit()
    conn.close()

def delete_todo_by_id(todo_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()
