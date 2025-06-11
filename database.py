import sqlite3


def create_connection():
    conn = sqlite3.connect("clinic.db")
    return conn


def initiazlize_database():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            diagnosis TEXT
        )
    ''')

    conn.commit()
    conn.close()