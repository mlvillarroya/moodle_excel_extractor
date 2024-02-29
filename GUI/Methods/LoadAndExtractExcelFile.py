from excel import ExcelExtractor

def extract_excel_file(file_path):
    excel_extractor = ExcelExtractor(file_path)
    excel_questions = excel_extractor.extract_questions_from_workbook()
    return excel_questions