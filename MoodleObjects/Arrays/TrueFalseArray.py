from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import TrueFalse
import misc.Constants as CS
from .Base.BaseArray import BaseArray

class TrueFalseArray(BaseArray):
    """Class for true-false questions array"""
    def extract_category(self,question, main_category):
        return main_category + '/' + \
            question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] else main_category

    def extract_answer_list(self, question):
        return [Answer(question[CS.TRUE_FALSE_ANSWER_TITLE])]

    def create_question(self,category,question,answers):
        return TrueFalse(category,\
                        'TF'+str(self.successfull_answers),\
                        question[CS.TRUE_FALSE_QUESTION_TITLE],\
                        answers,\
                        question[CS.TRUE_FALSE_FEEDBACK_TITLE])
