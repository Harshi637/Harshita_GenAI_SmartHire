# 📄 SmartHire GenAI

An AI-powered career assistance platform that helps candidates analyze resumes, discover relevant jobs, improve their resumes, and receive personalized career guidance using Generative AI.

Upload a resume → AI extracts a structured profile → semantic search retrieves matching jobs → AI generates resume improvement suggestions → Career Mentor answers career-related questions.

---

## 🚀 Features

### 📄 Resume Parser
- Upload PDF resumes.
- Extract resume text using PyPDF2.
- Parse resumes into structured JSON using Gemini 3.5 Flash.
- Resume caching to reduce API usage.

Extracted fields include:
- Name
- Email
- Phone
- Skills
- Education
- Career Domain
- Current Role
- Target Role
- Experience
- Certifications
- Professional Summary

---

### 🔍 Semantic Job Search

- Uses Sentence Transformers to generate embeddings.
- FAISS vector database for semantic similarity search.
- Returns Top-5 most relevant jobs.
- Domain-aware search query generation.

---

### 🤖 AI Resume Suggestions

Analyzes:

- Resume
- Candidate profile
- Target job

Generates:

- ATS Score
- Missing Skills
- Resume Improvements
- Recommended Certifications
- Professional Summary
- Action Items

Suggestions are domain-aware and avoid irrelevant recommendations.

---

### 🎯 AI Career Mentor

Interactive AI assistant that provides:

- Career Roadmaps
- Skill Recommendations
- Certification Guidance
- Domain-specific Career Advice
- Experience-aware Suggestions

The mentor adapts recommendations based on:

- Career Domain
- Experience Level
- Current Role
- Target Role

---

### ⚡ Resume Cache

Parsed resumes are cached using SHA-256 hashing.

Benefits:

- Faster response
- Reduced Gemini API calls
- Lower API usage

---

### 🌐 Deployment

The application is deployed using Streamlit Community Cloud.

---

# 🛠 Tech Stack

| Category | Technology |
|-----------|------------|
| Language | Python |
| Frontend | Streamlit |
| LLM | Gemini 3.5 Flash |
| Embeddings | Sentence Transformers |
| Vector Database | FAISS |
| PDF Processing | PyPDF2 |
| Data Processing | Pandas |
| Environment | python-dotenv |
| Deployment | Streamlit Community Cloud |
| Version Control | Git & GitHub |

---

# 📂 Project Structure

```
Harshita_GenAI_SmartHire/
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── assets/
│
├── cache/
│
├── components/
│   ├── sidebar.py
│   ├── resume_card.py
│   ├── job_card.py
│   └── tabs.py
│
├── data/
│   ├── job_market.csv
│   ├── postings_processed.csv
│   └── sample resumes
│
├── modules/
│   ├── parser.py
│   ├── embedding.py
│   ├── search.py
│   ├── suggestions.py
│   └── mentor.py
│
├── scripts/
│   ├── build_vectorstore.py
│   └── test_embedding.py
│
├── utils/
│   ├── gemini_client.py
│   └── helpers.py
│
└── vectorstore/
    ├── jobs.index
    └── jobs.pkl
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone <YOUR_GITHUB_REPO>
cd Harshita_GenAI_SmartHire
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Mac/Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure API Key

Create a `.env`

```
GEMINI_API_KEY=YOUR_API_KEY
```

Never commit the `.env` file.

---

# 📊 Dataset

The project uses a job market dataset containing thousands of job postings across multiple domains including:

- Information Technology
- Finance
- Healthcare
- Manufacturing
- Education
- Government
- Consulting
- Retail
- Logistics
- Media

The dataset is embedded using Sentence Transformers and indexed using FAISS for semantic retrieval.

---

# ▶️ Build Vector Store

Generate embeddings and create the FAISS index.

```bash
python -m scripts.build_vectorstore
```

This creates:

```
vectorstore/
├── jobs.index
└── jobs.pkl
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🧠 System Workflow

```
Resume Upload
      │
      ▼
PDF Reader (PyPDF2)
      │
      ▼
Gemini Resume Parser
      │
      ▼
Structured Candidate Profile
      │
      ├───────────────► Resume Cache
      │
      ▼
Search Query Builder
      │
      ▼
Sentence Transformer
      │
      ▼
FAISS Vector Search
      │
      ▼
Top 5 Matching Jobs
      │
      ├────────────► AI Resume Suggestions
      │
      └────────────► AI Career Mentor
      │
      ▼
Streamlit User Interface
```

---

# 🎯 Key Improvements

Compared to the initial implementation:

- ✅ Domain-aware Resume Parser
- ✅ Improved Search Query Generation
- ✅ Enhanced Prompt Engineering
- ✅ Smarter AI Resume Suggestions
- ✅ Personalized Career Mentor
- ✅ Resume Caching
- ✅ Larger Multi-domain Dataset
- ✅ Gemini 3.5 Flash Integration
- ✅ Streamlit Deployment

---

# 🔮 Future Enhancements

- Live Job API Integration
- Multi-language Resume Support
- Voice-based Career Mentor
- Resume Rewriting
- Company-specific Interview Preparation
- Explainable Job Matching
- Conversation Memory

---

# 👩‍💻 Author

**Harshita Arisetti**

B.Tech Computer Science Engineering

IIIT Tiruchirappalli

GitHub:
https://github.com/Harshi637

LinkedIn:
https://www.linkedin.com/in/arisetti-harshita-733868377

---

# ⭐ Acknowledgements

This project was developed as part of the Generative AI Capstone Project using:

- Google Gemini API
- Sentence Transformers
- FAISS
- Streamlit
- Python
