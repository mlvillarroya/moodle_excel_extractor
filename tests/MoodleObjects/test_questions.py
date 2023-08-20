import pytest
from MoodleObjects.Questions import *

QUESTION_CATEGORY = 'Question category'
QUESTION_CODE = 'Question code'
QUESTION_TEXT = 'Question_text'
ANSWER_LIST = ['Answer1','Answer2','Answer3']
GENERAL_FEEDBACK = 'General feedback'

def test_create_base_question_ok():
    """Test object standard generation"""
    base_question = Question(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert base_question.category == QUESTION_CATEGORY
    assert base_question.code == QUESTION_CODE
    assert base_question.question == QUESTION_TEXT
    assert base_question.answers_list == ANSWER_LIST
    assert base_question.general_feedback == GENERAL_FEEDBACK
    assert base_question.feedback == '####General feedback\n'

def test_create_base_question_category_none_gets_empty():
    """Test object standard generation with errors"""
    base_question = Question(
        None,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert base_question.category == ''

def test_create_base_question_code_none_gets_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            None,
            QUESTION_TEXT,
            ANSWER_LIST,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == 'Argument cannot be None'

def test_create_base_question_question_none_gets_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            None,
            ANSWER_LIST,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == 'Argument cannot be None'

def test_create_base_question_answer_none_gets_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            QUESTION_TEXT,
            None,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == 'Argument cannot be None'

def test_create_base_question_feedback_none_gets_empty():
    """Test object standard generation with errors"""
    base_question = Question(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        None)
    assert base_question.general_feedback is None
    assert base_question.feedback == ''
