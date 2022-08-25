from openpyxl.comments import Comment
from excel.ExcelCellStyling import ExcelCellStyling

class NumericSheet: 
    def createNumericSheet(wb):
        ws = wb.create_sheet("Numeric")
        ws['A1'] = "Question *"
        ws['B1'] = "Correct numeric value *"
        ws['C1'] = "Numeric tolerance *"
        ws['D1'] = "Feedback"
        ws['E1'] = "Subcategory"
        for row in ws['A1':'E1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
        ws['A2'] = "Value of Pi?"
        ws['B2'] = "3.14"
        ws['C2'] = "0.01"
        ws['D2'] = "Value of Pi is 3.141592653589793238"
        ws['E2'] = "Math"
        for row in ws['A2':'E20']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,wrap_text=True)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
