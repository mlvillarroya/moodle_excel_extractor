from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.Question import Question
import misc.Constants as CS

class MultipleChoice(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        if len(answersList) < 2 or answersList[1].value is None:
            raise Exception('Argument cannot be None')
        Question.__init__(self,category,code,question,answersList,generalFeedback)

    def createAnswerFromList(self):
        completeAnswer = ''
        for index,answer in enumerate(self.answersList):
            value = "%" + answer.value + "%" if answer.value != '' else ''
            answerValue = "=" if index == 0 else "~" + value
            feedback = "#" + answer.feedback if answer.feedback != '' else ''
            nextLine = "\n" if index < len(self.answersList) - 1 else ''
            completeAnswer = completeAnswer + answerValue + answer.answer + feedback + nextLine
        return completeAnswer