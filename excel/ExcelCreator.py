from openpyxl import Workbook
from excel.sheets.MultipleChoiceSheet import MultipleChoiceSheet
from excel.sheets.TrueFalseSheet import TrueFalseSheet
from excel.sheets.NumericSheet import NumericSheet
from excel.sheets.OneAnswerSheet import OneAnswerSheet
from excel.sheets.SettingsSheet import SettingsSheet
import pathlib
import misc.Constants as CS
from os import path as OSPath

class ExcelCreator:

    def __init__(self,createMultipleChoice = False, createTrueFalse = False, createOneAnswer = False, createNumeric = False, path = '', demoData = False):
        self.path = path if path != '' else pathlib.Path().resolve().__str__()
        self.filename = CS.FILENAME
        self.wb = Workbook()
        ws = self.wb.active
        SettingsSheet.configureSettingsSheet(ws, demoData)
        if createMultipleChoice: 
            MultipleChoiceSheet.createMultipleChoiceSheet(self.wb,demoData)
        if createOneAnswer:
            OneAnswerSheet.createOneAnswerSheet(self.wb, demoData)
        if createTrueFalse:
            TrueFalseSheet.createTrueFalseSheet(self.wb, demoData)
        if createNumeric:
            NumericSheet.createNumericSheet(self.wb, demoData)
        self.wb.save(OSPath.join(self.path,self.filename))