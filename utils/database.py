"""
SQLite database operations for StudyMate AI
"""

import sqlite3
import json
from datetime import datetime
from pathlib import Path


DATABASE_FILE = "studymate_progress.db"


def init_database():
    """Initialize SQLite database with required tables."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Create progress table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS study_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            num_flashcards INTEGER,
            num_questions INTEGER,
            quiz_score REAL,
            total_questions INTEGER,
            percentage REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            study_date DATE
        )
    """)
    
    conn.commit()
    conn.close()


def save_progress(topic: str, difficulty: str, num_flashcards: int, 
                  num_questions: int, quiz_score: int, total_questions: int):
    """
    Save study session progress to database.
    
    Args:
        topic: Topic studied
        difficulty: Difficulty level
        num_flashcards: Number of flashcards generated
        num_questions: Number of quiz questions
        quiz_score: User's score
        total_questions: Total questions in quiz
    """
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    percentage = (quiz_score / total_questions * 100) if total_questions > 0 else 0
    study_date = datetime.now().date()
    
    cursor.execute("""
        INSERT INTO study_progress 
        (topic, difficulty, num_flashcards, num_questions, quiz_score, total_questions, percentage, study_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (topic, difficulty, num_flashcards, num_questions, quiz_score, total_questions, percentage, study_date))
    
    conn.commit()
    conn.close()


def get_progress_history():
    """
    Fetch all study progress history from database.
    
    Returns:
        List of tuples containing progress records
    """
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT topic, difficulty, num_flashcards, num_questions, 
                   quiz_score, total_questions, percentage, timestamp
            FROM study_progress
            ORDER BY timestamp DESC
            LIMIT 100
        """)
        
        records = cursor.fetchall()
        conn.close()
        return records
    except Exception as e:
        print(f"Error fetching progress: {e}")
        return []


def get_progress_summary():
    """Get summary statistics of study progress."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        
        # Total sessions
        cursor.execute("SELECT COUNT(*) FROM study_progress")
        total_sessions = cursor.fetchone()[0]
        
        # Average score
        cursor.execute("SELECT AVG(percentage) FROM study_progress WHERE percentage IS NOT NULL")
        avg_score = cursor.fetchone()[0] or 0
        
        # Topics studied
        cursor.execute("SELECT COUNT(DISTINCT topic) FROM study_progress")
        unique_topics = cursor.fetchone()[0]
        
        conn.close()
        
        return {
            "total_sessions": total_sessions,
            "average_score": round(avg_score, 2),
            "unique_topics": unique_topics
        }
    except Exception as e:
        print(f"Error getting summary: {e}")
        return {"total_sessions": 0, "average_score": 0, "unique_topics": 0}


def clear_database():
    """Clear all progress data (for testing/reset)."""
    try:
        conn = sqlite3.connect(DATABASE_FILE)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM study_progress")
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"Error clearing database: {e}")
        return False
