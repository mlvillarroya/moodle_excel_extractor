"""One answer questions. Inherits from Question"""
from MoodleQuestions.Question_answer import Question

class OneAnswer(Question):
    """Class OneAnswer inherits from Question"""
    def __init__(self,category,code,question,answersList,generalFeedback):
        super().__init__(category,code,question,answersList,generalFeedback)

    def create_answer_from_list(self):
        """Function to create custom text for one answer questions"""
        complete_answer = ''
        for index,answer in enumerate(self.__answers_list):
            next_line = "\n" if index < len(self.__answers_list) - 1 else ''
            complete_answer = complete_answer + "=%100%" + answer.answer + next_line
        return complete_answer
