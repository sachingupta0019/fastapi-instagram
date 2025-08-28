
# 📸 FastAPI Instagram Clone API

A backend API built with **FastAPI** that mimics Instagram’s core features such as authentication, posting images, liking, and commenting.

---

## 🚀 Features

* User authentication & authorization (JWT-based)
* Create, update, and delete posts
* Add Post title, description, caption, Images
* Like & comment on posts
* SQLite database (default, via `instagram_api.db`)
* Organized project structure (auth, database, routes, schema)
* Automatic API docs with **Swagger** & **ReDoc**

---

## 📂 Project Structure

```bash
Instagram_Clone/
│── Instagram/
│   ├── auth/             # Authentication logic
│   ├── database/         # Database connection/config
│   ├── images/           # Uploaded images
│   ├── routes/           # API routes (users, posts, comments, etc.)
│   ├── schema/           # Pydantic schemas
│   ├── instagram_api.db  # SQLite database
│   ├── main.py           # Application entry point
│   └── requirements.txt  # Dependencies for this app
│
├── instagram_env/        # Virtual environment (ignored in git)
├── react_app/            # Frontend (React project)
├── .gitignore
└── requirements.txt      # Root dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/fastapi-instagram-clone.git
cd FastAPI/Instagram_Clone
```

### 2️⃣ Create & activate virtual environment

```bash
# Create virtual environment
python -m venv instagram_env

# Activate venv (Windows)
instagram_env\Scripts\activate

# Activate venv (Mac/Linux)
source instagram_env/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install -r Instagram/requirements.txt
```

### 4️⃣ Run the application

```bash
uvicorn Instagram.main:app --reload
```

Server will start at 👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📑 API Documentation

* Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🛠️ Environment Variables

Create a `.env` file in the root or configure inside `main.py`:

```ini
DATABASE_URL=sqlite:///./Instagram/instagram_api.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 🎯 Future Enhancements

* Switch to PostgreSQL for production
* Add image storage in AWS S3 / Cloudinary
* Implement notifications & stories
* Dockerize the application

---

✅ Now you can run your **Instagram Clone API** locally with just a few commands.


## Frontend Setup 

*COming Soon.
