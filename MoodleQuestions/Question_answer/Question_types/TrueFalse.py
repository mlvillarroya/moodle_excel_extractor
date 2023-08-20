from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.Question import Question

class TrueFalse(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
  
    def create_answer_from_list(self):
        if self.__answers_list[0].answer != 'True' or \
            self.__answers_list[0].answer != 'T' or \
            self.__answers_list[0].answer != 'true' or \
            self.__answers_list[0].answer != 't':
                return 'T'
        else: return 'F'