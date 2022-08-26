from MoodleQuestions.Question import Question

class MultipleChoice(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        self.completeAnswer = ''
        for index,answer in enumerate(answersList):
            value = "%" + answer.value + "%" if answer.value != '' else ''
            answerValue = "=" if index == 0 else "~" + value
            feedback = "#" + answer.feedback if answer.feedback != '' else ''
            nextLine = "\n" if index < len(answersList) - 1 else ''
            self.completeAnswer = self.completeAnswer + answerValue + answer.answer + feedback + nextLine

        self.feedback = "####" + generalFeedback if generalFeedback != '' else ''

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.completeAnswer + "\n" \
                + self.feedback + "\n" \
                + "}"