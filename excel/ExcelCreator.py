from openpyxl import Workbook
from excel.sheets.MultipleChoiceSheet import MultipleChoiceSheet
from excel.sheets.TrueFalseSheet import TrueFalseSheet
from excel.sheets.NumericSheet import NumericSheet
from excel.sheets.OneAnswerSheet import OneAnswerSheet
from excel.sheets.SettingsSheet import SettingsSheet
import pathlib

class ExcelCreator:

    def __init__(self,createMultipleChoice = False, createTrueFalse = False, createOneAnswer = False, createNumeric = False, path = ''):
        self.path = path if path != '' else pathlib.Path().resolve().__str__()
        self.filename = 'MoodleExcel.xlsx'
        self.wb = Workbook()
        ws = self.wb.active
        SettingsSheet.configureSettingsSheet(ws)
        if createMultipleChoice: 
            MultipleChoiceSheet.createMultipleChoiceSheet(self.wb)
        if createOneAnswer:
            OneAnswerSheet.createOneAnswerSheet(self.wb)
        if createTrueFalse:
            TrueFalseSheet.createTrueFalseSheet(self.wb)
        if createNumeric:
            NumericSheet.createNumericSheet(self.wb)
        self.wb.save(self.path + '\\' + self.filename)