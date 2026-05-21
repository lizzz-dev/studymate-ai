# 📚 StudyMate AI

> AI-powered study assistant for notes, flashcards, quizzes, uploaded study material, and progress tracking.

StudyMate AI is an open-source, offline study assistant built with Python and Streamlit. It helps students revise smarter by generating explanations, key points, flashcards, quizzes, downloadable notes, and progress history.

The app works without API keys and uses local SQLite storage for progress tracking.

---

## 🚀 Key Features

### Core Study Tools
- 📖 Generate clear explanations for study topics
- 🎯 Generate key points for revision
- 🎴 Create interactive flashcards with flip navigation
- 🧪 Generate multiple-choice quizzes with instant scoring
- 📊 Save quiz progress using SQLite
- 📥 Download generated study notes as a text file

### Unique Feature: Upload Your Own Notes
Students can upload their own `.txt` or `.md` study material. StudyMate AI then generates:
- Explanation
- Key points
- Flashcards
- Quiz questions
- Downloadable notes
- Progress history entry showing the uploaded file source

### Personalization
- 👤 Student name input
- Personalized welcome message
- Personalized progress dashboard title

### UI Enhancements
- Fixed dark theme
- Animated AI-style background effects
- Polished buttons and hover effects
- Clean Streamlit interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- SQLite
- JSON
- HTML/CSS inside Streamlit
- Rule-based offline content generation

---

## 📁 Project Structure

```text
studymate-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── .streamlit/
│   └── config.toml
│
├── utils/
│   ├── __init__.py
│   ├── generator.py
│   ├── database.py
│   └── validation.py
│
├── data/
│   └── sample_topics.json
│
└── assets/
    └── README_assets.txt