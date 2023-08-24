"""Tests to question class"""
import pytest
import misc.Constants as CS
from MoodleObjects.Questions import Question, MultipleChoice, Numeric, OneAnswer, TrueFalse
from MoodleObjects.Answers import Answer

ANSWER1 = Answer('Answer text1','Feedback1',100,0)
ANSWER2 = Answer('Answer text2','Feedback2',30,0)
ANSWER3 = Answer('Answer text3','Feedback3',0,0)
NUMERIC_ANSWER = Answer(17,'Feedback',0,0.1)
TRUE_ANSWER = Answer('True','Feedback')
FALSE_ANSWER = Answer('False','Feedback')

QUESTION_CATEGORY = 'Question category'
QUESTION_CODE = 'Question code'
QUESTION_TEXT = 'Question_text'
ANSWER_LIST = [ANSWER1,ANSWER2,ANSWER3]
GENERAL_FEEDBACK = 'General feedback'

QUESTION_BASE_CORRECT_ANSWER = ''
BASE_QUESTION_TEXT = "::Question code::Question_text{\n\n####General feedback\n}"
BASE_QUESTION_PRINTED_QUESTION = \
    "$CATEGORY: Question category\n\n::Question code::Question_text{\n\n####General feedback\n}\n"

MULTIPLE_CHOICE_QUESTION_CORRECT_ANSWER = \
    '=Answer text1#Feedback1\n~%30%Answer text2#Feedback2\n~%0%Answer text3#Feedback3'

NUMERIC_QUESTION_CORRECT_ANSWER = '#17:0.1'

ONE_ANSWER_QUESTION_CORRECT_ANSWER = '=%100%Answer text1\n=%100%Answer text2\n=%100%Answer text3'

TRUE_FALSE_TRUE_CORRECT_ANSWER = 'T'
TRUE_FALSE_FALSE_CORRECT_ANSWER = 'F'

def test_base_question_create_question_ok():
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
    assert base_question.answer == ""

def test_base_question_create_question_category_none_gets_empty():
    """Test object standard generation with errors"""
    base_question = Question(
        None,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert base_question.category == ''

def test_base_question_create_question_code_none_gets_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            None,
            QUESTION_TEXT,
            ANSWER_LIST,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_NONE_ARGUMENT

def test_base_question_create_question_question_none_gets_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            None,
            ANSWER_LIST,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_NONE_ARGUMENT

def test_base_question_create_question_answer_none_gets_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            QUESTION_TEXT,
            None,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_NONE_ARGUMENT

def test_base_question_create_question_answer_list_str_get_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            QUESTION_TEXT,
            ['Answer1','Answer2','Answer3'],
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_LIST_ANSWERS_NEEDED

def test_base_question_create_question_answer_not_list_get_exception():
    """Test object standard generation"""
    with pytest.raises(ValueError) as exc_info:
        Question(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            QUESTION_TEXT,
            ANSWER1,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_LIST_ANSWERS_NEEDED

def test_base_question_create_question_feedback_none_gets_empty():
    """Test object standard generation with errors"""
    base_question = Question(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        None)
    assert base_question.general_feedback is None
    assert base_question.feedback == QUESTION_BASE_CORRECT_ANSWER

def test_base_question_create_question_text_ok():
    """Test function create question text"""
    base_question = Question(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert base_question.create_question_text() == BASE_QUESTION_TEXT

def test_base_question_print_question_ok():
    """Test function print question"""
    base_question = Question(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert base_question.print_question() == BASE_QUESTION_PRINTED_QUESTION

def test_multiple_choice_question_create_question_ok():
    """Test object standard generation"""
    multiple_choice_question = MultipleChoice(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert multiple_choice_question.category == QUESTION_CATEGORY
    assert multiple_choice_question.code == QUESTION_CODE
    assert multiple_choice_question.question == QUESTION_TEXT
    assert multiple_choice_question.answers_list == ANSWER_LIST
    assert multiple_choice_question.general_feedback == GENERAL_FEEDBACK
    assert multiple_choice_question.feedback == '####General feedback\n'
    assert multiple_choice_question.answer == MULTIPLE_CHOICE_QUESTION_CORRECT_ANSWER

def test_multiple_choice_question_only_one_answer_get_exception():
    """Test object standard generation with only one answer"""
    with pytest.raises(ValueError) as exc_info:
        MultipleChoice(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            QUESTION_TEXT,
            [ANSWER1],
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_AT_LEAST_TWO_ANSWERS

def test_numeric_question_create_question_ok():
    """Test object standard generation"""
    numeric_question = Numeric(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        [NUMERIC_ANSWER],
        GENERAL_FEEDBACK)
    assert numeric_question.category == QUESTION_CATEGORY
    assert numeric_question.code == QUESTION_CODE
    assert numeric_question.question == QUESTION_TEXT
    assert numeric_question.answers_list == [NUMERIC_ANSWER]
    assert numeric_question.general_feedback == GENERAL_FEEDBACK
    assert numeric_question.feedback == '####General feedback\n'
    assert numeric_question.answer == NUMERIC_QUESTION_CORRECT_ANSWER

def test_numeric_question_no_numeric_answer_get_exception():
    """Test object standard generation with no numeric answer"""
    with pytest.raises(ValueError) as exc_info:
        Numeric(
            QUESTION_CATEGORY,
            QUESTION_CODE,
            QUESTION_TEXT,
            ANSWER_LIST,
            GENERAL_FEEDBACK)
    assert str(exc_info.value) == CS.EXCEPTION_ANSWER_MUST_BE_FLOAT

def test_one_answer_question_create_question_ok():
    """Test object standard generation"""
    numeric_question = OneAnswer(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        ANSWER_LIST,
        GENERAL_FEEDBACK)
    assert numeric_question.category == QUESTION_CATEGORY
    assert numeric_question.code == QUESTION_CODE
    assert numeric_question.question == QUESTION_TEXT
    assert numeric_question.answers_list == ANSWER_LIST
    assert numeric_question.general_feedback == GENERAL_FEEDBACK
    assert numeric_question.feedback == '####General feedback\n'
    assert numeric_question.answer == ONE_ANSWER_QUESTION_CORRECT_ANSWER

def test_true_false_question_create_true_question_ok():
    """Test object standard generation"""
    numeric_question = TrueFalse(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        [TRUE_ANSWER],
        GENERAL_FEEDBACK)
    assert numeric_question.category == QUESTION_CATEGORY
    assert numeric_question.code == QUESTION_CODE
    assert numeric_question.question == QUESTION_TEXT
    assert numeric_question.answers_list == [TRUE_ANSWER]
    assert numeric_question.general_feedback == GENERAL_FEEDBACK
    assert numeric_question.feedback == '####General feedback\n'
    assert numeric_question.answer == TRUE_FALSE_TRUE_CORRECT_ANSWER

def test_true_false_question_create_false_question_ok():
    """Test object standard generation"""
    numeric_question = TrueFalse(
        QUESTION_CATEGORY,
        QUESTION_CODE,
        QUESTION_TEXT,
        [FALSE_ANSWER],
        GENERAL_FEEDBACK)
    assert numeric_question.category == QUESTION_CATEGORY
    assert numeric_question.code == QUESTION_CODE
    assert numeric_question.question == QUESTION_TEXT
    assert numeric_question.answers_list == [FALSE_ANSWER]
    assert numeric_question.general_feedback == GENERAL_FEEDBACK
    assert numeric_question.feedback == '####General feedback\n'
    assert numeric_question.answer == TRUE_FALSE_FALSE_CORRECT_ANSWER
