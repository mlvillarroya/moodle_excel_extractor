from openpyxl.styles.fills import PatternFill
from openpyxl.styles import Font
from openpyxl.styles import Alignment
from openpyxl.styles import Border, Side

class ExcelCellStyling:
    def ChangeCellBackgroundAndTextColors(cell,backgroundColor='FFFFFF',textColor='000000'):
        cell.fill = PatternFill("solid", start_color="E7AA73")
        cell.font=Font(b=True, color="653159")
    
    def ApplyFullBorderToCell(cell):
        cell.border = Border(left=Side(style='thin'), 
                     right=Side(style='thin'), 
                     top=Side(style='thin'), 
                     bottom=Side(style='thin'))

    def ChangeCellAlignment(cell, horizontalAlignment='left',verticalAlignment='top',wrap_text = True):
        cell.alignment = Alignment(horizontal=horizontalAlignment,vertical=verticalAlignment,wrap_text=wrap_text)

    def adjustSheetRowSize(ws,row,height):
        ws.row_dimensions[row].height = height

    def adjustSheetColumnSize(ws,column,width):
        ws.column_dimensions[column].width = width
