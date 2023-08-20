"""True of false questions. Inherits from Question"""
from .Base.Question import Question

class TrueFalse(Question):
    """Class TrueFalse inherits from Question"""

    def create_answer_from_list(self):
        if self.__answers_list[0].answer != 'True' or \
            self.__answers_list[0].answer != 'T' or \
            self.__answers_list[0].answer != 'true' or \
            self.__answers_list[0].answer != 't':
            return 'T'
        return 'F'
