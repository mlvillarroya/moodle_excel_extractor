import json

from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import TrueFalse
import misc.Constants as CS
from misc import ProjectPaths
from .Base.BaseArray import BaseArray

with open(ProjectPaths.get_constants_path(), "r", encoding="utf8") as file:
    CONSTANTS = json.load(file)
ARRAY_NAME = 'true_false_sheet'


class TrueFalseArray(BaseArray):
    """Class for true-false questions array"""

    def __init__(self, dictionary_array, main_category='Category'):
        super().__init__(dictionary_array, main_category, ARRAY_NAME, CONSTANTS)

    def _extract_category(self,question, main_category):
        return main_category + '/' + \
            question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] else main_category

    def _extract_answer_list(self, question):
        return [Answer(question[CS.TRUE_FALSE_ANSWER_TITLE])]

    def _extract_question(self,category,question,answers):
        return TrueFalse(category,\
                        'TF'+str(self.successful_answers),\
                        question[CS.TRUE_FALSE_QUESTION_TITLE],\
                        answers,\
                        question[CS.TRUE_FALSE_FEEDBACK_TITLE])
