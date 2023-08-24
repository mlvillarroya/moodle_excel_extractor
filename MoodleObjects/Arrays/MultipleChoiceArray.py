from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import MultipleChoice
import misc.Constants as CS
from .Base.BaseArray import BaseArray

class MultipleChoiceArray(BaseArray):
    """Class for multiplechoice questions array"""

    def _extract_category(self, question, main_category):
        """Function to extract category"""
        return main_category + '/' + \
            question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] if question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] else main_category

    def _extract_answer_list(self, question: dict):
        """Function to extract answer list"""
        answers = []
        if not CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE in question.keys():
            question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE] = '0'
        for i, answer in enumerate([question[CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE]]):
            if i in (0,1) and answer is None:
                raise ValueError(CS.EXCEPTION_NONE_VALUE)
            elif i == 0:
                created_answer = Answer(answer,value="100")
            elif answer is not None:
                created_answer = Answer(answer,value=question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE])
            else: continue
            answers.append(created_answer)
        return answers

    def _extract_question(self, category, question, answers) -> MultipleChoice:
        return MultipleChoice(category,\
                            'MC'+ str(self.successfull_answers),\
                            question[CS.MULTIPLE_CHOICE_QUESTION_TITLE],\
                            answers,\
                            question[CS.MULTIPLE_CHOICE_FEEDBACK_TITLE])