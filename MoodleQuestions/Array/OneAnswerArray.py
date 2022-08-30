from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.MultipleChoice import MultipleChoice
from MoodleQuestions.Base.OneAnswer import OneAnswer
import misc.Constants as CS
from MoodleQuestions.Array.QuestionsArray import QuestionsArray


class OneAnswerArray(QuestionsArray):
    def __init__(self, questionsArray=[], successfullAnswers=0, failedAnswers=0):
        super().__init__(questionsArray, successfullAnswers, failedAnswers)
 
    def ExtractCategory(self,question, mainCategory):
        return mainCategory + '/' + question[CS.ONE_ANSWER_SUBCATEGORY_TITLE] if question[CS.ONE_ANSWER_SUBCATEGORY_TITLE] else mainCategory
    def ExtractAnswerList(self, question):
        answers = []
        for i, answer in enumerate([question[CS.ONE_ANSWER_CORRECT_ANSWER_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE],\
                                    question[CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE]]):
            if i==0 and answer is None: raise Exception("Value cannot be null")
            elif answer != None: createdAnswer = Answer(answer,value=100)
            else: continue
            answers.append(createdAnswer)
        return answers

    def CreateQuestion(self,category,question,answer):
        return OneAnswer(category,\
                            'OA'+str(self.successfullAnswers),\
                            question[CS.ONE_ANSWER_QUESTION_TITLE],\
                            answer,\
                            question[CS.ONE_ANSWER_FEEDBACK_TITLE])