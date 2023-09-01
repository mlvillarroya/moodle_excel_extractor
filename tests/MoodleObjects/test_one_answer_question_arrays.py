import misc.Constants as CS
from MoodleObjects.Arrays import OneAnswerArray

mc1_data = {
    CS.ONE_ANSWER_QUESTION_TITLE: 'Question',
    CS.ONE_ANSWER_CORRECT_ANSWER_TITLE: 'Correct answer',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE: 'Alternate1',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE: 'Alternate2',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE: 'Alternate3',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE: 'Alternate4',
    CS.ONE_ANSWER_FEEDBACK_TITLE: 'Feedback',
    CS.ONE_ANSWER_SUBCATEGORY_TITLE: 'Subcategory'
}
mc2_data = {
    CS.ONE_ANSWER_QUESTION_TITLE: 'Question',
    CS.ONE_ANSWER_CORRECT_ANSWER_TITLE: 'Correct answer',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE: 'Alternate1',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE: 'Alternate2',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE: 'Alternate3',
    CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE: 'Alternate4',
    CS.ONE_ANSWER_FEEDBACK_TITLE: 'Feedback',
    CS.ONE_ANSWER_SUBCATEGORY_TITLE: 'Subcategory'
}
ONE_ANSWER_questions = [mc1_data,mc2_data]

def test_one_answer_question_array_creation_ok():
    """Testing base array constructor"""
    questions_generated = OneAnswerArray(ONE_ANSWER_questions,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[0].answer == '=%100%Correct answer\n=%100%Alternate1\n=%100%Alternate2\n=%100%Alternate3\n=%100%Alternate4'
    assert questions_generated.question_array[0].category == 'main_category/Subcategory'
    assert questions_generated.question_array[0].question == 'Question'
    assert questions_generated.question_array[0].feedback == '####Feedback\n'
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::OA1::Question{\n=%100%Correct answer\n=%100%Alternate1\n=%100%Alternate2\n=%100%Alternate3\n=%100%Alternate4\n####Feedback\n}\n'
    assert questions_generated.print_all_questions() == \
                questions_generated.question_array[0].print_question() +\
                "\n" +\
                questions_generated.question_array[1].print_question() +\
                "\n"

def test_one_answer_questions_question_with_no_title_not_created():
    """Test errors when a question has no title"""
    questions_with_errors = ONE_ANSWER_questions
    questions_with_errors[1][CS.ONE_ANSWER_QUESTION_TITLE] = None
    questions_generated = OneAnswerArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 1
    assert questions_generated.failed_answers == 1

def test_one_answer_questions_question_with_no_alternate_answers_created_ok():
    """Test errors when a question has no second answer -> answer not created"""
    questions_with_errors = ONE_ANSWER_questions
    questions_with_errors[1][CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE] = None
    questions_with_errors[1][CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE] = None
    questions_with_errors[1][CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE] = None
    questions_with_errors[1][CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE] = None
    questions_generated = OneAnswerArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::OA1::Question{\n=%100%Correct answer\n####Feedback\n}\n'

def test_one_answer_questions_question_with_no_feedback_created_ok():
    """Test when a question has no feedback -> answer created"""
    questions_with_errors = ONE_ANSWER_questions
    questions_with_errors[1][CS.ONE_ANSWER_FEEDBACK_TITLE] = None
    questions_generated = OneAnswerArray(questions_with_errors,'main_category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main_category/Subcategory\n\n::OA1::Question{\n=%100%Correct answer\n=%100%Alternate1\n=%100%Alternate2\n=%100%Alternate3\n=%100%Alternate4\n}\n'

def test_one_answer_questions_question_with_no_category_created_ok():
    """Test when a question has no category -> answer created"""
    questions_with_errors = ONE_ANSWER_questions
    questions_generated = OneAnswerArray(questions_with_errors)
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: Category/Subcategory\n\n::OA1::Question{\n=%100%Correct answer\n=%100%Alternate1\n=%100%Alternate2\n=%100%Alternate3\n=%100%Alternate4\n####Feedback\n}\n'

def test_one_answer_questions_question_with_no_subcategory_created_ok():
    """Test when a question has no subcategory -> answer created"""
    questions_with_errors = ONE_ANSWER_questions
    questions_with_errors[1][CS.ONE_ANSWER_SUBCATEGORY_TITLE] = None
    questions_generated = OneAnswerArray(questions_with_errors,'main category')
    assert questions_generated.successful_answers == 2
    assert questions_generated.failed_answers == 0
    assert questions_generated.question_array[1].print_question() == '$CATEGORY: main category\n\n::OA1::Question{\n=%100%Correct answer\n=%100%Alternate1\n=%100%Alternate2\n=%100%Alternate3\n=%100%Alternate4\n####Feedback\n}\n'
