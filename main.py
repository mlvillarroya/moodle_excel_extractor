from ctypes import alignment
from turtle import color
from MoodleQuestions.MultipleChoice import MultipleChoice
from MoodleQuestions.Numeric import Numeric
from MoodleQuestions.OneAnswer import OneAnswer
from MoodleQuestions.TrueFalse import TrueFalse
from MoodleQuestions.Answer import Answer
from MoodleQuestions.MultipleChoice import MultipleChoice
from misc.ExplorerOpen import ExplorerOpen
import misc.Constants as CS


""" trueFalse = TrueFalse("Test/C1","TF1","Primera pregunta",[Answer("T")],"Bravo, moreno")
printedQuestion = trueFalse.printQuestion()
print(printedQuestion)

multipleChoice = MultipleChoice("Test/C2","MC1","Segunda Pregunta con opciones",[Answer("Respuesta correcta","Bravo"),Answer("Respuesta semicorrecta","Pichí pichá","50"),Answer("Respuesta incorrecta","Lo sisento, amigo","0"),Answer("Respuesta muy incorrecta","Madre mía cómo has podido poner esto","-30")],"Gracias, amigo")
printedQuestion = multipleChoice.printQuestion()
print(printedQuestion)

oneAnswer = OneAnswer("Test/C3","MC1","Color del caballo blanco de Santiago",[Answer("Blanco"),Answer("White"),Answer("Txuria"),Answer("Blanche")],"Gracias, amigo")
printedQuestion = oneAnswer.printQuestion()
print(printedQuestion)

numeric = Numeric("Test/C3","MC1","Valor de Pi",[Answer("3.14",numericTolerance="0.01")],"Gracias, amigo")
printedQuestion = numeric.printQuestion()
print(printedQuestion)
 """

from excel.ExcelCreator import ExcelCreator
from excel.ExcelExtractor import ExcelExtractor

#template = ExcelCreator(True,True,True,True,demoData = True)
#ExplorerOpen.ExplorerOpen(template.path)
#ExplorerOpen.ExplorerOpen(excel.path + '\\' + excel.filename)
excel = ExcelExtractor('MoodleExcel.xlsx')
multipleChoiceDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.MULTIPLE_CHOICE_SHEET_NAME)
trueFalseQuestions = excel.ExtractQuestionsFromSheet(CS.TRUE_FALSE_SHEET_NAME)
numericQuestions = excel.ExtractQuestionsFromSheet(CS.NUMERIC_SHEET_NAME)
oneAnswerQuestions = excel.ExtractQuestionsFromSheet(CS.ONE_ANSWER_SHEET_NAME)

multipleChoiceQuestions = MultipleChoice.createMultipleChoiceQuestionsFromDictionaryArray(multipleChoiceDictionaryQuestions,excel.mainCategory)
for question in multipleChoiceQuestions.questionsArray:
    print(question.printQuestion())
pass