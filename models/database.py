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

#  INSERTING USER TO DATABASE
def add_user(email, password_hash):
    try:
        with get_db() as conn:

            conn.execute(
                "INSERT INTO users (email, password) VALUES (?, ?)",
                (email, password_hash)
            )

            return True
    except Exception as e:
        print("Error adding user: ", e)
        return False


#   Return a user row by email or None if nort found
def get_user_by_email(email):
    db = get_db()
    user = db.execute(
        "SELECT * FROM users WHERE email = ?",
        (email,)
    ).fetchone()
    return user