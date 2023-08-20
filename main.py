"""Main program"""
import tkinter as tk
from tkinter import ttk
from MoodleQuestions.Array.MultipleChoiceArray import MultipleChoiceArray
from MoodleQuestions.Array.NumericArray import NumericArray
from MoodleQuestions.Array.OneAnswerArray import OneAnswerArray
from MoodleQuestions.Array.TrueFalseArray import TrueFalseArray
from MoodleQuestions.Question_answer.Question_types import MultipleChoice
from MoodleQuestions.Question_answer.Question_types import Numeric
from MoodleQuestions.Question_answer.Question_types import OneAnswer
from MoodleQuestions.Question_answer.Question_types import TrueFalse
from MoodleQuestions.Question_answer.Question_types import Answer
from MoodleQuestions.Question_answer.Question_types import MultipleChoice
from misc.ExplorerOpen import ExplorerOpen
import misc.Constants as CS
from misc import Windows

from GUI.Style import Style

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
from GUI.Frames.CreateExcelFrame import CreateExcelFrame
from GUI.Frames.CreateInstructionsFrame import CreateInstructionsFrame

# template = ExcelCreator(True,True,True,True,demoData = True)
# ExplorerOpen.ExplorerOpen(template.path)
# ExplorerOpen.ExplorerOpen(template.path + '\\' + template.filename)
# excel = ExcelExtractor('MoodleExcel.xlsx')
# multipleChoiceDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.MULTIPLE_CHOICE_SHEET_NAME)
# trueFalseDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.TRUE_FALSE_SHEET_NAME)
# oneAnswerDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.ONE_ANSWER_SHEET_NAME)
# numericDictionaryQuestions = excel.ExtractQuestionsFromSheet(CS.NUMERIC_SHEET_NAME)

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
# numericQuestions = NumericArray()
# numericQuestions.createQuestionsArrayFromDictionaryArray(numericDictionaryQuestions,excel.mainCategory)
# for question in numericQuestions.questionsArray:
#     print(question.printQuestion())

# pass

Windows.setDpiAwareness()

root = tk.Tk()
root.geometry("768x768")
root.resizable(False,False)
root.title("Moodle questions creator")

# create a notebook
notebook = ttk.Notebook(root, padding=10)
notebook.pack(fill='both', expand=True)

# create notebook frames
instructionsFrame = CreateInstructionsFrame(notebook)
createExcelFrame = CreateExcelFrame(notebook)
extractExcelFrame = ttk.Frame(notebook)

instructionsFrame.pack(fill='both', expand=True)
createExcelFrame.pack(fill='both', expand=True)
extractExcelFrame.pack(fill='both', expand=True)

# add frames to notebook
notebook.add(createExcelFrame, text='Create Excel')
notebook.add(extractExcelFrame, text='Import Excel')
notebook.add(instructionsFrame, text='Instructions')

#styles
Style.ConfigureGuiStyle()

root.mainloop()