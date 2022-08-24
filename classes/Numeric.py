from classes.Question import Question

class Numeric(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        self.answer = answersList[0]
        self.feedback = "####" + generalFeedback if generalFeedback != '' else ''

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + "#=%100%" + self.answer.answer + ":" + self.answer.numericTolerance + "\n" \
                + self.feedback + "\n" \
                + "}"