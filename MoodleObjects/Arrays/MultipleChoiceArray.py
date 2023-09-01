import json
from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import MultipleChoice
import misc.Constants as CS
from .Base.BaseArray import BaseArray

with open("static/excel_creation_constants.json", "r", encoding="utf8") as file:
    constants = json.load(file)
    mc_titles = {key:constants["multiple_choice_sheet"]["cell_titles"][key][1] for key in constants["multiple_choice_sheet"]["cell_titles"].keys()}

class MultipleChoiceArray(BaseArray):
    """Class for multiple choice questions array"""

    def _extract_category(self, question, main_category):
        """Function to extract category"""
        subcategory = question[mc_titles["subcategory_title"]] or None
        return main_category + '/' + subcategory if subcategory else main_category

    def _extract_answer_list(self, question: dict):
        """Function to extract answer list"""
        answers = []
        if not mc_titles["bad_answer_points_title"] in question.keys():
            question[mc_titles["bad_answer_points_title"]] = '0'
        for i, answer in enumerate([question[mc_titles["correct_answer_title"]],\
                                    question[mc_titles["incorrect_answer_1_title"]],\
                                    question[mc_titles["incorrect_answer_2_title"]],\
                                    question[mc_titles["incorrect_answer_3_title"]],\
                                    question[mc_titles["incorrect_answer_4_title"]]
                                    ]):
            if i in (0,1) and answer is None:
                raise ValueError(CS.EXCEPTION_NONE_VALUE)
            elif i == 0:
                created_answer = Answer(answer,value="100")
            elif answer is not None:
                created_answer = Answer(answer,value=question[mc_titles["bad_answer_points_title"]])
            else: continue
            answers.append(created_answer)
        return answers

    def _extract_question(self, category, question, answers) -> MultipleChoice:
        return MultipleChoice(category,\
                            'MC'+ str(self.successful_answers),\
                            question[mc_titles["question_name_title"]],\
                            answers,\
                            question[mc_titles["feedback_title"]])