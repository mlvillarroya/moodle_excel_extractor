from pathlib import Path
import json
from os import remove as OSRemove
from os import path as OSPath
from enum import Enum
from openpyxl import Workbook
from openpyxl.comments import Comment
import misc.Constants as CS
from . import ExcelCellStyling

with open("static/excel_creation_constants.json", "r", encoding="utf8") as file:
    constants = json.load(file)
styling = ExcelCellStyling()

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

    def save_excel_file(self):
        """Function to save the workbook into a file"""
        self.__wb.save(OSPath.join(self.__path,self.__filename))

    def remove_excel_file(self):
        """Function to save the workbook into a file"""
        OSRemove(OSPath.join(self.__path,self.__filename))

    def __configure_settings_sheet(self, demo_data= False):
        settings_constants = constants["settings_sheet"]
        first_sheet = self.__wb.active
        self.__insert_cell_text_into_sheet(settings_constants, first_sheet)
        styling.first_row_adequation(first_sheet,'B')
        if demo_data:
            self.__insert_demo_data_into_sheet(settings_constants, first_sheet)

    def __create_multiple_choice_sheet(self, demo_data= False):
        """Function to create multiple choice sheets"""
        multiple_choice_constants = constants["multiple_choice_sheet"]
        multiple_choice_sheet = self.__wb.create_sheet()
        self.__insert_cell_text_into_sheet(multiple_choice_constants, multiple_choice_sheet)
        styling.first_row_adequation(multiple_choice_sheet,'I')
        if demo_data:
            self.__insert_demo_data_into_sheet(multiple_choice_constants, multiple_choice_sheet)

    def __create_one_answer_sheet(self, demo_data = False):
        one_answer_constants = constants["one_answer_sheet"]
        one_answer_sheet = self.__wb.create_sheet()
        self.__insert_cell_text_into_sheet(one_answer_constants, one_answer_sheet)
        styling.first_row_adequation(one_answer_sheet,'H')
        if demo_data:
            self.__insert_demo_data_into_sheet(one_answer_constants, one_answer_sheet)

    def __create_true_false_sheet(self, demo_data = False):
        true_false_sheet = self.__wb.create_sheet(CS.TRUE_FALSE_SHEET_NAME)
        true_false_sheet['A1'] = CS.TRUE_FALSE_QUESTION_TITLE
        true_false_sheet['B1'] = CS.TRUE_FALSE_ANSWER_TITLE
        true_false_sheet['C1'] = CS.TRUE_FALSE_FEEDBACK_TITLE
        true_false_sheet['D1'] = CS.TRUE_FALSE_SUBCATEGORY_TITLE
        for row in true_false_sheet['A1':'D1']:
            for cell in row:
                ExcelCellStyling.__change_cell_alignment(cell,'center','center')
                ExcelCellStyling.__change_cell_background_and_text_colors(cell,'E7AA73','653159')
                ExcelCellStyling.__adjust_sheet_column_size(true_false_sheet,cell.column_letter,20)
                ExcelCellStyling.__apply_full_border_to_cell(cell)
        ExcelCellStyling.__adjust_sheet_row_size(true_false_sheet,1,38)
        if demo_data:
            true_false_sheet['A2'] = "RAM memory is volatile"
            true_false_sheet['B2'] = "T"
            true_false_sheet['C2'] = "RAM is volatile memory, which means that the information temporarily stored in the module is erased when you restart or shut down your computer."
            true_false_sheet['D2'] = "Processing"
        for row in true_false_sheet['A2':'D20']:
            for cell in row:
                ExcelCellStyling.__change_cell_alignment(cell, wrap_text= True)
                ExcelCellStyling.__apply_full_border_to_cell(cell)

    def __create_numeric_sheet(self, demo_data = False):
        numeric_sheet = self.__wb.create_sheet(CS.NUMERIC_SHEET_NAME)
        numeric_sheet['A1'] = CS.NUMERIC_QUESTION_TITLE
        numeric_sheet['B1'] = CS.NUMERIC_CORRECT_VALUE_TITLE
        numeric_sheet['C1'] = CS.NUMERIC_TOLERANCE_TITLE
        numeric_sheet['D1'] = CS.NUMERIC_FEEDBACK_TITLE
        numeric_sheet['E1'] = CS.NUMERIC_SUBCATEGORY_TITLE
        for row in numeric_sheet['A1':'E1']:
            for cell in row:
                ExcelCellStyling.__change_cell_alignment(cell,'center','center')
                ExcelCellStyling.__change_cell_background_and_text_colors(cell,'E7AA73','653159')
                ExcelCellStyling.__adjust_sheet_column_size(numeric_sheet,cell.column_letter,18)
                ExcelCellStyling.__apply_full_border_to_cell(cell)
        ExcelCellStyling.__adjust_sheet_row_size(numeric_sheet,1,38)
        if demo_data:
            numeric_sheet['A2'] = "Value of Pi?"
            numeric_sheet['B2'] = "3.14"
            numeric_sheet['C2'] = "0.01"
            numeric_sheet['D2'] = "Value of Pi is 3.141592653589793238"
            numeric_sheet['E2'] = "Math"
        for row in numeric_sheet['A2':'E20']:
            for cell in row:
                ExcelCellStyling.__change_cell_alignment(cell,wrap_text=True)
                ExcelCellStyling.__apply_full_border_to_cell(cell)

    def __insert_cell_text_into_sheet(self, constants_dict, sheet):
        sheet_name = constants_dict["name"]
        sheet.title = sheet_name
        sheet_cells_data = constants_dict["cells"]
        for coordinates, name in sheet_cells_data.values():
            sheet[coordinates] = name

    def __insert_demo_data_into_sheet(self, constants_dict, sheet):
        demo_data = constants_dict["demo_data"]
        for coordinates, name in demo_data.values():
            sheet[coordinates] = name
