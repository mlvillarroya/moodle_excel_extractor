from MoodleQuestions.Base.Question import Question

class Numeric(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        tryParse = float(answersList[0].answer)
        Question.__init__(self,category,code,question,answersList,generalFeedback)

    def createAnswerFromList(self):
        if self.answersList[0].numericTolerance is None: self.answersList[0].numericTolerance = 0
        return '#' + str(self.answersList[0].answer) + ':' + str(self.answersList[0].numericTolerance)