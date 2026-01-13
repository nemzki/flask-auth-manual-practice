import sqlite3

DB_NAME = "auth.db"

def get_db():
    # return a connection to the database with row access by name
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row

    return conn

# Create users if not exists
def init_db():

    with get_db() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
        )
        """)