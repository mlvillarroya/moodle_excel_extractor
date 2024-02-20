import misc.Constants as CS
from MoodleObjects.Arrays import NumericArray


def create_questions():
    mc1_data = {
        CS.NUMERIC_QUESTION_TITLE: 'Question',
        CS.NUMERIC_CORRECT_VALUE_TITLE: 100,
        CS.NUMERIC_TOLERANCE_TITLE: 0.1,
        CS.NUMERIC_FEEDBACK_TITLE: 'Feedback',
        CS.NUMERIC_SUBCATEGORY_TITLE: 'Subcategory'
    }
    mc2_data = {
        CS.NUMERIC_QUESTION_TITLE: 'Question',
        CS.NUMERIC_CORRECT_VALUE_TITLE: 100,
        CS.NUMERIC_TOLERANCE_TITLE: 0.1,
        CS.NUMERIC_FEEDBACK_TITLE: 'Feedback',
        CS.NUMERIC_SUBCATEGORY_TITLE: 'Subcategory'
    }
    return [mc1_data,mc2_data]


def test_mc_question_array_creation_ok():
    """Testing base array constructor"""
    questions_generated = NumericArray(create_questions(),'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[0].answer == '#100:0.1'
    assert questions_generated.question_array[0].category == 'main_category/Subcategory'
    assert questions_generated.question_array[0].question == 'Question'
    assert questions_generated.question_array[0].feedback == '####Feedback\n'
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::N1::Question{\n#100:0.1\n####Feedback\n}\n'
    assert questions_generated.print_all_questions() == \
                questions_generated.question_array[0].print_question() +\
                "\n" +\
                questions_generated.question_array[1].print_question() +\
                "\n"

def test_mc_questions_question_with_no_title_not_created():
    """Test errors when a question has no title"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.NUMERIC_QUESTION_TITLE] = None
    questions_generated = NumericArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_mc_questions_question_with_no_value_not_created():
    """Test errors when a question has no first answer -> answer not created"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.NUMERIC_CORRECT_VALUE_TITLE] = None
    questions_generated = NumericArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_mc_questions_question_with_no_tolerance_created_ok():
    """Test errors when a question has no second answer -> answer not created"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.NUMERIC_TOLERANCE_TITLE] = None
    questions_generated = NumericArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::N1::Question{\n#100:0\n####Feedback\n}\n'

def test_mc_questions_question_with_no_feedback_created_ok():
    """Test when a question has no feedback -> answer created"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.NUMERIC_FEEDBACK_TITLE] = None
    questions_generated = NumericArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::N1::Question{\n#100:0.1\n}\n'

def test_mc_questions_question_with_no_category_created_ok():
    """Test when a question has no category -> answer created"""
    questions_with_errors = create_questions()
    questions_generated = NumericArray(questions_with_errors)
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: Category/Subcategory\n\n::N1::Question{\n#100:0.1\n####Feedback\n}\n'

def test_mc_questions_question_with_no_subcategory_created_ok():
    """Test when a question has no subcategory -> answer created"""
    questions_with_errors = create_questions()
    questions_with_errors[1][CS.NUMERIC_SUBCATEGORY_TITLE] = None
    questions_generated = NumericArray(questions_with_errors,'main category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main category\n\n::N1::Question{\n#100:0.1\n####Feedback\n}\n'
