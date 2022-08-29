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
        Question.__init__(self,category,code,question,answersList,generalFeedback)

    def createQuestionText(self):
        return "::" + self.code + "::" + self.question + "{" + "\n" \
                + self.answer + "\n" \
                + self.feedback \
                + "}"
    
    def createAnswerFromList(self):
        if self.answersList[0].answer != 'True' or \
            self.answersList[0].answer != 'T' or \
            self.answersList[0].answer != 'true' or \
            self.answersList[0].answer != 't':
                return 'T'
        else: return 'F'

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