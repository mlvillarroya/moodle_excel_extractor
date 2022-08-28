from MoodleQuestions.Answer import Answer
from MoodleQuestions.Question import Question
import misc.Constants as CS

class GeneratedMultipleChoiceQuestions:
    def __init__(self,questionsArray,succesfullAnswers, failedAnswers):
        self.questionsArray = questionsArray
        self.succesfullAnswers = succesfullAnswers
        self.failedAnswers = failedAnswers

class MultipleChoice(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        if code is None or question is None or answersList is None or len(answersList) < 2 or answersList[0].value is None or answersList[1].value is None:
            raise Exception('Argument cannot be None')
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        self.completeAnswer = ''
        for index,answer in enumerate(answersList):
            value = "%" + answer.value + "%" if answer.value != '' else ''
            answerValue = "=" if index == 0 else "~" + value
            feedback = "#" + answer.feedback if answer.feedback != '' else ''
            nextLine = "\n" if index < len(answersList) - 1 else ''
            self.completeAnswer = self.completeAnswer + answerValue + answer.answer + feedback + nextLine

        self.feedback = "####" + generalFeedback + "\n" if generalFeedback else ''

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.completeAnswer + "\n" \
                + self.feedback \
                + "}"

    def createMultipleChoiceAnswersFromArray(answerArray,badAnswersPoints):
        answers = []
        if not badAnswersPoints: badAnswersPoints = '0'
        for i, answer in enumerate(answerArray):
            if (i==0 or i==1) and answer is None: raise Exception("Value cannot be null")
            elif i==0: createdAnswer = Answer(answer,value="100")
            elif answer != None: createdAnswer = Answer(answer,value=badAnswersPoints)
            else: continue
            answers.append(createdAnswer)
        return answers

    def createMultipleChoiceQuestionsFromDictionaryArray(dictionaryArray,mainCategory):
        questionsArray = []
        failedAnswers = 0
        successfullAnswers = 0
        for i,question in enumerate(dictionaryArray):
            try:
                category = mainCategory + question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] if question[CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE] else ''
                answers = MultipleChoice.createMultipleChoiceAnswersFromArray([question[CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE],\
                                                                question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE],\
                                                                question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE],\
                                                                question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE],\
                                                                question[CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE]],\
                                                                question[CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE])
                question=MultipleChoice(category,\
                                'MC'+str(i),\
                                question[CS.MULTIPLE_CHOICE_QUESTION_TITLE],\
                                answers,\
                                question[CS.MULTIPLE_CHOICE_FEEDBACK_TITLE])
                questionsArray.append(question)
            except: failedAnswers +=1
            else: successfullAnswers+=1
        return GeneratedMultipleChoiceQuestions(questionsArray,successfullAnswers,failedAnswers)