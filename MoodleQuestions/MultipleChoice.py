from MoodleQuestions.Answer import Answer
from MoodleQuestions.Question import Question
import misc.Constants as CS

class MultipleChoice(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        self.completeAnswer = ''
        for index,answer in enumerate(answersList):
            value = "%" + answer.value + "%" if answer.value != '' else ''
            answerValue = "=" if index == 0 else "~" + value
            feedback = "#" + answer.feedback if answer.feedback != '' else ''
            nextLine = "\n" if index < len(answersList) - 1 else ''
            self.completeAnswer = self.completeAnswer + answerValue + answer.answer + feedback + nextLine

        self.feedback = "####" + generalFeedback if generalFeedback != '' else ''

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.completeAnswer + "\n" \
                + self.feedback + "\n" \
                + "}"

    def createAnswersFromArray(answerArray,badAnswersPoints):
        answers = []
        for i, answer in enumerate(answerArray):
            if i==0: createdAnswer = Answer(answer,value="100")
            elif answer != '' and answer != None: createdAnswer = Answer(answer,value=badAnswersPoints)
            else: continue
            answers.append(createdAnswer)
        return answers

    def createQuestionsFromDictionaryArray(dictionaryArray,mainCategory):
        questionsArray = []
        for i,question in enumerate(dictionaryArray):
            answers = MultipleChoice.createAnswersFromArray([question[CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE],\
                                                            question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE],\
                                                            question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE],\
                                                            question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE],\
                                                            question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE]],\
                                                            question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE])
            question=MultipleChoice(mainCategory + question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE],\
                            'MC'+str(i),\
                            question[CS.MULTIPLE_CHOICE_QUESTION_TITLE],\
                            answers,\
                            question[CS.MULTIPLE_CHOICE_FEEDBACK_TITLE])
            questionsArray.append(question)
        return questionsArray