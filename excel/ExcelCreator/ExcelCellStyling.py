from openpyxl.styles.fills import PatternFill
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import Border, Side
from openpyxl.worksheet.worksheet import Worksheet

class ExcelCellStyling:
    """Class for excel styling"""
    def __change_cell_background_and_text_colors(self, cell, background_color='FFFFFF', text_color='000000'):
        cell.fill = PatternFill("solid", start_color= background_color)
        cell.font = Font(b= True, color= text_color)

    def __apply_full_border_to_cell(self, cell):
        cell.border = Border(left=Side(style='thin'),
                     right=Side(style='thin'),
                     top=Side(style='thin'),
                     bottom=Side(style='thin'))

    def __change_cell_alignment(self,
                                cell,
                                horizontal_alignment='left',
                                vertical_alignment='top',
                                wrap_text = True):
        cell.alignment = Alignment(horizontal= horizontal_alignment,
                                   vertical= vertical_alignment,
                                   wrap_text= wrap_text)

    def __adjust_sheet_row_size(self, sheet, row, height):
        sheet.row_dimensions[row].height = height

    def __adjust_sheet_column_size(self, sheet, column, width):
        sheet.column_dimensions[column].width = width

    def first_row_adequation(self, sheet: Worksheet):
        """Editing first row with border and background"""
        last_column_letter = sheet.dimensions[3]
        for row in sheet['A1':last_column_letter+'1']:
            for cell in row:
                self.__change_cell_alignment(cell,'center','center')
                self.__change_cell_background_and_text_colors(cell,'E7AA73','653159')
                self.__adjust_sheet_column_size(sheet,cell.column_letter,18)
                self.__apply_full_border_to_cell(cell)
        self.__adjust_sheet_row_size(sheet,1,38)
