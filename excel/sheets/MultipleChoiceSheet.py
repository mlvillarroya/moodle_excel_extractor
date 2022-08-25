from openpyxl.comments import Comment
from excel.ExcelCellStyling import ExcelCellStyling

class MultipleChoiceSheet: 
    def createMultipleChoiceSheet(wb):
        ws = wb.create_sheet("Multiple choice")
        ws['A1'] = "Question *"
        ws['B1'] = "Correct answer *"
        ws['C1'] = "Incorrect answer 1 *"
        ws['D1'] = "Incorrect answer 2"
        ws['E1'] = "Incorrect answer 3"
        ws['F1'] = "Incorrect answer 4"
        ws['G1'] = "Bad answer points"
        ws['G1'].comment = Comment("Allowed values, positive or negative are: 100.00000  90.00000  83.33333  80.00000  75.00000  70.00000  66.66667  60.00000  50.00000  40.00000  33.33333  30.00000  25.00000  20.00000  16.66667  14.28571  12.50000  11.11111  10.00000   5.00000","admin",250,200)
        ws['H1'] = "Feedback"
        ws['I1'] = "Subcategory"
        for row in ws['A1':'I1']:
            for cell in row:
                ExcelCellStyling.ChangeCellAlignment(cell,'center','center')
                ExcelCellStyling.ChangeCellBackgroundAndTextColors(cell,'E7AA73','653159')
                ExcelCellStyling.adjustSheetColumnSize(ws,cell.column_letter,18)
                ExcelCellStyling.ApplyFullBorderToCell(cell)
        ExcelCellStyling.adjustSheetRowSize(ws,1,38)
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
