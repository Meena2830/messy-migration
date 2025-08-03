# 🧠 messy-migration

A clean, secure, and structured **User Management REST API** built with **FastAPI**. This project demonstrates how to create and manage users, perform login validation, and maintain clean architecture using modern Python best practices.

---

## 🚀 Features

- Create, update, and delete users
- Password hashing with `bcrypt`
- Input validation using `Pydantic`
- Login endpoint to verify user credentials
- SQLite with SQLAlchemy ORM
- Modular folder structure
- FastAPI interactive docs at `/docs`

---

## 📁 Folder Structure
messy-migration/app/
├── auth.py
├── db.py
├── main.py
├── models.py
├── routes.py
├── schemas.py
├── utils.py
├── __init__.py
└── __pycache__/
    ├── db.cpython-312.pyc
    ├── main.cpython-312.pyc
    ├── models.cpython-312.pyc
    ├── routes.cpython-312.pyc
    ├── schemas.cpython-312.pyc
    ├── utils.cpython-312.pyc
    └── __init__.cpython-312.pyc


---

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/messy-migration.git
cd messy-migration


2. Set up a virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


3. Install dependencies

pip install -r requirements.txt


4. Initialize the database

python init_db.py


Run the app locally bash


uvicorn app.main:app --reload



pip install pytest httpx
pytest test_user.py



Run tests:

pip install pytest httpx
pytest test_user.py


