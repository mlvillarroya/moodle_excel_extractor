import json
from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import MultipleChoice
import misc.Constants as CS
from .Base.BaseArray import BaseArray

with open("static/excel_creation_constants.json", "r", encoding="utf8") as file:
    constants = json.load(file)

class MultipleChoiceArray(BaseArray):
    """Class for multiple choice questions array"""
    
    def __init__(self, dictionary_array, main_category = 'Category'):
        super().__init__(dictionary_array, main_category,'multiple_choice_sheet', constants)

    def _extract_category(self, question, main_category):
        """Function to extract category"""
        subcategory = question[self.titles["subcategory_title"]] or None
        return main_category + '/' + subcategory if subcategory else main_category

    def _extract_answer_list(self, question: dict):
        """Function to extract answer list"""
        answers = []
        if not self.titles["bad_answer_points_title"] in question.keys():
            question[self.titles["bad_answer_points_title"]] = '0'
        for i, answer in enumerate([question[self.titles["correct_answer_title"]],\
                                    question[self.titles["incorrect_answer_1_title"]],\
                                    question[self.titles["incorrect_answer_2_title"]],\
                                    question[self.titles["incorrect_answer_3_title"]],\
                                    question[self.titles["incorrect_answer_4_title"]]
                                    ]):
            if i in (0,1) and answer is None:
                raise ValueError(CS.EXCEPTION_NONE_VALUE)
            elif i == 0:
                created_answer = Answer(answer,value="100")
            elif answer is not None:
                created_answer = Answer(answer,value=question[self.titles["bad_answer_points_title"]])
            else: continue
            answers.append(created_answer)
        return answers

    def _extract_question(self, category, question, answers) -> MultipleChoice:
        return MultipleChoice(category,\
                            'MC'+ str(self.successful_answers),\
                            question[self.titles["question_name_title"]],\
                            answers,\
                            question[self.titles["feedback_title"]])