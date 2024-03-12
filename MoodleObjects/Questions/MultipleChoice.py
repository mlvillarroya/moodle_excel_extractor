"""Multiple choice questions. Inherits from Question"""
import misc.Constants as CS
import misc.StringFunctions as SF
from .Base.Question import Question

class MultipleChoice(Question):
    """Class MultipleChoice inherits from Question"""
    def __init__(self,category,code,question,answers_list,general_feedback):
        super().__init__(category,code,question,answers_list,general_feedback)
        if len(answers_list) < 2:
            raise ValueError(CS.EXCEPTION_AT_LEAST_TWO_ANSWERS)

    def create_answer_from_list(self):
        """Function to create custom text for multiple choice questions"""
        complete_answer = ''
        for index, answer in enumerate(self.answers_list):
            value = "%" + str(answer.value) + "%" if not SF.string_empty_or_whitespace(answer.value) else ''
            answer_value = "=" if index == 0 else "~" + value
            feedback = "#" + answer.feedback if not SF.string_empty_or_whitespace(answer.feedback) else ''
            next_line = "\n" if index < len(self.answers_list) - 1 else ''
            complete_answer = complete_answer + answer_value + answer.answer + feedback + next_line
        return complete_answer
