from pathlib import Path
import json
from os import path as OSPath
from enum import Enum
from openpyxl import Workbook
from openpyxl.comments import Comment
import misc.Constants as CS
from . import ExcelCellStyling

with open("static/excel_demo_constants.json", "r", encoding="utf8") as file:
    constants = json.load(file)

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
            self.__configure_settings_sheet(demo_data)
            if create_multiple_choice:
                self.__create_multiple_choice_sheet(demo_data)
            if create_one_answer:
                self.__create_one_answer_sheet(demo_data)
            if create_true_false:
                self.__create_true_false_sheet(demo_data)
            if create_numeric:
                self.__create_numeric_sheet(demo_data)
            self.__wb.save(OSPath.join(self.__path,self.__filename))

    @property
    def path(self):
        """Property: path"""
        return self.__path

    @property
    def filename(self):
        """Property: path"""
        return self.__filename

    @property
    def workbook(self):
        """Property: path"""
        return self.__wb

    def __configure_settings_sheet(self, demo_data = False):
        settings_constants = constants["settings_sheet"]
        settings_sheet_name = settings_constants["name"]
        settings_sheet_coordinates = settings_constants["cell_coordinates"]
        settings_sheet_labels = settings_constants["cell_labels"]
        first_sheet = self.__wb.active
        first_sheet.title = settings_sheet_name
        first_sheet[settings_sheet_coordinates["subject_name"]] =\
            settings_sheet_labels["subject_name"]
        first_sheet[settings_sheet_coordinates["chapter_name"]] =\
            settings_sheet_labels["chapter_name"]
        first_sheet[settings_sheet_coordinates["mandatory_field_label"]] =\
            settings_sheet_labels["mandatory_field_label"]
        for row in first_sheet['A1':'B1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(first_sheet,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(first_sheet,1,38)
        if demo_data:
            first_sheet['A2'] = "SMX_M03"
            first_sheet['B2'] = "Spreadsheet"
        for row in first_sheet['A2':'B2']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_multiple_choice_sheet(self, demo_data = False):
        """Function to create multiple choice sheets"""
        multiple_choice_sheet = self.__wb.create_sheet(CS.MULTIPLE_CHOICE_SHEET_NAME)
        multiple_choice_sheet['A1'] = CS.MULTIPLE_CHOICE_QUESTION_TITLE
        multiple_choice_sheet['B1'] = CS.MULTIPLE_CHOICE_CORRECT_ANSWER_TITLE
        multiple_choice_sheet['C1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_1_TITLE
        multiple_choice_sheet['D1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_2_TITLE
        multiple_choice_sheet['E1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_3_TITLE
        multiple_choice_sheet['F1'] = CS.MULTIPLE_CHOICE_INCORRECT_ANSWER_4_TITLE
        multiple_choice_sheet['G1'] = CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_TITLE
        multiple_choice_sheet['G1'].comment = Comment(CS.MULTIPLE_CHOICE_BAD_ANSWER_POINTS_COMMENT,"admin",250,200)
        multiple_choice_sheet['H1'] = CS.MULTIPLE_CHOICE_FEEDBACK_TITLE
        multiple_choice_sheet['I1'] = CS.MULTIPLE_CHOICE_SUBCATEGORY_TITLE
        for row in multiple_choice_sheet['A1':'I1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(multiple_choice_sheet,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(multiple_choice_sheet,1,38)
        if demo_data:
            multiple_choice_sheet['A2'] = "Meaning of CPU?"
            multiple_choice_sheet['B2'] = "Control process unit"
            multiple_choice_sheet['C2'] = "Carpenter public uniform"
            multiple_choice_sheet['D2'] = "Car pen use"
            multiple_choice_sheet['E2'] = "Coconut private use"
            multiple_choice_sheet['F2'] = "Cardigan pickle uniform"
            multiple_choice_sheet['G2'] = "-30"
            multiple_choice_sheet['H2'] = "A central processing unit (CPU) is the electronic circuitry that executes instructions comprising a computer program."
            multiple_choice_sheet['I2'] = "Processing"
        for row in multiple_choice_sheet['A2':'I20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_one_answer_sheet(self, demo_data = False):
        one_answer_sheet = self.__wb.create_sheet(CS.ONE_ANSWER_SHEET_NAME)
        one_answer_sheet['A1'] = CS.ONE_ANSWER_QUESTION_TITLE
        one_answer_sheet['B1'] = CS.ONE_ANSWER_CORRECT_ANSWER_TITLE
        one_answer_sheet['C1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_1_TITLE
        one_answer_sheet['D1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_2_TITLE
        one_answer_sheet['E1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_3_TITLE
        one_answer_sheet['F1'] = CS.ONE_ANSWER_ALTERNATE_CORRECT_ANSWER_4_TITLE
        one_answer_sheet['G1'] = CS.ONE_ANSWER_FEEDBACK_TITLE
        one_answer_sheet['H1'] = CS.ONE_ANSWER_SUBCATEGORY_TITLE
        for row in one_answer_sheet['A1':'H1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(one_answer_sheet,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(one_answer_sheet,1,38)
        if demo_data:
            one_answer_sheet['A2'] = "Color of one original Power Rangers"
            one_answer_sheet['B2'] = "Red"
            one_answer_sheet['C2'] = "Blue"
            one_answer_sheet['D2'] = "Yellow"
            one_answer_sheet['E2'] = "Pink"
            one_answer_sheet['F2'] = "Black"
            one_answer_sheet['G2'] = "The color of the original Rangers are red, blue, yellow, pink and black"
            one_answer_sheet['H2'] = "Television"
        for row in one_answer_sheet['A2':'H20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_true_false_sheet(self, demo_data = False):
        true_false_sheet = self.__wb.create_sheet(CS.TRUE_FALSE_SHEET_NAME)
        true_false_sheet['A1'] = CS.TRUE_FALSE_QUESTION_TITLE
        true_false_sheet['B1'] = CS.TRUE_FALSE_ANSWER_TITLE
        true_false_sheet['C1'] = CS.TRUE_FALSE_FEEDBACK_TITLE
        true_false_sheet['D1'] = CS.TRUE_FALSE_SUBCATEGORY_TITLE
        for row in true_false_sheet['A1':'D1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(true_false_sheet,cell.column_letter,20)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(true_false_sheet,1,38)
        if demo_data:
            true_false_sheet['A2'] = "RAM memory is volatile"
            true_false_sheet['B2'] = "T"
            true_false_sheet['C2'] = "RAM is volatile memory, which means that the information temporarily stored in the module is erased when you restart or shut down your computer."
            true_false_sheet['D2'] = "Processing"
        for row in true_false_sheet['A2':'D20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell, wrap_text= True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)

    def __create_numeric_sheet(self, demo_data = False):
        numeric_sheet = self.__wb.create_sheet(CS.NUMERIC_SHEET_NAME)
        numeric_sheet['A1'] = CS.NUMERIC_QUESTION_TITLE
        numeric_sheet['B1'] = CS.NUMERIC_CORRECT_VALUE_TITLE
        numeric_sheet['C1'] = CS.NUMERIC_TOLERANCE_TITLE
        numeric_sheet['D1'] = CS.NUMERIC_FEEDBACK_TITLE
        numeric_sheet['E1'] = CS.NUMERIC_SUBCATEGORY_TITLE
        for row in numeric_sheet['A1':'E1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(numeric_sheet,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(numeric_sheet,1,38)
        if demo_data:
            numeric_sheet['A2'] = "Value of Pi?"
            numeric_sheet['B2'] = "3.14"
            numeric_sheet['C2'] = "0.01"
            numeric_sheet['D2'] = "Value of Pi is 3.141592653589793238"
            numeric_sheet['E2'] = "Math"
        for row in numeric_sheet['A2':'E20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
