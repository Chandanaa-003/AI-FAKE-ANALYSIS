# Fake AI Analysis

An AI-powered application designed to analyze digital content and identify potentially fake or manipulated media. It helps users examine suspicious content and understand whether it may be authentic or AI-generated.

---

## ✨ Features
- **AI-Powered Fake Content Analysis**: Examine media authenticity and identify manipulated media.
- **FastAPI REST Backend**: High performance, modern API architecture.
- **Modular Architecture**: Clean separation into Routers, Services, Repositories, Models, and Schemas.
- **Interactive Documentation**: Built-in Swagger UI and ReDoc.
- **Secure Configuration**: Environment-based config with `.env` support.

---

## 🛠️ Tech Stack
- **Backend:** Python 3.10+, FastAPI, SQLAlchemy, Pydantic, Uvicorn
- **Security:** python-jose (JWT), Argon2 password hashing
- **Testing:** Pytest

---

## 📁 Project Structure

```text
fast_api_tut/
├── .env.example              # Sample environment configuration
├── .gitignore                # Git ignore rules for Python, venv, IDEs
├── LICENSE                   # MIT License
├── README.md                 # Project documentation
├── requirements.txt          # Python dependencies
└── tut/
    ├── requirements.txt      # Backend dependencies
    ├── app/
    │   ├── main.py           # FastAPI entrypoint
    │   ├── core/             # Database configuration, helpers
    │   │   ├── db.py
    │   │   ├── helper.py
    │   │   └── image_upload.py
    │   ├── models/           # SQLAlchemy ORM models
    │   │   └── expense.py
    │   ├── repositories/     # Data access layer
    │   │   └── user_repo.py
    │   ├── routers/          # API route handlers
    │   ├── schemas/          # Pydantic validation schemas
    │   │   ├── api.py
    │   │   ├── expence.py
    │   │   └── user.py
    │   └── services/         # Business logic layer
    │       ├── auth_service.py
    │       └── expense_service.py
    └── test/                 # Test suite
        ├── auth.py
        └── services/
            └── auth.py
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Chandanaa-003/AI-FAKE-ANALYSIS.git
cd AI-FAKE-ANALYSIS
```

### 2. Create & Activate Virtual Environment

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
```bash
# Windows PowerShell
Copy-Item .env.example .env

# Linux / macOS
cp .env.example .env
```

---

## 🏃 Running the Application

Navigate to the `tut` directory and start the Uvicorn development server:

```bash
cd tut
uvicorn app.main:app --reload
```

The API will be running at: **`http://127.0.0.1:8000`**

---

## 📖 Interactive API Documentation

Once the server is running, explore the interactive documentation:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧪 Running Tests

Run the test suite using pytest:
```bash
pytest tut/test/
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
