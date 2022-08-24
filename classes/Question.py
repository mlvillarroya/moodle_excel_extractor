class Question:
    def __init__(self, category, code, question, answersList, generalFeedback):
        self.category = category
        self.code = code
        self.question = question
        self.answer = answersList
        self.generalFeedback = generalFeedback

    def createQuestionText(self):
        pass

    def printQuestion(self):
        return "$CATEGORY: " + self.category + "\n" \
                + "\n" \
                + self.createQuestionText() \
                + "\n"