from openpyxl import Workbook
from excel.sheets.MultipleChoiceSheet import MultipleChoiceSheet
from excel.sheets.TrueFalseSheet import TrueFalseSheet
from excel.sheets.NumericSheet import NumericSheet

class ExcelCreator:

    def __init__(self,createMultipleChoice = False, createTrueFalse = False, createOneAnswer = False, createNumeric = False):
        wb = Workbook()
        ws = wb.active
        ws.title = 'Settings'
        self.createSettingsSheet(ws)
        if createMultipleChoice: 
            MultipleChoiceSheet.createMultipleChoiceSheet(wb)
        if createOneAnswer: wb.create_sheet("One answer")
        if createTrueFalse:
            TrueFalseSheet.createTrueFalseSheet(wb)
        if createNumeric:
            NumericSheet.createNumericSheet(wb)
        wb.save('MoodleExcel.xlsx')

    def createSettingsSheet(self,ws):
        ws['A1'] = "Subject name"

