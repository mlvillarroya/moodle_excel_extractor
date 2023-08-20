
class QuestionsArray:
    def __init__(self,questionsArray=[],successfullAnswers=0,failedAnswers=0):
        self.questionsArray = questionsArray
        self.successfullAnswers = successfullAnswers
        self.failedAnswers = failedAnswers

    def ExtractCategory(self,question, mainCategory):
        pass
    def ExtractAnswerList(self, question):
        pass
    def CreateQuestion(self,category,question,answer):
        pass
    def createQuestionsArrayFromDictionaryArray(self,dictionaryArray,mainCategory):
        for question in dictionaryArray:
            try:
                category = self.ExtractCategory(question, mainCategory)
                answer = self.ExtractAnswerList(question)
                question=self.CreateQuestion(category,question,answer)
                self.questionsArray.append(question)
            except: self.failedAnswers +=1
            else: self.successfullAnswers+=1
