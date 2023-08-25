from pathlib import Path
from os import path as OSPath
from enum import Enum
from openpyxl import Workbook
from openpyxl.comments import Comment
import misc.Constants as CS
from . import ExcelCellStyling

class ExcelMode(Enum):
    """Enum: Excel creation or extraction"""
    CREATE = 1
    EXTRACT = 2

class ExcelCreator:
    """Class to create excel files with example"""
    def __init__(self,
                 path = '',
                 excel_mode: ExcelMode = ExcelMode.CREATE,
                 create_multiple_choice = False,
                 create_true_false = False,
                 create_one_answer = False,
                 create_numeric = False,
                 demo_data = False):
        if excel_mode == ExcelMode.CREATE:
            self.__path = path if path != '' else Path().resolve().__str__()
            self.__filename = CS.FILENAME
            self.__wb = Workbook()
            first_sheet = self.__wb.active
            self.__configure_settings_sheet(first_sheet, demo_data)
            if create_multiple_choice:
                self.__create_multiple_choice_sheet(self.__wb,demo_data)
            if create_one_answer:
                self.__create_one_answer_sheet(self.__wb, demo_data)
            if create_true_false:
                self.__create_true_false_sheet(self.__wb, demo_data)
            if create_numeric:
                self.__create_numeric_sheet(self.__wb, demo_data)
            self.__wb.save(OSPath.join(self.__path,self.__filename))

    def __configure_settings_sheet(self, ws, demoData = False):
        ws.title = CS.SETTINGS_SHEET_NAME
        ws['A1'] = CS.SETTINGS_SUBJECT_NAME_TITLE
        ws['B1'] = CS.SETTINGS_CHAPTER_NAME_TITLE
        ws['E1'] = CS.SETTINGS_MANDATORY_FIELD_LABEL
        for row in ws['A1':'B1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        if demoData:
            ws['A2'] = "SMX_M03"
            ws['B2'] = "Spreadsheet"
        for row in ws['A2':'B2']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_multiple_choice_sheet(self, wb, demoData = False):
        """Function to create multiple choice sheets"""
        ws = wb.create_sheet(CS.MULTIPLE_CHOICE_SHEET_NAME)
        ws['A1'] = CS.MULTIPLE_CHOICE_QUESTION_TITLE
        ws['B1'] = CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE
        ws['C1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE
        ws['D1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE
        ws['E1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE
        ws['F1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE
        ws['G1'] = CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE
        ws['G1'].comment = Comment(CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_COMMENT,"admin",250,200)
        ws['H1'] = CS.MULTIPLE_CHOICE_FEEDBACK_TITLE
        ws['I1'] = CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE
        for row in ws['A1':'I1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        if demoData:
            ws['A2'] = "Meaning of CPU?"
            ws['B2'] = "Control process unit"
            ws['C2'] = "Carpenter public uniform"
            ws['D2'] = "Car pen use"
            ws['E2'] = "Coconut private use"
            ws['F2'] = "Cardigan pickle uniform"
            ws['G2'] = "-30"
            ws['H2'] = "A central processing unit (CPU) is the electronic circuitry that executes instructions comprising a computer program."
            ws['I2'] = "Processing"
        for row in ws['A2':'I20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_one_answer_sheet(self, wb, demoData = False):
        ws = wb.create_sheet(CS.ONE_ANSWER_SHEET_NAME)
        ws['A1'] = CS.ONE_ANSWER_QUESTION_TITLE
        ws['B1'] = CS.ONE_ANSWER_CORRECT_ANSWER_TITLE
        ws['C1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE
        ws['D1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE
        ws['E1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE
        ws['F1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE
        ws['G1'] = CS.ONE_ANSWER_FEEDBACK_TITLE
        ws['H1'] = CS.ONE_ANSWER_SUBCATEGORY_TITLE
        for row in ws['A1':'H1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        if demoData:
            ws['A2'] = "Color of one original Power Rangers"
            ws['B2'] = "Red"
            ws['C2'] = "Blue"
            ws['D2'] = "Yellow"
            ws['E2'] = "Pink"
            ws['F2'] = "Black"
            ws['G2'] = "The color of the original Rangers are red, blue, yellow, pink and black"
            ws['H2'] = "Television"
        for row in ws['A2':'H20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_true_false_sheet(self, wb, demoData = False):
        ws = wb.create_sheet(CS.TRUE_FALSE_SHEET_NAME)
        ws['A1'] = CS.TRUE_FALSE_QUESTION_TITLE
        ws['B1'] = CS.TRUE_FALSE_ANSWER_TITLE
        ws['C1'] = CS.TRUE_FALSE_FEEDBACK_TITLE
        ws['D1'] = CS.TRUE_FALSE_SUBCATEGORY_TITLE
        for row in ws['A1':'D1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,20)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        if demoData:
            ws['A2'] = "RAM memory is volatile"
            ws['B2'] = "T"
            ws['C2'] = "RAM is volatile memory, which means that the information temporarily stored in the module is erased when you restart or shut down your computer."
            ws['D2'] = "Processing"
        for row in ws['A2':'D20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_numeric_sheet(self, wb, demoData = False):
        ws = wb.create_sheet(CS.NUMERIC_SHEET_NAME)
        ws['A1'] = CS.NUMERIC_QUESTION_TITLE
        ws['B1'] = CS.NUMERIC_CORRECT_VALUE_TITLE
        ws['C1'] = CS.NUMERIC_TOLERANCE_TITLE
        ws['D1'] = CS.NUMERIC_FEEDBACK_TITLE
        ws['E1'] = CS.NUMERIC_SUBCATEGORY_TITLE
        for row in ws['A1':'E1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        if demoData:
            ws['A2'] = "Value of Pi?"
            ws['B2'] = "3.14"
            ws['C2'] = "0.01"
            ws['D2'] = "Value of Pi is 3.141592653589793238"
            ws['E2'] = "Math"
        for row in ws['A2':'E20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
