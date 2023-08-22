from MoodleObjects.Arrays import BaseArray

def test_base_array_init_ok():
    """Testing base array constructor"""
    questions_array = BaseArray()
    assert questions_array.question_array is None
    assert questions_array.successfull_answers == 0
    assert questions_array.failed_answers == 0

    # """Testing base array constructor"""
    # questions_array = BaseArray()
    # assert questions_array.extract_category() == ''