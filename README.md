# 🤖 HireSense-AI — Intelligent Resume Analyzer & Job Match System 📊

An AI-powered recruitment assistant that analyzes resumes, detects skills, evaluates job readiness, and recommends missing technologies 🎯

---

## 🌟 Overview

**HireSense-AI** is a smart Applicant Tracking & Evaluation System designed to help students understand whether they are ready for a specific job role.

Instead of manually guessing your preparation level, the system automatically:

* reads uploaded resume PDFs 📄
* extracts text using NLP 🧠
* identifies technical skills ⚙️
* compares with target job role 🎯
* calculates match score 📊
* recommends missing skills 📚

It simulates how real companies filter candidates using automated resume screening systems (ATS).

---

## 🎯 Problem Statement

Many students apply for internships and placements without knowing:

* Is my resume ATS-friendly?
* Do my skills match the role?
* Why am I not getting shortlisted?
* What should I learn next?

**HireSense-AI answers all of these automatically.**

---

## 🚀 Features (Planned & In Progress)

### Core Features

* 📄 Resume PDF Upload
* 🔍 Resume text extraction
* 🧠 AI-based skill detection
* 🎯 Job role input (e.g., Backend Developer / Data Analyst)
* 📊 Resume-job match score
* 📚 Missing skills suggestions

### Advanced Features (Coming Soon)

* ATS resume feedback
* AI career roadmap
* Interview question generator
* GitHub profile analysis
* Placement readiness prediction

---

## 🧠 System Workflow

1. User uploads resume
2. Backend extracts text from PDF
3. AI detects skills (Python, React, SQL, etc.)
4. User selects a job role
5. Matching engine compares skills vs role
6. System generates score and recommendations

---

## 🏗️ Tech Stack

### Backend

* Python 3
* FastAPI
* NLP (Skill Extraction)
* PyMuPDF (PDF Parsing)

### Frontend

* React / Next.js
* Tailwind CSS

### Tools & Concepts

* REST APIs
* Swagger UI API Testing
* Git & GitHub
* Modular Backend Architecture

---

## 📂 Project Structure

```
hiresense-ai/
│
├── backend/
│   ├── main.py              # FastAPI server
│   ├── resume_parser.py     # Extract resume text
│   ├── skills.py            # Skill detection logic
│   ├── matcher.py           # Job matching engine
│   └── uploads/             # Uploaded resumes
│
├── frontend/
│   ├── components/
│   ├── pages/
│   └── UI dashboard
│
├── requirements.txt
└── README.md
```

---

## 🖼️ Screenshots

🚧 UI and result screenshots will be added after frontend completion.

---

## 🎥 Demo

🚧 Demo video will be uploaded after core features are implemented.

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```
git clone https://github.com/Shristirajpoot/hiresense-ai.git
cd hiresense-ai
```

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

### 3️⃣ Activate Environment

**Windows**

```
venv\Scripts\activate
```

**Linux / Mac**

```
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```
pip install -r requirements.txt
```

### 5️⃣ Run Backend Server

```
cd backend
uvicorn main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

---

## 🛠️ Built With

* 🐍 Python
* ⚡ FastAPI
* 📄 PDF Parsing
* 🧠 NLP Techniques
* 🎨 React (Frontend UI)

---

## 📌 Future Enhancements

* Resume formatting checker
* Multi-resume comparison
* LinkedIn analysis
* Company-wise readiness score
* AI interview preparation assistant

---

## 👩‍💻 Author
### Shristi Rajpoot
- 📧 Email: shristirajpoot369@gmail.com
- 🔗 GitHub: @Shristirajpoot

## 📄 License
This project is licensed under the MIT License.

### 🌟 If you liked this project, consider starring the repo and sharing it!

