from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.Numeric import Numeric
import misc.Constants as CS
from MoodleQuestions.Array.QuestionsArray import QuestionsArray


class NumericArray(QuestionsArray):
    def __init__(self, questionsArray=[], successfullAnswers=0, failedAnswers=0):
        super().__init__(questionsArray, successfullAnswers, failedAnswers)
 
    def ExtractCategory(self,question, mainCategory):
        return mainCategory + '/' + question[CS.NUMERIC_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] else mainCategory
    def ExtractAnswerList(self, question):
        if question[CS.NUMERIC_TOLERANCE_TITLE] is None: question[CS.NUMERIC_TOLERANCE_TITLE] = 0
        return [Answer(question[CS.NUMERIC_CORRECT_VALUE_TITLE],numericTolerance=question[CS.NUMERIC_TOLERANCE_TITLE])]
    def CreateQuestion(self,category,question,answer):
        return Numeric(category,\
                        'N'+str(self.successfullAnswers),\
                        question[CS.NUMERIC_QUESTION_TITLE],\
                        answer,\
                        question[CS.NUMERIC_FEEDBACK_TITLE])