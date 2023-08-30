"""Excel extractor class"""
import openpyxl
import json
import misc.Constants as CS

with open("static/excel_creation_constants.json", "r", encoding="utf8") as file:
    constants = json.load(file)

class ExcelExtractor:
    """Class to extract excel information into an array"""
    def __init__(self, filepath):
        try:
            self.__wb = openpyxl.load_workbook(filepath)
        except FileNotFoundError:
            raise FileNotFoundError("File not found. Please check the path")
        settings_constants = constants["settings_sheet"]
        ## REVISAR QUE EL WB TIENE SHEET DE SETTINGS
        try:
            settings_sheet = self.__wb[settings_constants["name"]]
        except KeyError:
            raise KeyError("A sheet named Settings is missing. Please, create one")
        subject_name_cell = settings_constants["data"]["subject_name"]
        chapter_name_cell = settings_constants["data"]["chapter_name"]
        subject_name = settings_sheet[subject_name_cell].value or ''
        chapter_name = settings_sheet[chapter_name_cell].value or ''
        pass
        # settings_sheet_constants = constants["settings_sheet"]
        # subject_cell = settings_sheet_constants["data"]["subject_name"]
        # subjectName = self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_SUBJECT_NAME_CELL].value +\
        #       '/' if  self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_SUBJECT_NAME_CELL].value else ''
        # chapterName =  self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_CHAPTER_NAME_CELL].value  if self.wb[CS.SETTINGS_SHEET_NAME][CS.SHEET_CHAPTER_NAME_CELL].value else ''      
        # self.mainCategory = subjectName + chapterName

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