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
        try:
            settings_sheet = self.__wb[settings_constants["name"]]
        except KeyError:
            raise KeyError("A sheet named Settings is missing. Please, create one")
        subject_name_cell = settings_constants["data"]["subject_name"]
        chapter_name_cell = settings_constants["data"]["chapter_name"]
        subject_name = settings_sheet[subject_name_cell].value
        chapter_name = settings_sheet[chapter_name_cell].value
        self.__main_category = '/'.join(filter(None, (subject_name, chapter_name)))

    @property
    def main_category(self):
        return self.__main_category
    
    @property
    def workbook(self):
        return self.__wb

    def __extract_questions_from_sheet(self,sheetName):
        ws = self.__wb[sheetName]
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

    def __get_sheet_width(self, sheet):
        return sheet.max_column
    
    def __get_mandatory_columns(self, sheet):
        fist_row = sheet[1]
        mandatory_columns = []
        for i, cell in enumerate(fist_row):
            if "*" in cell.value:
                mandatory_columns.append(i+1)
        return mandatory_columns