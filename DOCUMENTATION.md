# 📚 StudyMate AI Documentation

## 1. Project Overview

StudyMate AI is an offline AI-style study assistant built with Python and Streamlit.

It helps students revise smarter by generating:

- Explanations
- Key points
- Flashcards
- Quiz questions
- Downloadable study notes
- Progress history

Students can either type a topic manually or upload their own `.txt` or `.md` study material.

The app works without API keys and stores progress locally using SQLite.

---

## 2. Problem Statement

Students often struggle to revise efficiently because they need to manually create notes, flashcards, and quizzes from their study material.

This process can be time-consuming and unorganized.

StudyMate AI solves this problem by automatically converting a study topic or uploaded notes into revision-ready learning content.

---

## 3. Solution

StudyMate AI provides a simple study workflow:

```text
Student enters topic or uploads notes
↓
App generates explanation and key points
↓
App creates flashcards for active recall
↓
App creates quiz questions
↓
Student submits quiz
↓
App shows score and feedback
↓
Progress is saved locally
```

This helps students revise faster and practice active recall.

---

## 4. Main Features

### 4.1 Topic-Based Study Generation

Students can enter a topic such as:

```text
Photosynthesis
```

The app generates:

- Explanation
- Key points
- Flashcards
- Quiz questions

Sample supported topics include:

- Photosynthesis
- Python Programming
- World War II
- Mitochondria
- Democracy

The app also supports custom typed topics using offline rule-based generation.

---

### 4.2 Upload Your Own Study Notes

Students can upload their own `.txt` or `.md` study material.

The app reads the uploaded file and generates:

- Explanation from the uploaded content
- Key points from the uploaded content
- Flashcards from the uploaded content
- Quiz questions from the uploaded content
- Downloadable notes
- Progress history showing the uploaded file source

This makes the app more useful because students are not limited to sample topics.

---

### 4.3 Flashcards

StudyMate AI creates interactive flashcards.

Students can:

- View one card at a time
- Flip the card to see the answer
- Move to the next or previous card
- Practice active recall

Active recall helps students remember information by testing themselves instead of only rereading notes.

---

### 4.4 Quiz System

The app generates multiple-choice quiz questions.

After answering, students receive:

- Score
- Percentage
- Grade
- Personalized feedback

The quiz helps students check their understanding of the topic or uploaded notes.

---

### 4.5 Progress Tracking

StudyMate AI uses SQLite to save progress locally.

The progress history stores:

- Topic or uploaded file name
- Difficulty level
- Number of flashcards
- Number of quiz questions
- Quiz score
- Percentage
- Date and time

This allows students to track their study sessions and performance.

---

### 4.6 Student Personalization

Students can enter their name in the sidebar.

The app then shows:

- Personalized welcome message
- Personalized quiz feedback
- Personalized progress dashboard title

This makes the app feel more student-friendly.

---

### 4.7 Download Study Notes

Students can download generated study material as a `.txt` file.

The downloaded file includes:

- Student name
- Topic or uploaded file source
- Difficulty
- Explanation
- Key points
- Flashcards
- Quiz questions

This allows students to revise offline later.

---

## 5. Technology Stack

StudyMate AI uses:

- Python
- Streamlit
- SQLite
- JSON
- HTML/CSS inside Streamlit
- Rule-based offline content generation

---

## 6. Why This Tech Stack Was Chosen

### Python

Python is beginner-friendly and suitable for AI-style educational applications.

### Streamlit

Streamlit allows fast development of interactive web apps using only Python. It is ideal for a short app-building competition because it avoids complex frontend/backend setup.

### SQLite

SQLite is lightweight and built into Python. It does not require a separate database server, making it perfect for local progress tracking.

### Rule-Based Offline Generation

The app does not require paid APIs or internet access during the demo. This makes it more reliable for competition judging.

---

## 7. Folder Structure

