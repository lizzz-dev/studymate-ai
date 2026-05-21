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
```

---

## ⚙️ Setup & Run Guide

### 1. Clone the Repository

```bash
git clone https://github.com/lizz-dev/studymate-ai.git
cd studymate-ai
```

### 2. Create a Virtual Environment

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 📦 Requirements / Dependencies

All required Python packages are listed in:

```text
requirements.txt
```

Main dependency:

```text
streamlit
```

The app uses Python’s built-in SQLite support for local progress tracking.

---

## 🔐 Environment Configuration

StudyMate AI works offline and does not require any API key.

An `.env.example` file is included for future API integration.

Example:

```env
# StudyMate AI currently works offline.
# Optional future API key:
OPENAI_API_KEY=your_api_key_here
```

Do not upload real `.env` files to GitHub.

---

## 📖 How to Use

### Option 1: Generate from a Topic

1. Enter your student name in the sidebar.
2. Type a topic such as `Photosynthesis`.
3. Select difficulty level.
4. Choose number of flashcards and quiz questions.
5. Click **Generate Study Materials**.
6. Review explanation, key points, flashcards, and quiz.
7. Submit quiz and view your score.
8. Download notes.
9. Open Progress History to see saved attempts.

### Option 2: Generate from Uploaded Notes

1. Upload a `.txt` or `.md` file containing study material.
2. Click **Generate Study Materials**.
3. StudyMate AI creates explanation, key points, flashcards, and quiz questions from the uploaded file.
4. Submit the quiz.
5. Progress History records the uploaded file source.
6. Download the generated study notes.

---

## 🗃️ Progress Tracking

StudyMate AI uses SQLite to save local progress.

It stores:

- Topic or uploaded file name
- Difficulty level
- Number of flashcards
- Number of quiz questions
- Quiz score
- Percentage
- Date/time

---

## ✅ Validation and Safety

The app includes:

- Empty topic checks
- Uploaded file validation
- Friendly error messages
- Quiz reset after new generation
- Protection against duplicate progress saves
- `.gitignore` to avoid uploading virtual environments, cache files, databases, and secret files

---

## 🎥 5-Minute Demo Flow

Suggested screen recording flow:

1. Open StudyMate AI.
2. Enter student name.
3. Generate study materials from a typed topic.
4. Show explanation and key points.
5. Flip through flashcards.
6. Submit quiz and show score feedback.
7. Upload a `.txt` notes file.
8. Generate study materials from uploaded notes.
9. Download notes.
10. Open Progress History and show saved attempts.

---

## 🌟 Future Improvements

- PDF upload support
- Secure login/signup with password hashing
- Separate student profiles
- Spaced repetition for flashcards
- AI API integration using `.env`
- Export study reports as PDF
- More advanced progress analytics
- Multi-language support

---

## 🎯 30-Second Pitch

StudyMate AI is an offline AI-style study assistant that helps students revise smarter. A student can type a topic or upload their own notes, and the app generates explanations, key points, flashcards, quizzes, downloadable notes, and progress history. It is beginner-friendly, open-source, GitHub-ready, and works without API keys.

---

## 👨‍💻 Author

Created for an open-source AI app-building competition.

GitHub: https://github.com/lizz-dev/studymate-ai