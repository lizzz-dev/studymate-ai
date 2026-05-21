"""
StudyMate AI - AI-Powered Study Assistant
Build understanding with notes, flashcards, quizzes, and progress tracking.

An open-source study companion that helps students learn effectively
using rule-based offline content generation.
"""

import streamlit as st
import json
import random
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
    .main {
        padding: 2rem;
    }

    .stButton>button {
        width: 100%;
        border-radius: 8px;
        font-weight: 600;
    }

    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        margin: 0.5rem 0;
    }

    /* Make clickable Streamlit widgets show hand cursor */
    button,
    .stButton > button,
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
    </style>
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

    # Display questions
    for i, question in enumerate(questions):
        st.write(f"**Question {i + 1}**: {question['question']}")

        response = st.radio(
            label="Select your answer:",
            options=question["options"],
            key=f"q_{i}",
            label_visibility="collapsed"
        )

        st.session_state.quiz_responses[i] = response
        st.write("---")

    # Submit button
    if st.button("📊 Submit Quiz", type="primary"):
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

                # Safe explanation fallback
                explanation = question.get(
                    "explanation",
                    "Review the explanation, flashcards, and key points for this topic to strengthen your understanding."
                )
                st.write(f"Explanation: {explanation}")

        percentage = (score / len(questions)) * 100

        # Display score with color coding
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

    # Format notes as text
    notes = f"""
STUDYMATE AI - STUDY NOTES
==========================

Student: {get_student_label()}
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

    # Download button
    st.download_button(
        label="⬇️ Download as Text File",
        data=notes,
        file_name=f"studymate_{materials['topic'].replace(' ', '_')}.txt",
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

            # Validate input
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
                    # Generate materials
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

    main()