import misc.Constants as CS
from MoodleObjects import TrueFalseArray

def create_questions():
    mc1_data = {
        CS.TRUE_FALSE_QUESTION_TITLE: 'Question',
        CS.TRUE_FALSE_ANSWER_TITLE: 'True',
        CS.TRUE_FALSE_FEEDBACK_TITLE: 'Feedback',
        CS.TRUE_FALSE_SUBCATEGORY_TITLE: 'Subcategory'
    }
    mc2_data = {
        CS.TRUE_FALSE_QUESTION_TITLE: 'Question',
        CS.TRUE_FALSE_ANSWER_TITLE: 'False',
        CS.TRUE_FALSE_FEEDBACK_TITLE: 'Feedback',
        CS.TRUE_FALSE_SUBCATEGORY_TITLE: 'Subcategory'
    }
    return [mc1_data,mc2_data]

def test_true_false_question_array_creation_ok():
    """Testing base array constructor"""
    questions_generated = TrueFalseArray(create_questions(),'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[0].answer == 'T'
    assert questions_generated.question_array[1].answer == 'F'
    assert questions_generated.question_array[0].category == 'main_category/Subcategory'
    assert questions_generated.question_array[0].question == 'Question'
    assert questions_generated.question_array[0].feedback == '####Feedback\n'
    assert questions_generated.question_array[0].print_question() == '$CATEGORY: main_category/Subcategory\n\n::TF0::Question{\nT\n####Feedback\n}\n'
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::TF1::Question{\nF\n####Feedback\n}\n'
    assert questions_generated.print_all_questions() == \
                questions_generated.question_array[0].print_question() +\
                "\n" +\
                questions_generated.question_array[1].print_question() +\
                "\n"

def test_true_false_questions_question_with_no_title_not_created():
    """Test errors when a question has no title"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.TRUE_FALSE_QUESTION_TITLE] = None
    questions_generated = TrueFalseArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_true_false_questions_question_with_no_feedback_created_ok():
    """Test when a question has no feedback -> answer created"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.TRUE_FALSE_FEEDBACK_TITLE] = None
    questions_generated = TrueFalseArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::TF1::Question{\nF\n}\n'

def test_true_false_questions_question_with_no_category_created_ok():
    """Test when a question has no category -> answer created"""
    questions_with_errors = create_questions()
    questions_generated = TrueFalseArray(questions_with_errors)
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: Category/Subcategory\n\n::TF1::Question{\nF\n####Feedback\n}\n'

def test_true_false_questions_question_with_no_subcategory_created_ok():
    """Test when a question has no subcategory -> answer created"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.TRUE_FALSE_SUBCATEGORY_TITLE] = None
    questions_generated = TrueFalseArray(questions_with_errors,'main category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main category\n\n::TF1::Question{\nF\n####Feedback\n}\n'
