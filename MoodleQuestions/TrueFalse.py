from MoodleQuestions.Question import Question

class TrueFalse(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        if answersList[0].answer != 'True' or \
            answersList[0].answer != 'T' or \
            answersList[0].answer != 'true' or \
            answersList[0].answer != 't':
                answersList[0].answer = 'T'
        else: answersList[0].answer = 'F'

        self.feedback = "####" + generalFeedback if generalFeedback != '' else ''
        self.answer = answersList[0].answer

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.answer + "\n" \
                + self.feedback + "\n" \
                + "}"