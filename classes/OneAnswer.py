from classes.Question import Question

class OneAnswer(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        self.completeAnswer = ''
        for index,answer in enumerate(answersList):
            nextLine = "\n" if index < len(answersList) - 1 else ''
            self.completeAnswer = self.completeAnswer + "=%100%" + answer.answer + nextLine

        self.feedback = "####" + generalFeedback if generalFeedback != '' else ''

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.completeAnswer + "\n" \
                + self.feedback + "\n" \
                + "}"