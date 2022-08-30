from ctypes import alignment
from turtle import color
from MoodleQuestions.Array.MultipleChoiceArray import MultipleChoiceArray
from MoodleQuestions.Array.NumericArray import NumericArray
from MoodleQuestions.Array.OneAnswerArray import OneAnswerArray
from MoodleQuestions.Array.TrueFalseArray import TrueFalseArray
from MoodleQuestions.Base.MultipleChoice import MultipleChoice
from MoodleQuestions.Base.Numeric import Numeric
from MoodleQuestions.Base.OneAnswer import OneAnswer
from MoodleQuestions.Base.TrueFalse import TrueFalse
from MoodleQuestions.Base.Answer import Answer
from MoodleQuestions.Base.MultipleChoice import MultipleChoice
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

# template = ExcelCreator(True,True,True,True,demoData = True)
# ExplorerOpen.ExplorerOpen(template.path)
# ExplorerOpen.ExplorerOpen(template.path + '\\' + template.filename)
excel = ExcelExtractor('MoodleExcel.xlsx')
# multipleChoiceDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.MULTIPLE_CHOICE_SHEET_NAME)
# trueFalseDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.TRUE_FALSE_SHEET_NAME)
# oneAnswerDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.ONE_ANSWER_SHEET_NAME)
numericDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.NUMERIC_SHEET_NAME)

# trueFalseQuestions = TrueFalseArray()
# trueFalseQuestions.createQuestionsArrayFromDictionaryArray(trueFalseDictionaryQuestions,excel.mainCategory)
# for question in trueFalseQuestions.questionsArray:
#     print(question.printQuestion())
# multipleChoiceQuestions = MultipleChoiceArray()
# multipleChoiceQuestions.createQuestionsArrayFromDictionaryArray(multipleChoiceDictionaryQuestions,excel.mainCategory)
# for question in multipleChoiceQuestions.questionsArray:
#     print(question.printQuestion())
# oneAnswerQuestions = OneAnswerArray()
# oneAnswerQuestions.createQuestionsArrayFromDictionaryArray(oneAnswerDictionaryQuestions,excel.mainCategory)
# for question in oneAnswerQuestions.questionsArray:
#     print(question.printQuestion())
numericQuestions = NumericArray()
numericQuestions.createQuestionsArrayFromDictionaryArray(numericDictionaryQuestions,excel.mainCategory)
for question in numericQuestions.questionsArray:
    print(question.printQuestion())

pass