# 🌍 HopeConnect AI — NGO Volunteer & Donation Management System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=for-the-badge&logo=flask)
![AI/ML](https://img.shields.io/badge/AI-TF--IDF_Matching-FF6B6B?style=for-the-badge&logo=scikitlearn)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub_Actions-2088FF?style=for-the-badge&logo=githubactions)
![JWT](https://img.shields.io/badge/Auth-JWT_Secured-orange?style=for-the-badge)
![Social Good](https://img.shields.io/badge/Purpose-Social_Good-brightgreen?style=for-the-badge)

> An AI-powered platform that connects volunteers to NGO opportunities using machine learning — built to solve real-world challenges faced by non-profit organizations in volunteer recruitment and donation tracking.

---

## 🎯 Project Overview

HopeConnect AI is a **secure, intelligent backend system** designed for non-profit organizations to streamline volunteer management, opportunity posting, and donation tracking. The core feature is an **AI-powered matching engine** that uses TF-IDF vectorization and cosine similarity to intelligently connect volunteers to the most relevant NGO opportunities based on their skills, location, and availability.

This project was built with a social impact mindset — directly addressing the challenge of efficient volunteer-NGO coordination faced by thousands of non-profits globally.

---

## 💡 Problem Statement

Non-profit organizations struggle with:
- **Manual volunteer matching** — time-consuming and often inaccurate
- **Skill-opportunity mismatches** — volunteers assigned to wrong roles
- **Fragmented donation tracking** — no centralized summary per NGO
- **No data-driven insights** — decisions made without analytics

**HopeConnect AI solves all four.**

---

## ⚙️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Backend** | Python, Flask | Core API development |
| **AI/ML** | Scikit-learn, TF-IDF, Cosine Similarity | Intelligent volunteer-opportunity matching |
| **Data Processing** | Pandas, NumPy | Data manipulation and analysis |
| **Database** | SQLite + SQLAlchemy ORM | Relational data modeling |
| **Authentication** | Flask-JWT-Extended | Secure token-based auth |
| **Containerization** | Docker | Environment consistency |
| **CI/CD** | GitHub Actions | Automated build & test pipeline |
| **Testing** | Pytest | Automated unit test execution |
| **Version Control** | Git + GitHub | Source control & collaboration |

---

## 🤖 AI Matching Engine

The heart of HopeConnect is its **ML-powered matching algorithm**:

```
Volunteer Profile                    Opportunity Profile
─────────────────                    ───────────────────
Skills: "teaching, coding"           Required: "coding, teaching"
Location: "Mumbai"          ──►      Location: "Mumbai"
Availability: "weekends"             Schedule: "weekends"
        │                                    │
        ▼                                    ▼
┌───────────────────────────────────────────────┐
│         TF-IDF Vectorization                   │
│  Converts text profiles into numeric vectors   │
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│         Cosine Similarity Scoring              │
│  Measures angle between volunteer & opp vectors│
└───────────────────────┬───────────────────────┘
                        │
                        ▼
┌───────────────────────────────────────────────┐
│         Ranked Match Results                   │
│  Returns opportunities sorted by match score   │
└───────────────────────────────────────────────┘
```

**Sample AI Output:**
```json
{
  "volunteer": {
    "name": "Priya Sharma",
    "skills": "teaching coding",
    "location": "Mumbai"
  },
  "matches": [
    {
      "title": "Code Teacher for Underprivileged Kids",
      "ngo_name": "EduHelp Foundation",
      "match_score": 94.7
    },
    {
      "title": "Digital Literacy Trainer",
      "ngo_name": "BridgeIT NGO",
      "match_score": 78.3
    }
  ]
}
```

---

## 🏗️ System Architecture

```
Client Request
      │
      ▼
┌─────────────────┐
│  JWT Auth Layer  │  ◄── Secure token validation
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Flask Routes    │  ◄── RESTful API endpoints
└────────┬────────┘
         │
    ┌────┴─────┐
    │          │
    ▼          ▼
┌───────┐  ┌──────────────┐
│  ORM  │  │  AI Matcher   │  ◄── TF-IDF + Cosine Similarity
└───┬───┘  └──────────────┘
    │
    ▼
┌─────────────────┐
│   SQLite DB      │  ◄── Volunteers, Opportunities, Donations
└─────────────────┘
```

---

## 📡 API Endpoints

| Method | Endpoint | Auth | Description |
|--------|----------|:----:|-------------|
| `POST` | `/login` | ❌ | Authenticate and receive JWT token |
| `POST` | `/volunteers` | ✅ | Register a new volunteer |
| `GET` | `/volunteers` | ✅ | List all registered volunteers |
| `POST` | `/opportunities` | ✅ | Post a new NGO opportunity |
| `GET` | `/opportunities` | ✅ | List all opportunities |
| `GET` | `/match/<volunteer_id>` | ✅ | **AI match volunteer to opportunities** |
| `POST` | `/donations` | ✅ | Record a donation |
| `GET` | `/donations/summary` | ✅ | Get donation totals by NGO |

---

## 🔐 Security Implementation

- **JWT Authentication** — All sensitive endpoints protected with JSON Web Tokens
- **Token Expiry** — Tokens auto-expire to prevent unauthorized reuse
- **Input Validation** — All request payloads validated before DB operations
- **Structured Error Handling** — 404/500 handlers prevent data leakage
- **Environment Isolation** — Sensitive configs excluded via `.gitignore`

---

## 🚀 CI/CD Pipeline

Every `git push` automatically triggers:

```
Push to GitHub
      │
      ▼
┌──────────────────────┐
│  1. Checkout Code     │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  2. Setup Python 3.10 │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  3. Install Deps      │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  4. Run Pytest        │  ◄── AI matcher unit tests
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│  5. Build Docker Image│
└──────────────────────┘
```

---

## 🐳 Run with Docker

```bash
# Build the image
docker build -t hopeconnect-ai .

# Run the container
docker run -p 5000:5000 hopeconnect-ai
```

---

## 💻 Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/SoumyasreeMitra/hopeconnect-ai.git
cd hopeconnect-ai

# 2. Install dependencies
pip install -r requirements.txt

# 3. Start the server
python app.py

# Server runs at http://localhost:5000
```

---

## 🧪 Sample API Usage

**Step 1 — Login:**
```bash
POST /login
{ "username": "admin" }
# Returns: { "access_token": "eyJ..." }
```

**Step 2 — Register a volunteer:**
```bash
POST /volunteers
Headers: Authorization: Bearer <token>
{
  "name": "Priya Sharma",
  "email": "priya@email.com",
  "skills": "teaching coding python",
  "location": "Mumbai",
  "availability": "weekends"
}
```

**Step 3 — Get AI matches:**
```bash
GET /match/1
Headers: Authorization: Bearer <token>

# Returns ranked opportunities with match scores
{
  "volunteer": { "name": "Priya Sharma", ... },
  "matches": [
    { "title": "Code Teacher", "match_score": 94.7 },
    { "title": "Digital Trainer", "match_score": 78.3 }
  ]
}
```

---

## 📁 Project Structure

```
hopeconnect-ai/
├── app.py                  # Application entry point
├── models.py               # Database models (Volunteer, Opportunity, Donation)
├── routes.py               # API route definitions
├── ai_matcher.py           # ML matching engine (TF-IDF + Cosine Similarity)
├── requirements.txt        # Project dependencies
├── Dockerfile              # Container configuration
├── test_app.py             # AI matcher unit tests
├── .gitignore              # Excludes sensitive/unnecessary files
└── .github/
    └── workflows/
        └── ci.yml          # GitHub Actions CI/CD pipeline
```

---

## 🌱 Software Engineering Practices Demonstrated

| Practice | Implementation |
|---|---|
| **AI/ML Integration** | TF-IDF vectorization + cosine similarity matching |
| **Secure Coding** | JWT auth, input validation, structured error handling |
| **Agile / CI/CD** | Automated GitHub Actions pipeline on every push |
| **Application Resiliency** | Error handlers (404, 500) for stable API behavior |
| **Containerization** | Dockerized for consistent cross-environment deployment |
| **Relational Database** | SQLAlchemy ORM with normalized data models |
| **Social Impact** | Built for real NGO use cases — volunteer & donation management |
| **Unit Testing** | Pytest-based tests for AI matching engine |

---

## 🔮 Future Enhancements

- [ ] Upgrade to BERT embeddings for deeper semantic volunteer matching
- [ ] Add analytics dashboard for NGO performance insights
- [ ] Migrate to PostgreSQL for production-scale data
- [ ] Deploy on AWS with auto-scaling for high volunteer registration periods
- [ ] Add email notification system for match alerts

---

## 🤝 Social Impact

This project was inspired by the real-world challenge of connecting willing volunteers to organizations that need them most. By applying machine learning to NGO operations, HopeConnect AI demonstrates how technology can be a **force for good** — reducing friction between people who want to help and the organizations that need help.

---

## 👩‍💻 Author

**Soumyasree Mitra**
- GitHub: [@SoumyasreeMitra](https://github.com/SoumyasreeMitra)
- LinkedIn: [linkedin.com/in/soumyasreemitra](#)

---

> *Built at the intersection of artificial intelligence and social good — demonstrating that technology's greatest impact is in the lives it changes.*