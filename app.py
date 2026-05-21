"""
StudyMate AI - AI-Powered Study Assistant
Build understanding with notes, flashcards, quizzes, and progress tracking.

An open-source study companion that helps students learn effectively
using rule-based offline content generation.
"""

import streamlit as st
import json
import random
import re
from datetime import datetime
from utils.generator import StudyMaterialGenerator
from utils.database import init_database, save_progress, get_progress_history, get_progress_summary
from utils.validation import validate_topic, validate_num_flashcards, validate_num_questions


# Page configuration
st.set_page_config(
    page_title="StudyMate AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize database
init_database()

# Custom CSS for better UI
st.markdown("""
    <style>
    /* Full app background */
    .stApp {
        background:
            radial-gradient(circle at top left, rgba(255, 75, 92, 0.16), transparent 35%),
            radial-gradient(circle at top right, rgba(112, 96, 255, 0.14), transparent 35%),
            linear-gradient(135deg, #090b12 0%, #10131f 45%, #090b12 100%);
        color: #f5f7fb;
    }

    /* Smooth page entrance */
    .block-container {
        animation: fadeSlideIn 0.55s ease-in-out;
        padding-top: 2rem;
    }

    @keyframes fadeSlideIn {
        from {
            opacity: 0;
            transform: translateY(14px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #171923 0%, #10131f 100%);
        border-right: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* Buttons */
    .stButton > button,
    .stDownloadButton > button {
        width: 100%;
        border-radius: 14px;
        font-weight: 700;
        border: 1px solid rgba(255, 75, 92, 0.45);
        background: linear-gradient(135deg, #ff4b5c 0%, #b83280 55%, #6c5ce7 100%);
        color: white;
        box-shadow: 0 0 18px rgba(255, 75, 92, 0.25);
        transition: all 0.22s ease-in-out;
        position: relative;
        overflow: hidden;
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        transform: translateY(-2px) scale(1.01);
        box-shadow: 0 0 26px rgba(255, 75, 92, 0.55);
        border: 1px solid rgba(255, 255, 255, 0.55);
    }

    .stButton > button:active,
    .stDownloadButton > button:active {
        transform: scale(0.98);
    }

    /* Inputs and dropdowns */
    input,
    textarea,
    div[data-baseweb="select"] {
        border-radius: 12px !important;
    }

    div[data-baseweb="select"] > div {
        background-color: #1f2330 !important;
        border: 1px solid rgba(255, 255, 255, 0.12) !important;
    }

    /* Tabs */
    button[data-baseweb="tab"] {
        font-weight: 700;
        transition: all 0.2s ease-in-out;
    }

    button[data-baseweb="tab"]:hover {
        color: #ff4b5c !important;
        transform: translateY(-1px);
    }

    /* Metric cards */
    div[data-testid="stMetric"] {
        background: rgba(255, 255, 255, 0.045);
        border: 1px solid rgba(255, 255, 255, 0.08);
        padding: 1rem;
        border-radius: 18px;
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.25);
        transition: all 0.22s ease-in-out;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-3px);
        border-color: rgba(255, 75, 92, 0.45);
        box-shadow: 0 10px 30px rgba(255, 75, 92, 0.18);
    }

    /* Dataframe/table polish */
    div[data-testid="stDataFrame"] {
        border-radius: 16px;
        overflow: hidden;
        border: 1px solid rgba(255, 255, 255, 0.08);
    }

    /* File uploader polish */
    section[data-testid="stFileUploader"] {
        border: 1px dashed rgba(255, 75, 92, 0.55);
        border-radius: 18px;
        padding: 0.75rem;
        background: rgba(255, 255, 255, 0.035);
        transition: all 0.22s ease-in-out;
    }

    section[data-testid="stFileUploader"]:hover {
        box-shadow: 0 0 24px rgba(255, 75, 92, 0.22);
        transform: translateY(-2px);
    }

    /* Alert boxes slightly rounded */
    div[data-testid="stAlert"] {
        border-radius: 16px;
        animation: softPop 0.35s ease-in-out;
    }

    @keyframes softPop {
        from {
            opacity: 0;
            transform: scale(0.98);
        }
        to {
            opacity: 1;
            transform: scale(1);
        }
    }

    /* Make clickable Streamlit widgets show hand cursor */
    button,
    .stButton > button,
    .stDownloadButton > button,
    div[data-baseweb="select"],
    div[data-baseweb="select"] *,
    div[data-testid="stSelectbox"],
    div[data-testid="stSelectbox"] *,
    div[data-testid="stSlider"],
    div[data-testid="stSlider"] *,
    input[type="range"] {
        cursor: pointer !important;
    }

    /* Text input should still show normal typing cursor */
    input[type="text"],
    textarea {
        cursor: text !important;
    }



@keyframes floatBlob {
    0% {
        transform: translateY(0px) translateX(0px) scale(1);
    }
    25% {
        transform: translateY(-20px) translateX(15px) scale(1.05);
    }
    50% {
        transform: translateY(10px) translateX(-18px) scale(0.96);
    }
    75% {
        transform: translateY(-12px) translateX(10px) scale(1.03);
    }
    100% {
        transform: translateY(0px) translateX(0px) scale(1);
    }
}

/* Make sure main content stays above blobs */
.block-container {
    position: relative;
    z-index: 1;
}

section[data-testid="stSidebar"] {
    position: relative;
    z-index: 2;
}

/* Animated AI background layer */
.ai-bg-blob,
.ai-bg-line {
    position: fixed;
    pointer-events: none;
    z-index: 0;
}

/* Stronger visible floating blobs */
.ai-bg-blob {
    border-radius: 50%;
    filter: blur(55px);
    opacity: 0.14;
    animation: blobFloat 20s ease-in-out infinite alternate;
}

.ai-blob-1 {
    width: 280px;
    height: 280px;
    background: #ff4b5c;
    top: 9%;
    left: 6%;
    animation-delay: 0s;
}

.ai-blob-2 {
    width: 330px;
    height: 330px;
    background: #6c5ce7;
    top: 30%;
    right: 5%;
    animation-delay: 1.5s;
}

.ai-blob-3 {
    width: 240px;
    height: 240px;
    background: #00c2ff;
    bottom: 10%;
    left: 32%;
    animation-delay: 3s;
}

@keyframes blobFloat {
    0% {
        transform: translate(0px, 0px) scale(1);
    }
    50% {
        transform: translate(55px, -45px) scale(1.12);
    }
    100% {
        transform: translate(-35px, 45px) scale(0.95);
    }
}

/* Floating neon lines */
.ai-bg-line {
    width: 160px;
    height: 2px;
    background: linear-gradient(90deg, transparent, rgba(255, 75, 92, 0.85), transparent);
    opacity: 0.45;
    animation: lineFloat 11s linear infinite;
}

.ai-line-1 {
    top: 18%;
    left: -180px;
    animation-delay: 0s;
}

.ai-line-2 {
    top: 46%;
    left: -220px;
    animation-delay: 3s;
    background: linear-gradient(90deg, transparent, rgba(108, 92, 231, 0.85), transparent);
}

.ai-line-3 {
    top: 72%;
    left: -260px;
    animation-delay: 6s;
    background: linear-gradient(90deg, transparent, rgba(0, 194, 255, 0.85), transparent);
}

@keyframes lineFloat {
    0% {
        transform: translateX(0) rotate(-12deg);
        opacity: 0;
    }
    15% {
        opacity: 0.55;
    }
    85% {
        opacity: 0.55;
    }
    100% {
        transform: translateX(130vw) rotate(-12deg);
        opacity: 0;
    }
}

/* Keep actual app content above animations */
.block-container {
    position: relative;
    z-index: 2;
}

section[data-testid="stSidebar"] {
    position: relative;
    z-index: 3;
}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="ai-bg-blob ai-blob-1"></div>
<div class="ai-bg-blob ai-blob-2"></div>
<div class="ai-bg-blob ai-blob-3"></div>

<div class="ai-bg-line ai-line-1"></div>
<div class="ai-bg-line ai-line-2"></div>
<div class="ai-bg-line ai-line-3"></div>
""", unsafe_allow_html=True)



def load_sample_topics():
    """Load sample topics from JSON file."""
    try:
        with open("data/sample_topics.json", "r") as f:
            data = json.load(f)
            return [topic["name"] for topic in data["sample_topics"]]
    except Exception as e:
        st.warning(f"Could not load sample topics: {e}")
        return ["Photosynthesis", "Python Programming", "World War II"]


def get_student_name():
    """Return the student's name from session state."""
    return st.session_state.get("student_name", "").strip()


def get_student_label():
    """Return student name or default label."""
    student_name = get_student_name()
    return student_name if student_name else "Student"


def set_topic(topic):
    """Callback to set the selected topic via button."""
    st.session_state.topic_input = topic
    st.session_state.selected_sample_topic = topic


def suggest_random_topic():
    """Callback to set a randomly suggested topic."""
    sample_topics = load_sample_topics()
    topic = random.choice(sample_topics)
    st.session_state.topic_input = topic
    st.session_state.selected_sample_topic = topic


def read_uploaded_text_file(uploaded_file):
    """Read text from an uploaded .txt or .md file safely."""
    if uploaded_file is None:
        return None, None

    try:
        file_name = uploaded_file.name
        raw_bytes = uploaded_file.getvalue()

        try:
            text = raw_bytes.decode("utf-8")
        except UnicodeDecodeError:
            text = raw_bytes.decode("latin-1")

        text = text.strip()

        if not text:
            return None, "The uploaded file is empty. Please upload a file with study notes."

        if len(text) < 50:
            return None, "The uploaded file is too short. Please upload more detailed study material."

        return {
            "file_name": file_name,
            "text": text
        }, None

    except Exception as e:
        return None, f"Could not read uploaded file: {e}"


def split_study_sentences(text):
    """Split uploaded study material into useful sentence-like chunks."""
    cleaned = text.replace("\t", " ").strip()

    # Remove common report/header lines that should not become key points
    lines = cleaned.splitlines()
    useful_lines = []

    skip_phrases = [
        "STUDYMATE AI",
        "STUDY NOTES",
        "Generated:",
        "Student:",
        "Source Type:",
        "File Name:",
        "Topic:",
        "Difficulty:",
        "EXPLANATION",
        "KEY POINTS",
        "FLASHCARDS",
        "QUIZ QUESTIONS",
        "==========",
        "----------"
    ]

    for line in lines:
        line = line.strip()

        if not line:
            continue

        if any(phrase.lower() in line.lower() for phrase in skip_phrases):
            continue

        if set(line) in [{"="}, {"-"}, {"_"}]:
            continue

        useful_lines.append(line)

    cleaned = " ".join(useful_lines)

    parts = re.split(r"(?<=[.!?])\s+|\n+", cleaned)

    sentences = []
    for part in parts:
        sentence = part.strip(" -•\n\r\t")

        if len(sentence) > 25:
            sentences.append(sentence)

    if not sentences:
        words = cleaned.split()
        chunks = []

        for i in range(0, len(words), 30):
            chunk = " ".join(words[i:i + 30]).strip()

            if len(chunk) > 25:
                chunks.append(chunk)

        sentences = chunks

    return sentences[:60]


def sample_with_replacement(items, count):
    """Return requested number of items, repeating only if needed."""
    if not items:
        return []

    if count <= len(items):
        return random.sample(items, count)

    selected = items[:]
    while len(selected) < count:
        selected.append(random.choice(items))

    random.shuffle(selected)
    return selected[:count]


def make_uploaded_file_options(correct_answer, all_facts):
    """Create simple multiple-choice options from uploaded file facts."""
    wrong_pool = []

    for fact in all_facts:
        if fact != correct_answer and fact not in wrong_pool and len(fact) > 20:
            wrong_pool.append(fact)

    fallback_wrong = [
        "This is not directly supported by the uploaded material.",
        "This is a common misunderstanding of the uploaded notes.",
        "This answer is too general and misses the main idea.",
        "This option does not match the uploaded study material.",
        "This point is unrelated to the uploaded file."
    ]

    while len(wrong_pool) < 3:
        wrong_answer = random.choice(fallback_wrong)
        if wrong_answer not in wrong_pool:
            wrong_pool.append(wrong_answer)

    options = [correct_answer] + random.sample(wrong_pool, 3)
    random.shuffle(options)
    return options


def generate_materials_from_uploaded_file(file_name, file_text, difficulty, num_flashcards, num_questions):
    """Generate study materials from uploaded student notes."""
    sentences = split_study_sentences(file_text)

    if not sentences:
        sentences = [
            "The uploaded material contains important study information.",
            "Students should review the uploaded notes carefully.",
            "Key ideas can be turned into flashcards and quiz questions."
        ]

    source_title = f"Uploaded File: {file_name}"

    explanation_sentences = sentences[:min(5, len(sentences))]
    explanation = " ".join(explanation_sentences)

    key_point_count = min(12, len(sentences))
    key_points = sentences[:key_point_count]

    flashcards = []
    selected_flashcard_facts = sample_with_replacement(sentences, num_flashcards)

    for index, fact in enumerate(selected_flashcard_facts, start=1):
        question_templates = [
            f"What important idea is explained in this part of {file_name}?",
            f"According to the uploaded notes, what should you remember from point {index}?",
            f"How would you summarize this uploaded-note idea?",
            f"What is a key takeaway from the uploaded material?",
            f"What should a student recall from this section of the file?"
        ]

        flashcards.append({
            "id": index,
            "question": random.choice(question_templates),
            "answer": fact
        })

    quiz = []
    selected_quiz_facts = sample_with_replacement(sentences, num_questions)

    for index, correct_fact in enumerate(selected_quiz_facts, start=1):
        quiz_question_templates = [
            f"Which statement is supported by the uploaded file '{file_name}'?",
            f"Based on the uploaded notes, which option is correct?",
            f"What does the uploaded study material say?",
            f"Which point best matches the uploaded notes?",
            f"What should the student remember from the uploaded file?"
        ]

        quiz.append({
            "id": index,
            "question": random.choice(quiz_question_templates),
            "options": make_uploaded_file_options(correct_fact, sentences),
            "correct_answer": correct_fact,
            "explanation": "This answer was selected from the uploaded study material."
        })

    notes = f"""
StudyMate AI Notes From Uploaded File

Source: {file_name}
Difficulty: {difficulty}

Explanation:
{explanation}

Key Points:
{chr(10).join("- " + point for point in key_points)}
"""

    return {
        "topic": source_title,
        "difficulty": difficulty,
        "explanation": explanation,
        "key_points": key_points,
        "flashcards": flashcards,
        "quiz": quiz,
        "quiz_questions": quiz,
        "notes": notes,
        "study_notes": notes,
        "summary": explanation,
        "source_type": "Uploaded File",
        "file_name": file_name
    }


def render_explanation(materials):
    """Render the explanation section."""
    st.subheader("📖 Explanation")
    st.info(materials["explanation"])

    st.subheader("🎯 Key Points")
    for i, point in enumerate(materials["key_points"], 1):
        st.write(f"{i}. {point}")


def render_flashcards(materials):
    """Render flashcards section."""
    st.subheader("🎴 Flashcards")

    flashcards = materials["flashcards"]

    # Initialize flashcard state
    if "current_card" not in st.session_state:
        st.session_state.current_card = 0

    if "flipped" not in st.session_state:
        st.session_state.flipped = [False] * len(flashcards)

    # Safety reset if number of flashcards changes
    if len(st.session_state.flipped) != len(flashcards):
        st.session_state.flipped = [False] * len(flashcards)
        st.session_state.current_card = 0

    if flashcards:
        if st.session_state.current_card >= len(flashcards):
            st.session_state.current_card = 0

        current_idx = st.session_state.current_card
        card = flashcards[current_idx]

        # Progress bar
        st.progress((current_idx + 1) / len(flashcards))
        st.write(f"Card {current_idx + 1} of {len(flashcards)}")

        # Flashcard display
        col1, col2 = st.columns([3, 1])

        with col1:
            if st.session_state.flipped[current_idx]:
                st.success(f"✅ **Answer**: {card['answer']}")
            else:
                st.warning(f"❓ **Question**: {card['question']}")

        with col2:
            if st.button("🔄 Flip", key=f"flip_{current_idx}"):
                st.session_state.flipped[current_idx] = not st.session_state.flipped[current_idx]
                st.rerun()

        # Navigation buttons
        col1, col2, col3 = st.columns(3)

        with col1:
            if current_idx > 0:
                if st.button("⬅️ Previous"):
                    st.session_state.current_card -= 1
                    st.rerun()

        with col3:
            if current_idx < len(flashcards) - 1:
                if st.button("Next ➡️"):
                    st.session_state.current_card += 1
                    st.rerun()

def render_quiz(materials):
    """Render quiz section with scoring."""
    st.subheader("🧪 Quiz Questions")

    questions = materials["quiz_questions"]

    # Initialize quiz state
    if "quiz_responses" not in st.session_state:
        st.session_state.quiz_responses = {}

    if "quiz_submitted" not in st.session_state:
        st.session_state.quiz_submitted = False

    if "quiz_progress_saved" not in st.session_state:
        st.session_state.quiz_progress_saved = False

    if "quiz_run_id" not in st.session_state:
        st.session_state.quiz_run_id = 0

    unanswered_questions = []

    # Display questions
    for i, question in enumerate(questions):
        st.write(f"**Question {i + 1}**: {question['question']}")

        response = st.radio(
            label="Select your answer:",
            options=question["options"],
            index=None,
            key=f"q_{st.session_state.quiz_run_id}_{i}",
            label_visibility="collapsed"
        )

        st.session_state.quiz_responses[i] = response

        if response is None:
            unanswered_questions.append(i + 1)

        st.write("---")

    # Submit button
    if st.button("📊 Submit Quiz", type="primary"):
        if unanswered_questions:
            st.warning(
                f"Please answer all questions before submitting. "
                f"Missing: {', '.join(map(str, unanswered_questions))}"
            )
        else:
            st.session_state.quiz_submitted = True
            st.rerun()

    # Show results if submitted
    if st.session_state.quiz_submitted:
        st.subheader("📈 Quiz Results")

        score = 0

        for i, question in enumerate(questions):
            if st.session_state.quiz_responses.get(i) == question["correct_answer"]:
                score += 1
                st.success(f"✅ Question {i + 1}: Correct")
            else:
                st.error(f"❌ Question {i + 1}: Incorrect")
                st.write(f"Correct answer: {question['correct_answer']}")

                explanation = question.get(
                    "explanation",
                    "Review the explanation, flashcards, and key points for this topic to strengthen your understanding."
                )
                st.write(f"Explanation: {explanation}")

        percentage = (score / len(questions)) * 100

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Your Score", f"{score}/{len(questions)}")

        with col2:
            st.metric("Percentage", f"{percentage:.1f}%")

        with col3:
            if percentage >= 80:
                st.metric("Grade", "A+")
            elif percentage >= 70:
                st.metric("Grade", "B")
            else:
                st.metric("Grade", "C")

        student_label = get_student_label()

        if percentage >= 80:
            st.balloons()
            st.success(f"🏆 Excellent work, {student_label}! You showed strong understanding of this topic.")
        elif percentage >= 50:
            st.info(f"👍 Good effort, {student_label}. Review the flashcards once more to improve your score.")
        else:
            st.warning(f"💪 Keep practicing, {student_label}. Start with the explanation and key points, then retry the quiz.")

        # Save progress to database only once per generated quiz
        if not st.session_state.quiz_progress_saved:
            save_progress(
                topic=materials["topic"],
                difficulty=materials["difficulty"],
                num_flashcards=len(materials["flashcards"]),
                num_questions=len(questions),
                quiz_score=score,
                total_questions=len(questions)
            )

            st.session_state.quiz_progress_saved = True
            st.success("✅ Progress saved to your history!")
        else:
            st.info("Progress already saved for this quiz attempt.")


def download_study_notes(materials):
    """Generate and offer download of study notes."""
    st.subheader("📥 Download Study Notes")

    source_type = materials.get("source_type", "Typed Topic")
    file_name = materials.get("file_name", "N/A")

    # Format notes as text
    notes = f"""
STUDYMATE AI - STUDY NOTES
==========================

Student: {get_student_label()}
Source Type: {source_type}
File Name: {file_name}
Topic: {materials['topic']}
Difficulty: {materials['difficulty']}
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

EXPLANATION
-----------
{materials['explanation']}

KEY POINTS
----------
"""

    for i, point in enumerate(materials["key_points"], 1):
        notes += f"{i}. {point}\n"

    notes += "\n\nFLASHCARDS\n----------\n"

    for card in materials["flashcards"]:
        notes += f"\nQ{card['id']}: {card['question']}\nA: {card['answer']}\n"

    notes += "\n\nQUIZ QUESTIONS\n--------------\n"

    for q in materials["quiz_questions"]:
        notes += f"\n{q['id']}. {q['question']}\n"
        for opt in q["options"]:
            notes += f"   • {opt}\n"

    safe_topic_name = materials["topic"].replace(" ", "_").replace(":", "").replace("/", "_").replace("\\", "_")

    # Download button
    st.download_button(
        label="⬇️ Download as Text File",
        data=notes,
        file_name=f"studymate_{safe_topic_name}.txt",
        mime="text/plain"
    )


def show_progress_history():
    """Display user's study progress history."""
    student_name = get_student_name()
    progress_title = f"{student_name}'s Study Progress" if student_name else "Your Study Progress"

    st.header(f"📊 {progress_title}")

    # Get summary statistics
    summary = get_progress_summary()

    # Display metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Study Sessions", summary["total_sessions"])

    with col2:
        st.metric("Average Score", f"{summary['average_score']:.1f}%")

    with col3:
        st.metric("Unique Topics", summary["unique_topics"])

    # Get history
    history = get_progress_history()

    if history:
        st.subheader("Recent Study Sessions")

        # Convert to list of dicts for better table display
        data = []

        for record in history:
            data.append({
                "Topic": record[0],
                "Difficulty": record[1],
                "Flashcards": record[2],
                "Questions": record[3],
                "Score": f"{record[4]}/{record[5]}",
                "Percentage": f"{record[6]:.1f}%",
                "Date": record[7]
            })

        st.dataframe(data, use_container_width=True)
    else:
        st.info("📚 No study sessions yet. Start studying to build your progress history!")


def main():
    """Main application."""
    # Sidebar
    with st.sidebar:
        st.title("🎓 StudyMate AI")
        st.divider()

        st.markdown("### 👤 Student Profile")
        st.text_input(
            "Enter your name",
            placeholder="e.g., Pedro",
            key="student_name"
        )

        student_name = get_student_name()

        if student_name:
            st.caption(f"Studying as **{student_name}**")
        else:
            st.caption("Add your name to personalize the app.")

        st.divider()

        page = st.radio(
            "Navigation",
            ["Study", "Progress History"],
            label_visibility="collapsed"
        )

        st.divider()

        st.markdown("""
        ### About StudyMate AI
        Your AI-powered study buddy for:
        - 📖 Clear explanations
        - 🎴 Flashcard learning
        - 🧪 Quiz practice
        - 📊 Progress tracking

        **No API keys required!** Everything works offline.

        ---
        *Open-source project for better learning*
        """)

    # Main content
    if page == "Study":
        st.title("📚 StudyMate AI")
        st.markdown("""
        ### *AI-powered study assistant for notes, flashcards, quizzes, and progress tracking*
        """)

        student_name = get_student_name()

        if student_name:
            st.success(f"👋 Welcome back, {student_name}! Ready to study smarter today?")
        else:
            st.info("👋 Enter your name in the sidebar to personalize your study session.")

        st.divider()

        # Study Interface
        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("🎯 What would you like to study?")

            # Topic input with suggestions
            col_input, col_suggest = st.columns([3, 1])

            with col_input:
                st.text_input(
                    "Enter a topic",
                    value=st.session_state.get("topic_input", ""),
                    placeholder="e.g., Photosynthesis, Python Programming...",
                    label_visibility="collapsed",
                    key="topic_input"
                )

            with col_suggest:
                st.button("💡 Suggest", on_click=suggest_random_topic)

            # Show info message if topic was selected
            if st.session_state.get("topic_input"):
                st.info(f"📌 Using topic: **{st.session_state.topic_input}**")

            st.markdown("### 📄 Or upload your own study material")
            uploaded_file = st.file_uploader(
                "Upload a .txt or .md file with your notes",
                type=["txt", "md"],
                help="Upload your own notes and StudyMate AI will generate explanation, flashcards, quiz questions, and downloadable notes from it."
            )

            uploaded_data = None

            if uploaded_file is not None:
                uploaded_data, upload_error = read_uploaded_text_file(uploaded_file)

                if upload_error:
                    st.error(upload_error)
                else:
                    st.success(f"✅ Uploaded file detected: **{uploaded_data['file_name']}**")
                    st.caption("Uploaded file mode will be used when you click Generate Study Materials.")

        with col2:
            st.subheader("📋 Sample Topics")

            sample_topics = load_sample_topics()

            for topic in sample_topics[:5]:
                st.button(
                    topic,
                    key=f"sample_{topic}",
                    use_container_width=True,
                    on_click=set_topic,
                    args=(topic,)
                )

        st.divider()

        # Study parameters
        col1, col2, col3 = st.columns(3)

        with col1:
            difficulty = st.selectbox(
                "Select Difficulty Level",
                ["Beginner", "Intermediate", "Advanced"],
                index=0
            )

        with col2:
            num_flashcards = st.slider(
                "Number of Flashcards",
                min_value=1,
                max_value=20,
                value=5
            )

        with col3:
            num_questions = st.slider(
                "Number of Quiz Questions",
                min_value=1,
                max_value=10,
                value=5
            )

        # Generate button
        if st.button("✨ Generate Study Materials", type="primary", use_container_width=True):
            # Get topic from session state
            user_topic = st.session_state.get("topic_input", "")

            # Check if user uploaded a file
            uploaded_data = None
            upload_error = None

            if "uploaded_file" in locals() and uploaded_file is not None:
                uploaded_data, upload_error = read_uploaded_text_file(uploaded_file)

            if upload_error:
                st.error(upload_error)

            elif uploaded_data:
                # Validate parameters only; typed topic is optional when a file is uploaded
                fc_valid, fc_error = validate_num_flashcards(num_flashcards)
                q_valid, q_error = validate_num_questions(num_questions)

                if not fc_valid:
                    st.error(fc_error)
                elif not q_valid:
                    st.error(q_error)
                else:
                    # Generate materials from uploaded file
                    with st.spinner(f"🔄 Generating study materials from '{uploaded_data['file_name']}'..."):
                        materials = generate_materials_from_uploaded_file(
                            file_name=uploaded_data["file_name"],
                            file_text=uploaded_data["text"],
                            difficulty=difficulty,
                            num_flashcards=num_flashcards,
                            num_questions=num_questions
                        )

                        st.session_state.materials = materials
                        st.session_state.show_materials = True

                        # Reset quiz state for fresh quiz
                        st.session_state.quiz_responses = {}
                        st.session_state.quiz_submitted = False
                        st.session_state.quiz_progress_saved = False
                        st.session_state.quiz_run_id = st.session_state.get("quiz_run_id", 0) + 1

                        # Reset flashcard state for fresh flashcards
                        st.session_state.current_card = 0
                        st.session_state.flipped = [False] * len(materials["flashcards"])

                        st.rerun()

            else:
                # Validate typed topic input
                is_valid, error_msg = validate_topic(user_topic)

                if not is_valid:
                    st.error(error_msg)
                else:
                    # Validate parameters
                    fc_valid, fc_error = validate_num_flashcards(num_flashcards)
                    q_valid, q_error = validate_num_questions(num_questions)

                    if not fc_valid:
                        st.error(fc_error)
                    elif not q_valid:
                        st.error(q_error)
                    else:
                        # Generate materials from typed topic
                        with st.spinner(f"🔄 Generating study materials for '{user_topic}'..."):
                            materials = StudyMaterialGenerator.generate_all_materials(
                                topic=user_topic,
                                difficulty=difficulty,
                                num_flashcards=num_flashcards,
                                num_questions=num_questions
                            )

                            st.session_state.materials = materials
                            st.session_state.show_materials = True

                            # Reset quiz state for fresh quiz
                            st.session_state.quiz_responses = {}
                            st.session_state.quiz_submitted = False
                            st.session_state.quiz_progress_saved = False

                            # Reset flashcard state for fresh flashcards
                            st.session_state.current_card = 0
                            st.session_state.flipped = [False] * len(materials["flashcards"])

                            st.rerun()

        # Display generated materials if available
        if st.session_state.get("show_materials") and st.session_state.get("materials"):
            materials = st.session_state.materials

            source_type = materials.get("source_type", "Typed Topic")
            file_name = materials.get("file_name", "")

            if source_type == "Uploaded File":
                st.success(f"✅ Study materials generated from uploaded file: **{file_name}** ({materials['difficulty'].upper()})")
            else:
                st.success(f"✅ Study materials generated for **{materials['topic']}** ({materials['difficulty'].upper()})")

            st.divider()

            # Tab interface for different content types
            tab1, tab2, tab3, tab4 = st.tabs(
                ["📖 Explanation", "🎴 Flashcards", "🧪 Quiz", "📥 Download"]
            )

            with tab1:
                render_explanation(materials)

            with tab2:
                render_flashcards(materials)

            with tab3:
                render_quiz(materials)

            with tab4:
                download_study_notes(materials)

    else:
        show_progress_history()


if __name__ == "__main__":
    # Initialize session state variables
    if "show_materials" not in st.session_state:
        st.session_state.show_materials = False

    if "materials" not in st.session_state:
        st.session_state.materials = None

    if "topic_input" not in st.session_state:
        st.session_state.topic_input = ""

    if "selected_sample_topic" not in st.session_state:
        st.session_state.selected_sample_topic = ""

    if "student_name" not in st.session_state:
        st.session_state.student_name = ""

    if "quiz_progress_saved" not in st.session_state:
        st.session_state.quiz_progress_saved = False
    
    if "quiz_run_id" not in st.session_state:
        st.session_state.quiz_run_id = 0

    main()