```text
studymate-ai/
├── app.py
├── requirements.txt
├── README.md
├── DOCUMENTATION.md
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

## 8. File Explanation

### `app.py`

This is the main Streamlit application.

It handles:

- Page layout
- Sidebar navigation
- Student name input
- Topic input
- File upload
- Flashcard display
- Quiz display
- Quiz scoring
- Download notes
- Progress history display

---

### `utils/generator.py`

This file handles content generation.

It creates:

- Explanations
- Key points
- Flashcards
- Quiz questions

It includes topic-aware logic for sample topics and fallback generation for custom topics.

---

### `utils/database.py`

This file handles SQLite database operations.

It manages:

- Database initialization
- Saving quiz progress
- Reading progress history
- Calculating progress summary statistics

---

### `utils/validation.py`

This file handles input validation.

It checks:

- Empty topic input
- Number of flashcards
- Number of quiz questions
- Invalid inputs

---

### `data/sample_topics.json`

This file stores sample topics that users can quickly select inside the app.

---

### `.streamlit/config.toml`

This file stores Streamlit theme configuration.

It helps keep the app’s visual theme consistent.

---

### `.env.example`

This file shows optional environment configuration for future API integration.

The current version does not require API keys.

---

### `.gitignore`

This file prevents unnecessary or private files from being uploaded to GitHub.

It ignores things like:

- `venv/`
- `.env`
- `__pycache__/`
- Python cache files
- local database files
- system files

---

## 9. Setup and Run Instructions

### 9.1 Clone the Repository

```bash
git clone https://github.com/lizz-dev/studymate-ai.git
cd studymate-ai
```

### 9.2 Create a Virtual Environment

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

### 9.3 Install Dependencies

```bash
pip install -r requirements.txt
```

### 9.4 Run the Application

```bash
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

---

## 10. Requirements / Dependencies

All dependencies are listed in:

```text
requirements.txt
```

Main dependency:

```text
streamlit
```

SQLite is used through Python’s built-in SQLite support.

---

## 11. Environment Configuration

StudyMate AI works offline and does not require an API key.

The `.env.example` file is included for future API integration.

Example:

```env
# StudyMate AI currently works offline.
# Optional future API key:
OPENAI_API_KEY=your_api_key_here
```

Real `.env` files should not be uploaded to GitHub.

---

## 12. How to Use the App

### Option 1: Generate Study Material from a Topic

1. Open the app.
2. Enter student name in the sidebar.
3. Type a topic such as `Photosynthesis`.
4. Select difficulty level.
5. Choose number of flashcards.
6. Choose number of quiz questions.
7. Click **Generate Study Materials**.
8. Review explanation and key points.
9. Use flashcards.
10. Answer quiz questions.
11. Submit quiz.
12. View score and feedback.
13. Download notes.
14. Open Progress History to see saved attempt.

---

### Option 2: Generate Study Material from Uploaded Notes

1. Open the app.
2. Upload a `.txt` or `.md` file.
3. Select difficulty level.
4. Choose number of flashcards and quiz questions.
5. Click **Generate Study Materials**.
6. Review explanation, key points, flashcards, and quiz.
7. Submit quiz.
8. Download generated notes.
9. Open Progress History to confirm the uploaded file attempt was saved.

---

## 13. Database and Progress Tracking

StudyMate AI uses SQLite for local progress tracking.

When a quiz is submitted, the app saves:

- Topic or uploaded file source
- Difficulty level
- Number of flashcards
- Number of quiz questions
- Quiz score
- Total questions
- Percentage
- Date and time

The Progress History page displays:

- Total study sessions
- Average score
- Unique topics
- Recent study attempts

---

## 14. Validation and Safety

The app includes:

- Empty topic validation
- Uploaded file validation
- Friendly error messages
- Quiz reset after generating new materials
- Protection against duplicate progress saving
- No hardcoded API keys
- `.env.example` instead of real `.env`
- `.gitignore` to prevent unnecessary/private files from being uploaded

---

## 15. GitHub and Version Control Practices

The project is pushed to GitHub.

The repository includes:

- Source code
- README
- Documentation
- Requirements file
- Environment example file
- Clean folder structure

The repository does not include:

- Virtual environment folder
- Real `.env` file
- Python cache files
- Local database files
- Unnecessary generated files

