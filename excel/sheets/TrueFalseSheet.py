from openpyxl.comments import Comment
from excel.ExcelCellStyling import ExcelCellStyling

class TrueFalseSheet: 
    def createTrueFalseSheet(wb):
        ws = wb.create_sheet("True false")
        ws['A1'] = "Question *"
        ws['B1'] = "True (T) or False (F)? *"
        ws['C1'] = "Feedback"
        ws['D1'] = "Subcategory"
        for row in ws['A1':'D1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,20)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        ws['A2'] = "RAM memory is volatile"
        ws['B2'] = "T"
        ws['C2'] = "RAM is volatile memory, which means that the information temporarily stored in the module is erased when you restart or shut down your computer."
        ws['D2'] = "Processing"
        for row in ws['A2':'D20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
