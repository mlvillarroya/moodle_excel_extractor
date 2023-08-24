"""Numeric questions. Inherits from Question"""
import misc.Constants as CS
from .Base.Question import Question

class Numeric(Question):
    """Class Numeric inherits from Question"""
    def __init__(self,category,code,question,answers_list,general_feedback):
        super().__init__(category,code,question,answers_list,general_feedback)
        try:
            float(answers_list[0].answer)
        except ValueError as e:
            raise ValueError(CS.EXCEPTION_ANSWER_MUST_BE_FLOAT) from e

    def create_answer_from_list(self):
        """Function to create custom text for numeric questions"""
        if self.answers_list[0].numeric_tolerance is None:
            self.answers_list[0].numeric_tolerance = 0
        return '#' + str(self.answers_list[0].answer) + \
                ':' + str(self.answers_list[0].numeric_tolerance)
    