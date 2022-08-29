from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.MultipleChoice import MultipleChoice
from MoodleQuestions.Base.TrueFalse import TrueFalse
import misc.Constants as CS
from MoodleQuestions.Array.QuestionsArray import QuestionsArray


class MultipleChoiceArray(QuestionsArray):
    def __init__(self, questionsArray=[], successfullAnswers=0, failedAnswers=0):
        super().__init__(questionsArray, successfullAnswers, failedAnswers)
 
    def ExtractCategory(self,question, mainCategory):
        return mainCategory + '/' + question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] if question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] else mainCategory
    def ExtractAnswerList(self, question):
        answers = []
        if not question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE]: question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE] = '0'
        for i, answer in enumerate([question[CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE],\
                                    question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE]]):
            if (i==0 or i==1) and answer is None: raise Exception("Value cannot be null")
            elif i==0: createdAnswer = Answer(answer,value="100")
            elif answer != None: createdAnswer = Answer(answer,value=question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE])
            else: continue
            answers.append(createdAnswer)
        return answers

    def CreateQuestion(self,category,question,answer):
        return MultipleChoice(category,\
                            'MC'+str(self.successfullAnswers),\
                            question[CS.MULTIPLE_CHOICE_QUESTION_TITLE],\
                            answer,\
                            question[CS.MULTIPLE_CHOICE_FEEDBACK_TITLE])