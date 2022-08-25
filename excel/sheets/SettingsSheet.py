from openpyxl.comments import Comment
from excel.ExcelCellStyling import ExcelCellStyling

class SettingsSheet: 
    def configureSettingsSheet(ws):
        ws.title = 'Settings'
        ws['A1'] = "Subject name *"
        ws['B1'] = "Chapter name *"
        ws['E1'] = "* Mandatory fields"
        for row in ws['A1':'B1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        ws['A2'] = "SMX_M03"
        ws['B2'] = "Spreadsheet"
        for row in ws['A2':'B2']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
