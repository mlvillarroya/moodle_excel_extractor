from MoodleQuestions.Answer import Answer
from MoodleQuestions.Question import Question
import misc.Constants as CS

class GeneratedTrueFalseQuestions:
    def __init__(self,questionsArray,succesfullAnswers, failedAnswers):
        self.questionsArray = questionsArray
        self.succesfullAnswers = succesfullAnswers
        self.failedAnswers = failedAnswers

class TrueFalse(Question):

    def __init__(self,category,code,question,answersList,generalFeedback):
        if code is None or question is None or answersList is None or len(answersList) < 1 or answersList[0].value is None:
            raise Exception('Argument cannot be None')
        Question.__init__(self,category,code,question,answersList,generalFeedback)
        if answersList[0].answer != 'True' or \
            answersList[0].answer != 'T' or \
            answersList[0].answer != 'true' or \
            answersList[0].answer != 't':
                answersList[0].answer = 'T'
        else: answersList[0].answer = 'F'

        self.feedback = "####" + generalFeedback + "\n" if generalFeedback else ''
        self.answer = answersList[0].answer

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.answer + "\n" \
                + self.feedback \
                + "}"
    
    # def createMultipleChoiceAnswersFromArray(answerArray,badAnswersPoints):
    #     answers = []
    #     if not badAnswersPoints: badAnswersPoints = '0'
    #     for i, answer in enumerate(answerArray):
    #         if (i==0 or i==1) and answer is None: raise Exception("Value cannot be null")
    #         elif i==0: createdAnswer = Answer(answer,value="100")
    #         elif answer != None: createdAnswer = Answer(answer,value=badAnswersPoints)
    #         else: continue
    #         answers.append(createdAnswer)
    #     return answers

    def createTrueFalseQuestionsFromDictionaryArray(dictionaryArray,mainCategory):
        questionsArray = []
        failedAnswers = 0
        successfullAnswers = 0
        for i,question in enumerate(dictionaryArray):
            try:
                category = mainCategory + '/' + question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] if question[CS.TRUE_FALSE_SUBCATEGORY_TITLE] else mainCategory
                answer = [Answer(question[CS.TRUE_FALSE_ANSWER_TITLE])]
                question=TrueFalse(category,\
                                'TF'+str(i),\
                                question[CS.TRUE_FALSE_QUESTION_TITLE],\
                                answer,\
                                question[CS.TRUE_FALSE_FEEDBACK_TITLE])
                questionsArray.append(question)
            except: failedAnswers +=1
            else: successfullAnswers+=1
        return GeneratedTrueFalseQuestions(questionsArray,successfullAnswers,failedAnswers)