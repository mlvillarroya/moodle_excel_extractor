import webbrowser
import openpyxl
import misc.Constants as CS
from MoodleQuestions.MultipleChoice import MultipleChoice

class ExcelExtractor:
    def __init__(self, filepath):
        self.wb = openpyxl.load_workbook(filepath)
        self.mainCategory = self.wb[CS.SETTINGS_SHEET_NAME]['A2'].value + '/' + self.wb[CS.SETTINGS_SHEET_NAME]['B2'].value + '/'

    def ExtractQuestionsFromSheet(self,sheetName):
        ws = self.wb[sheetName]
        headers = []
        questionsArray = []
        for cell in ws[1]:
            headers.append(cell.value)
        for row in ws[2:ws.max_column]:
            if row[0].value == None: break
            questionData = {}
            for i, cell in enumerate(row):
                questionData[headers[i]] = str(cell.value) if cell.value != None else None
            questionsArray.append(questionData)
        return questionsArray