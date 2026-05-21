# 📚 StudyMate AI

[![Open Source](https://img.shields.io/badge/Open%20Source-Yes-green)](https://github.com/)
[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> **AI-powered study assistant for notes, flashcards, quizzes, and progress tracking** 🎓

StudyMate AI is a beginner-friendly, open-source study companion that helps students understand and revise topics effectively. Built with Python and Streamlit, it requires **no API keys** and works completely offline using intelligent rule-based content generation.

## ✨ Features

### Core Study Tools
- 📖 **Intelligent Explanations** - Clear, difficulty-adjusted explanations for any topic
- 🎴 **Interactive Flashcards** - Create and flip through flashcards with immediate feedback
- 🧪 **Practice Quizzes** - Multiple-choice questions with instant scoring and explanations
- 📊 **Progress Tracking** - Automatic tracking of study sessions with detailed history
- 📥 **Download Notes** - Export your generated study materials as text files

### Student-Friendly Features
- 🎯 **Difficulty Levels** - Beginner, Intermediate, and Advanced content
- 💡 **Sample Topics** - Quick-start with pre-loaded study topics
- ✅ **Input Validation** - Friendly error messages for incorrect inputs
- 🔄 **Loading States** - Clear feedback during content generation
- 📱 **Responsive UI** - Clean, intuitive interface built with Streamlit

### Offline & Privacy-First
- ✔️ **No API Keys Required** - Works completely offline
- 🔐 **Local Data Storage** - Progress saved locally in SQLite
- 📦 **Lightweight** - Minimal dependencies, quick setup
- 🚀 **Easy Deployment** - Works on any machine with Python

## 📁 Project Structure

```
StudyMate-AI/
├── app.py                    # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── .env.example             # Environment variables template
│
├── utils/
│   ├── __init__.py          # Utils package initialization
│   ├── generator.py         # Rule-based content generation
│   ├── database.py          # SQLite database operations
│   └── validation.py        # Input validation utilities
│
├── data/
│   └── sample_topics.json   # Pre-loaded sample topics
│
└── assets/
    └── README_assets.txt    # Assets documentation
```

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the repository:**
   ```bash
   cd StudyMate-AI
   ```

2. **Create a virtual environment (recommended):**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate
   
   # On macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Set up environment variables:**
   ```bash
   copy .env.example .env
   # Edit .env file if needed (currently no required keys)
   ```

### Running the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## 📖 How to Use

### Study Mode

1. **Enter a Topic** - Type any subject you want to study
   - Use the "Suggest" button for random topics
   - Click sample topics for quick demos

2. **Select Difficulty** - Choose from:
   - 🟢 Beginner - Basic concepts and simple explanations
   - 🟡 Intermediate - More detailed analysis
   - 🔴 Advanced - Complex, analytical content

3. **Configure Study Materials**
   - Number of Flashcards (1-20)
   - Number of Quiz Questions (1-10)

4. **Generate Materials** - Click "Generate Study Materials"
   - Get instant explanations and key points
   - Review interactive flashcards
   - Take practice quizzes
   - Download your notes

### Progress Tracking

- View your study history in the "Progress History" page
- See statistics: Total Sessions, Average Score, Unique Topics
- Track your performance over time
- Performance data is saved locally in SQLite

## 🛠️ Technical Details

### Technology Stack
- **Frontend:** Streamlit (interactive web UI)
- **Backend:** Python 3.8+
- **Database:** SQLite (local progress storage)
- **Content Generation:** Rule-based system (no API required)

### Key Components

#### `app.py`
Main application file with:
- Streamlit UI setup and configuration
- User input handling
- Study material display and interaction
- Quiz scoring and results
- Progress history visualization

#### `utils/generator.py`
Content generation engine:
- Rule-based flashcard creation
- Quiz question generation
- Explanation and key points generation
- Template-based content for different difficulty levels

#### `utils/database.py`
SQLite database management:
- Progress tracking and storage
- History retrieval and statistics
- Summary calculations

#### `utils/validation.py`
Input validation:
- Topic validation
- Parameter validation
- User-friendly error messages

## 📊 Example Topics

StudyMate AI includes sample topics to get you started:
- 📚 **Biology**: Photosynthesis, Mitochondria, DNA Structure
- 💻 **Computer Science**: Python Programming
- 📜 **History**: World War II, Renaissance
- 🌍 **Other**: Democracy, Calculus, Shakespeare, Climate Change

## 🔒 Data & Privacy

- **No Cloud Storage** - All data stored locally on your machine
- **No Tracking** - No analytics or telemetry
- **No API Keys** - Works completely offline
- **SQLite Database** - Local, portable database format

## 🎓 Use Cases

- 📚 **Students** - Study and revise for exams
- 👨‍🏫 **Tutors** - Generate practice materials
- 🧠 **Lifelong Learners** - Quick topic overviews
- 👶 **Beginners** - Learn new concepts step-by-step

## 📈 Future Improvements

- [ ] Integration with OpenAI API for enhanced content
- [ ] Export progress reports in PDF format
- [ ] Spaced repetition algorithm for flashcards
- [ ] User accounts and cloud sync
- [ ] More sample topics and subjects
- [ ] Multi-language support
- [ ] Mobile app version
- [ ] Integration with learning platforms
- [ ] Collaborative study groups
- [ ] AI-powered adaptive difficulty

## 🤝 Contributing

Contributions are welcome! This is an open-source project.

### To contribute:
1. Fork the repository
2. Create a feature branch
3. Make your improvements
4. Submit a pull request

### Areas for contribution:
- New content generation templates
- Additional sample topics
- UI/UX improvements
- Performance optimization
- Bug fixes
- Documentation

## 📝 Demo Script

### Quick Demo Session

```
1. Open app with: streamlit run app.py
2. Enter topic: "Photosynthesis"
3. Select: Beginner, 5 Flashcards, 5 Questions
4. Click "Generate Study Materials"
5. Read the explanation and key points
6. Review flashcards (use Flip button)
7. Take the quiz and see your score
8. Download your notes
9. Check Progress History tab
```

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:** Install dependencies with `pip install -r requirements.txt`

### Issue: "Port 8501 already in use"
**Solution:** Kill the existing Streamlit process or use `streamlit run app.py --logger.level=debug --server.port 8502`

### Issue: Database errors
**Solution:** Delete `studymate_progress.db` and restart the app to reinitialize

### Issue: Sample topics not loading
**Solution:** Ensure `data/sample_topics.json` exists in the project directory

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

Created for the open-source AI app-building competition.

**Developed with ❤️ for students everywhere.**

---

## 🌟 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) - The fastest way to build web apps
- Inspired by effective learning methodologies
- Community feedback and contributions

---

## 📚 Learn More

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Python Documentation](https://docs.python.org/3/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

---

**Happy Studying! 📖✨**

*Questions or suggestions? Feel free to open an issue or contribute to the project.*
