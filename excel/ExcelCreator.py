from openpyxl import Workbook
from excel.sheets.MultipleChoiceSheet import MultipleChoiceSheet
from excel.sheets.TrueFalseSheet import TrueFalseSheet
from excel.sheets.NumericSheet import NumericSheet
from excel.sheets.OneAnswerSheet import OneAnswerSheet
from excel.sheets.SettingsSheet import SettingsSheet

class ExcelCreator:

    def __init__(self,createMultipleChoice = False, createTrueFalse = False, createOneAnswer = False, createNumeric = False):
        wb = Workbook()
        ws = wb.active
        SettingsSheet.configureSettingsSheet(ws)
        if createMultipleChoice: 
            MultipleChoiceSheet.createMultipleChoiceSheet(wb)
        if createOneAnswer:
            OneAnswerSheet.createOneAnswerSheet(wb)
        if createTrueFalse:
            TrueFalseSheet.createTrueFalseSheet(wb)
        if createNumeric:
            NumericSheet.createNumericSheet(wb)
        wb.save('MoodleExcel.xlsx')