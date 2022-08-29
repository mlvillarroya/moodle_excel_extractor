

class Question:
    def __init__(self, category, code, question, answersList, generalFeedback):
        if code is None or question is None or answersList is None or answersList[0].value is None:
            raise Exception('Argument cannot be None')
        self.category = category
        self.code = code
        self.question = question
        self.answersList = answersList
        self.generalFeedback = generalFeedback
        self.feedback = "####" + generalFeedback + "\n" if generalFeedback else ''
        self.answer = self.createAnswerFromList()

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.answer + "\n" \
                + self.feedback \
                + "}"

    def createAnswerFromList(self):
        pass

    def printQuestion(self):
        category = "$CATEGORY: " + self.category + "\n" + "\n" if self.category != '' else ''
        return  category \
                + self.createQuestionText() \
                + "\n"