from openpyxl.comments import Comment
from excel.ExcelCellStyling import ExcelCellStyling

class OneAnswerSheet: 
    def createOneAnswerSheet(wb):
        ws = wb.create_sheet("One answer")
        ws['A1'] = "Question *"
        ws['B1'] = "Correct answer *"
        ws['C1'] = "Alternate correct answer"
        ws['D1'] = "Alternate correct answer 2"
        ws['E1'] = "Alternate correct answer 3"
        ws['F1'] = "Alternate correct answer 4"
        ws['G1'] = "Feedback"
        ws['H1'] = "Subcategory"
        for row in ws['A1':'H1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
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
