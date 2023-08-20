from MoodleQuestions.Base.Question import Question

class OneAnswer(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        
    def create_answer_from_list(self):
        completeAnswer = ''
        for index,answer in enumerate(self.__answers_list):
            nextLine = "\n" if index < len(self.__answers_list) - 1 else ''
            completeAnswer = completeAnswer + "=%100%" + answer.answer + nextLine
        return completeAnswer

