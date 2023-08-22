from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.TrueFalse import TrueFalse
import misc.Constants as CS
from MoodleQuestions.Array.QuestionsArray import QuestionsArray


class TrueFalseArray(QuestionsArray):
    def __init__(self, questionsArray=[], successfullAnswers=0, failedAnswers=0):
        super().__init__(questionsArray, successfullAnswers, failedAnswers)
 
    def ExtractCategory(self,question, mainCategory):
        return mainCategory + '/' + question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] else mainCategory
    def ExtractAnswerList(self, question):
        return [Answer(question[CS.TRUE_FALSE_ANSWER_TITLE])]
    def CreateQuestion(self,category,question,answer):
        return TrueFalse(category,\
                        'TF'+str(self.successfullAnswers),\
                        question[CS.TRUE_FALSE_QUESTION_TITLE],\
                        answer,\
                        question[CS.TRUE_FALSE_FEEDBACK_TITLE])