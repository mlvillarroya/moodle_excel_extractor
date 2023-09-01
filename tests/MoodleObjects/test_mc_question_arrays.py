import misc.Constants as CS
from MoodleObjects.Arrays import MultipleChoiceArray

mc1_data = {
    CS.MULTIPLE_CHOICE_QUESTION_TITLE: 'Question',
    CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE: 'Correct answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_FEEDBACK_TITLE: 'Feedback',
    CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE: 'Subcategory',
    CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE: -10
}
mc2_data = {
    CS.MULTIPLE_CHOICE_QUESTION_TITLE: 'Question',
    CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE: 'Correct answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE: 'Incorrect answer',
    CS.MULTIPLE_CHOICE_FEEDBACK_TITLE: 'Feedback',
    CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE: 'Subcategory'
}
multiple_choice_questions = [mc1_data,mc2_data]

def test_mc_question_array_creation_ok():
    """Testing base array constructor"""
    questions_generated = MultipleChoiceArray(multiple_choice_questions,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[0].answer == '=Correct answer\n~%-10%Incorrect answer\n~%-10%Incorrect answer\n~%-10%Incorrect answer\n~%-10%Incorrect answer'
    assert questions_generated.question_array[0].category == 'main_category/Subcategory'
    assert questions_generated.question_array[0].question == 'Question'
    assert questions_generated.question_array[0].feedback == '####Feedback\n'
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::MC1::Question{\n=Correct answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n####Feedback\n}\n'
    assert questions_generated.print_all_questions() == \
                questions_generated.question_array[0].print_question() +\
                "\n" +\
                questions_generated.question_array[1].print_question() +\
                "\n"

def test_mc_questions_question_with_no_title_not_created():
    """Test errors when a question has no title"""
    questions_with_errors = multiple_choice_questions
    questions_with_errors[1][CS.MULTIPLE_CHOICE_QUESTION_TITLE] = None # type: ignore
    questions_generated = MultipleChoiceArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_mc_questions_question_with_no_first_answer_not_created():
    """Test errors when a question has no first answer -> answer not created"""
    questions_with_errors = multiple_choice_questions
    questions_with_errors[1][CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE] = None # type: ignore
    questions_generated = MultipleChoiceArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_mc_questions_question_with_no_second_answer_not_created():
    """Test errors when a question has no second answer -> answer not created"""
    questions_with_errors = multiple_choice_questions
    questions_with_errors[1][CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE] = None # type: ignore
    questions_generated = MultipleChoiceArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_mc_questions_question_with_no_third_answer_created_ok():
    """Test when a question has no third answer -> answer created"""
    questions_with_errors = multiple_choice_questions
    questions_with_errors[1][CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE] = None # type: ignore
    questions_generated = MultipleChoiceArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0

def test_mc_questions_question_with_no_feedback_created_ok():
    """Test when a question has no feedback -> answer created"""
    questions_with_errors = multiple_choice_questions
    questions_with_errors[1][CS.MULTIPLE_CHOICE_FEEDBACK_TITLE] = None # type: ignore
    questions_generated = MultipleChoiceArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::MC1::Question{\n=Correct answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n}\n'

def test_mc_questions_question_with_no_category_created_ok():
    """Test when a question has no category -> answer created"""
    questions_with_errors = multiple_choice_questions
    questions_generated = MultipleChoiceArray(questions_with_errors)
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: Category/Subcategory\n\n::MC1::Question{\n=Correct answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n####Feedback\n}\n'

def test_mc_questions_question_with_no_subcategory_created_ok():
    """Test when a question has no subcategory -> answer created"""
    questions_with_errors = multiple_choice_questions
    questions_with_errors[1][CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] = None # type: ignore
    questions_generated = MultipleChoiceArray(questions_with_errors,'main category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main category\n\n::MC1::Question{\n=Correct answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n~%0%Incorrect answer\n####Feedback\n}\n'