---

## 16. Current Limitations

- The app currently supports `.txt` and `.md` file uploads.
- PDF upload is not supported in the current version.
- The app uses offline rule-based generation instead of a real AI API.
- Progress is stored locally, not in the cloud.
- There is no full login/signup system yet.

---

## 17. Future Improvements

Possible future improvements include:

- PDF upload support
- Secure login/signup with password hashing
- Separate student profiles
- Spaced repetition flashcards
- AI API integration using `.env`
- Export study reports as PDF
- More advanced progress analytics
- Multi-language support
- Cloud database support

---

## 18. 5-Minute Demo Flow

Use this flow for the screen recording:

### 0:00 – 0:30 | Introduction

Say:

"Hello, this is StudyMate AI. It is an open-source study assistant built for students. It helps students revise topics using explanations, flashcards, quizzes, uploaded notes, and progress tracking."

Show:

- GitHub repository
- Project folder
- Running app

---

### 0:30 – 1:00 | Student Personalization

Say:

"The student can enter their name in the sidebar to personalize the study experience."

Show:

- Enter student name
- Personalized welcome message

---

### 1:00 – 2:00 | Generate from Typed Topic

Say:

"The student can type a topic or choose from sample topics. The app generates study materials based on difficulty level."

Show:

- Type `Photosynthesis`
- Select difficulty
- Choose flashcards and quiz count
- Generate materials

---

### 2:00 – 2:45 | Explanation and Flashcards

Say:

"The app creates explanation, key points, and interactive flashcards for active recall."

Show:

- Explanation tab
- Key points
- Flashcard flip
- Next/previous flashcard buttons

---

### 2:45 – 3:30 | Quiz and Score

Say:

"The quiz checks understanding. After submission, the app shows score, percentage, grade, and personalized feedback."

Show:

- Quiz tab
- Answer questions
- Submit quiz
- Score and feedback

---

### 3:30 – 4:20 | Upload Own Notes

Say:

"A unique feature is that students can upload their own notes. The app generates explanation, flashcards, quiz questions, and downloadable notes from the uploaded file."

Show:

- Upload `.txt` file
- Generate materials from uploaded notes
- Show uploaded-file content

---

### 4:20 – 4:45 | Download Notes

Say:

"The student can download the generated study notes for offline revision."

Show:

- Download tab
- Download button

---

### 4:45 – 5:00 | Progress History

Say:

"The Progress History page saves quiz attempts locally using SQLite. It shows total sessions, average score, unique topics, and recent attempts."

Show:

- Progress History page
- Summary cards
- Recent study sessions table

---

## 19. Judge Q&A

### Q1. Does this app require API keys?

No. StudyMate AI works offline using rule-based generation. `.env.example` is included for future AI API integration.

---

### Q2. Where is progress saved?

Progress is saved locally using SQLite.

---

### Q3. What makes the app unique?

The app allows students to upload their own `.txt` or `.md` notes and automatically generate study material from their own content.

---

### Q4. Why no login/signup?

Login/signup was not required by the core task. The current version focuses on the main learning workflow. A future version can add secure authentication with password hashing and separate student profiles.

---

### Q5. Why did you choose Streamlit?

Streamlit was chosen because it allows fast development of interactive Python web apps. It helped build a working competition-ready app quickly without needing complex frontend/backend setup.

---

### Q6. Is it real AI?

The current version is an offline AI-style learning assistant using rule-based content generation. This makes the app reliable without internet or paid APIs. The structure can support real AI API integration in the future using `.env`.

---

### Q7. What would you improve with more time?

I would add PDF upload, secure login/signup, spaced repetition, PDF export, and optional AI API integration.

---

## 20. 30-Second Pitch

StudyMate AI is an offline AI-style study assistant that helps students revise smarter. A student can type a topic or upload their own notes, and the app generates explanations, key points, flashcards, quizzes, downloadable notes, and progress history. It is beginner-friendly, open-source, GitHub-ready, and works without API keys.

---

## 21. GitHub Repository

Project repository:

```text
https://github.com/lizz-dev/studymate-ai
```