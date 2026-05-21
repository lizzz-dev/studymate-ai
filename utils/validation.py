"""
Input validation utilities for StudyMate AI
"""

def validate_topic(topic: str) -> tuple[bool, str]:
    """
    Validate topic input.
    
    Args:
        topic: User-entered topic
        
    Returns:
        Tuple of (is_valid, error_message)
    """
    if not topic or not topic.strip():
        return False, "❌ Please enter a topic to get started!"
    
    if len(topic.strip()) < 2:
        return False, "❌ Topic must be at least 2 characters long."
    
    if len(topic.strip()) > 200:
        return False, "❌ Topic must be less than 200 characters."
    
    # Check for special characters that might cause issues
    invalid_chars = ['<', '>', '"', "'", '|', '&']
    if any(char in topic for char in invalid_chars):
        return False, "❌ Topic contains invalid characters. Please remove special characters."
    
    return True, ""


def validate_num_flashcards(num: int) -> tuple[bool, str]:
    """Validate flashcard count."""
    if num < 1:
        return False, "❌ Minimum 1 flashcard required."
    if num > 20:
        return False, "❌ Maximum 20 flashcards allowed."
    return True, ""


def validate_num_questions(num: int) -> tuple[bool, str]:
    """Validate quiz question count."""
    if num < 1:
        return False, "❌ Minimum 1 question required."
    if num > 10:
        return False, "❌ Maximum 10 questions allowed."
    return True, ""
