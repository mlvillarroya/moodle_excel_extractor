from MoodleObjects.Answers import Answer
from MoodleObjects.Questions import OneAnswer
import misc.Constants as CS
from .Base.BaseArray import BaseArray

class OneAnswerArray(BaseArray):
    """Class for one answer questions array"""

    def _extract_category(self,question, main_category):
        return main_category + '/' + \
            question[CS.ONE_ANSWER_SUBCATEGORY_TITLE] if question[CS.ONE_ANSWER_SUBCATEGORY_TITLE] \
            else main_category

    def _extract_answer_list(self, question):
        answers = []
        for i, answer in enumerate([question[CS.ONE_ANSWER_CORRECT_ANSWER_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE]]):
            if i==0 and answer is None: 
                raise ValueError(CS.EXCEPTION_NONE_VALUE)
            elif answer is not None:
                created_answer = Answer(answer, value = 100)
            else: continue
            answers.append(created_answer)
        return answers

    def _extract_question(self,category,question,answers):
        return OneAnswer(category,\
                            'OA'+str(self.successful_answers),\
                            question[CS.ONE_ANSWER_QUESTION_TITLE],\
                            answers,\
                            question[CS.ONE_ANSWER_FEEDBACK_TITLE])
