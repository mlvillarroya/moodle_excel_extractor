"""Numeric questions. Inherits from Question"""
from .Base.Question import Question

class Numeric(Question):
    """Class Numeric inherits from Question"""
    def __init__(self,category,code,question,answersList,generalFeedback):
        try:
            float(answersList[0].answer)
        except ValueError as e:
            raise ValueError("Error. Answer value must be float") from e
        super().__init__(category,code,question,answersList,generalFeedback)

    def create_answer_from_list(self):
        """Function to create custom text for numeric questions"""
        if self.__answers_list[0].numericTolerance is None:
            self.__answers_list[0].numericTolerance = 0
        return '#' + str(self.__answers_list[0].answer) + \
                ':' + str(self.__answers_list[0].numericTolerance)
    