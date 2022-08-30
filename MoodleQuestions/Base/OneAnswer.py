from MoodleQuestions.Base.Question import Question

class OneAnswer(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        
    def createAnswerFromList(self):
        completeAnswer = ''
        for index,answer in enumerate(self.answersList):
            nextLine = "\n" if index < len(self.answersList) - 1 else ''
            completeAnswer = completeAnswer + "=%100%" + answer.answer + nextLine
        return completeAnswer

