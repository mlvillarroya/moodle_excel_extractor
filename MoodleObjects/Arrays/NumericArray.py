import json

from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import Numeric
import misc.Constants as CS
from misc import ProjectPaths
from .Base.BaseArray import BaseArray

with open(ProjectPaths.get_constants_path(), "r", encoding="utf8") as file:
    CONSTANTS = json.load(file)
ARRAY_NAME = 'numeric_sheet'


class NumericArray(BaseArray):
    """Class for numeric questions array"""
    def __init__(self, dictionary_array, main_category='Category'):
        super().__init__(dictionary_array, main_category, ARRAY_NAME, CONSTANTS)

    def _extract_category(self,question, main_category):
        return main_category + '/' + \
            question[CS.NUMERIC_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] \
            else main_category

    def _extract_answer_list(self, question):
        if question[CS.NUMERIC_TOLERANCE_TITLE] is None: 
            question[CS.NUMERIC_TOLERANCE_TITLE] = 0
        return [Answer(question[CS.NUMERIC_CORRECT_VALUE_TITLE],
                       numeric_tolerance = question[CS.NUMERIC_TOLERANCE_TITLE])]

    def _extract_question(self,category,question,answers):
        return Numeric(category,\
                        'N' + str(self.successful_answers),\
                        question[CS.NUMERIC_QUESTION_TITLE],\
                        answers,\
                        question[CS.NUMERIC_FEEDBACK_TITLE])
