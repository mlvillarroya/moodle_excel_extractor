from excel.ExcelCreator import ExcelCreator, ExcelMode

def test_excel_creator_settings_sheet_creates_ok():
    "Testing excel and settings sheet creation"
    excel = ExcelCreator('', ExcelMode.CREATE)
    workbook = excel.workbook
    settings_sheet = workbook.get_sheet_by_name("Settings")
    assert settings_sheet is not None
    assert settings_sheet['A1'].value == "Subject name"
    assert settings_sheet['B1'].value == "Chapter name"
    assert settings_sheet['E1'].value == "* Mandatory Fields"