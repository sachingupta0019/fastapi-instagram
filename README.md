Here’s an updated README that includes your React frontend along with your FastAPI backend. I’ve integrated it so users can run both parts together seamlessly.

---

# 📸 FastAPI Instagram Clone

A full-stack Instagram clone project with **FastAPI** as backend and **React** as frontend. Mimics Instagram’s core features such as authentication, posting images, liking, and commenting.

---

## 🚀 Features

### Backend (FastAPI)

* User authentication & authorization (JWT-based)
* Create, update, and delete posts
* Add post title, description, caption, images
* Like & comment on posts
* SQLite database (default, via `instagram_api.db`)
* Organized project structure (auth, database, routes, schema)
* Automatic API docs with **Swagger** & **ReDoc**

### Frontend (React)

* Responsive Instagram-like UI
* User login/signup
* Display posts with images, captions, likes, and comments
* Add, like, and comment on posts
* Works seamlessly with FastAPI backend

---

## 📂 Project Structure

```bash
Instagram_Clone/
│── Instagram/             # FastAPI backend
│   ├── auth/
│   ├── database/
│   ├── images/
│   ├── routes/
│   ├── schema/
│   ├── instagram_api.db
│   ├── main.py
│   └── requirements.txt
│
├── react_app/             # React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── README.md
│
├── instagram_env/         # Virtual environment (ignored in git)
├── .gitignore
└── requirements.txt       # Root dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/fastapi-instagram-clone.git
cd fastapi-instagram-clone
```

---

### 2️⃣ Backend Setup (FastAPI)

```bash
# Create virtual environment
python -m venv instagram_env

# Activate virtual environment
# Windows
instagram_env\Scripts\activate
# Mac/Linux
source instagram_env/bin/activate

# Install dependencies
pip install -r Instagram/requirements.txt

# Run backend
uvicorn Instagram.main:app --reload
```

Backend will start at 👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

API Docs:

* Swagger → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### 3️⃣ Frontend Setup (React)

```bash
# Navigate to frontend
cd react_app

# Install dependencies
npm install

# Start React app
npm start
```

React frontend will start at 👉 [http://localhost:3000](http://localhost:3000) and interact with FastAPI backend.

> ⚠️ Make sure the backend is running before using the frontend.

---

## 🛠️ Environment Variables

Create a `.env` file in the root or inside backend (`Instagram/`):

```ini
DATABASE_URL=sqlite:///./Instagram/instagram_api.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

For frontend, you can create a `.env` file in `react_app/` if you need API URLs:

```ini
REACT_APP_API_URL=http://127.0.0.1:8000
```

---

## 🎯 Future Enhancements

* Switch backend to PostgreSQL for production
* Store images in AWS S3 / Cloudinary
* Implement notifications & stories
* Dockerize backend & frontend for easy deployment
* Deploy frontend on GitHub Pages / Vercel
* Deploy backend on AWS EC2 / Railway / Render

---

✅ Now you can run your **Instagram Clone** locally with **FastAPI backend** and **React frontend** seamlessly.

