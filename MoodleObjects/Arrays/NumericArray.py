from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import Numeric
import misc.Constants as CS
from .Base.BaseArray import BaseArray

class NumericArray(BaseArray):
    """Class for numeric questions array"""

    def extract_category(self,question, main_category):
        return main_category + '/' + \
            question[CS.NUMERIC_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] \
            else main_category

    def extract_answer_list(self, question):
        if question[CS.NUMERIC_TOLERANCE_TITLE] is None: 
            question[CS.NUMERIC_TOLERANCE_TITLE] = 0
        return [Answer(question[CS.NUMERIC_CORRECT_VALUE_TITLE],
                       numeric_tolerance = question[CS.NUMERIC_TOLERANCE_TITLE])]

    def extract_question(self,category,question,answers):
        return Numeric(category,\
                        'N' + str(self.successfull_answers),\
                        question[CS.NUMERIC_QUESTION_TITLE],\
                        answers,\
                        question[CS.NUMERIC_FEEDBACK_TITLE])
