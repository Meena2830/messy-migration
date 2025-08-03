# import sqlite3
# from app.schemas import UserCreate, UserUpdate, User

# DB_PATH = "database.db"

# def get_connection():
#     return sqlite3.connect(DB_PATH)

# def get_users():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, name, email FROM users")
#     rows = cursor.fetchall()
#     conn.close()
#     return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]

# def get_user_by_id(user_id: int):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT id, name, email FROM users WHERE id=?", (user_id,))
#     row = cursor.fetchone()
#     conn.close()
#     if row:
#         return {"id": row[0], "name": row[1], "email": row[2]}
#     return None

# def create_user(user: UserCreate):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
#                    (user.name, user.email, user.password))
#     conn.commit()
#     user_id = cursor.lastrowid
#     conn.close()
#     return {"id": user_id, "name": user.name, "email": user.email}

# def update_user(user_id: int, user: UserUpdate):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("UPDATE users SET name=?, email=? WHERE id=?",
#                    (user.name, user.email, user_id))
#     conn.commit()
#     conn.close()
#     return {"id": user_id, "name": user.name, "email": user.email}

# def delete_user(user_id: int):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("DELETE FROM users WHERE id=?", (user_id,))
#     conn.commit()
#     conn.close()


from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
