 # 🚀 FastAPI-Postgres-CRUD

A simple Web API built with **FastAPI** and **PostgreSQL** for learning backend development.  
It covers:
- Creating a database and connecting it with FastAPI
- Building RESTful endpoints (CRUD operations)
- Using SQLAlchemy ORM for database interaction
- Documenting the API automatically with Swagger UI

---

## 🧠 Project Overview

This project is a hands-on learning project to understand how a backend server interacts with a relational database.  
It’s built step-by-step using:

- **FastAPI** — for building modern web APIs in Python  
- **PostgreSQL** — for managing persistent data  
- **SQLAlchemy** — as an ORM to map Python classes to database tables  
- **Pydantic** — for data validation  

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/FastAPI-Postgres-CRUD.git
cd FastAPI-Postgres-CRUD
```
### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the Application
```bash
uvicorn main:app --reload
```

### Open your browser at:

- http://127.0.0.1:8000/docs — Swagger UI
- http://127.0.0.1:8000/redoc — ReDoc docs

---

## 🧱 Folder Structure

```bash
FastAPI-Postgres-CRUD/
│
├── main.py              # Entry point for FastAPI
├── models.py            # SQLAlchemy models
├── database.py          # Database connection setup
├── schemas.py           # Pydantic models
├── crud.py              # Database operations (CRUD)
├── requirements.txt     # Project dependencies
├── .env                 # Environment variables (not uploaded)
└── README.md            # Project documentation
```

---

## 🧰 Technologies Used

- **Python 3.11+**
- **FastAPI**
- **PostgreSQL**
- **SQLAlchemy**
- **Uvicorn**
- **Pydantic**
- **dotenv**



