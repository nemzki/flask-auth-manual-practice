from .database import get_db

def create_user(username, email, password):
    try:
        with get_db() as conn:
            conn.execute(
                "INSERT INTO users (username, email, password) VALUES (?, ?, ?)",
                (username, email, password)
            )
            conn.commit()
            return True
    except Exception as e:
        print("Create user error", e)
        return False

def get_user_by_username(username):
    with get_db() as conn:
        return conn.execute(
                "SELECT * FROM users WHERE username = ?",
                (username,)
            ).fetchone()
