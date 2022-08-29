import openpyxl
import misc.Constants as CS

class ExcelExtractor:
    def __init__(self, filepath):
        self.wb = openpyxl.load_workbook(filepath)
        subjectName = self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_SUBJECT_NAME_CELL].value + '/' if  self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_SUBJECT_NAME_CELL].value else ''
        chapterName =  self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_CHAPTER_NAME_CELL].value  if self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_CHAPTER_NAME_CELL].value else ''      
        self.mainCategory = subjectName + chapterName

    def ExtractQuestionsFromSheet(self,sheetName):
        ws = self.wb[sheetName]
        headers = []
        questionsArray = []
        for cell in ws[1]:
            headers.append(cell.value)
        for row in ws[2:10000]:
            if row[0].value == None: break
            questionData = {}
            for i, cell in enumerate(row):
                questionData[headers[i]] = str(cell.value) if cell.value != None else None
            questionsArray.append(questionData)
        return questionsArray