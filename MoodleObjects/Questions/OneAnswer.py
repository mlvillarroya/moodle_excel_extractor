"""One answer questions. Inherits from Question"""
from .Base.Question import Question

class OneAnswer(Question):
    """Class OneAnswer inherits from Question"""

    def create_answer_from_list(self):
        """Function to create custom text for one answer questions"""
        complete_answer = ''
        for index,answer in enumerate(self.answers_list):
            next_line = "\n" if index < len(self.answers_list) - 1 else ''
            complete_answer = complete_answer + "=%100%" + answer.answer + next_line
        return complete_answer
