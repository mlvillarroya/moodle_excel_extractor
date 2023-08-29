"""Testing ExcelCreator class"""
from pathlib import Path
import os
from excel.ExcelCreator import ExcelCreator

def test_excel_creator_ok():
    """Testing the object creation"""
    excel = ExcelCreator()
    assert excel.filename == 'MoodleExcel.xlsx'
    assert excel.path == str(Path().resolve())
    assert excel.workbook is not None

def test_excel_creator_file_creates_removes_ok():
    """Testing file creation"""
    excel = ExcelCreator()
    excel.save_excel_file()
    assert os.path.isfile(os.path.join(excel.path,excel.filename))
    excel.remove_excel_file()
    assert os.path.isfile(os.path.join(excel.path,excel.filename)) is False

def test_excel_creator_settings_sheet_creates_ok():
    "Testing excel and settings sheet creation"
    excel = ExcelCreator()
    settings_sheet = excel.workbook.get_sheet_by_name("Settings")
    assert settings_sheet is not None
    assert settings_sheet['A1'].value == "Subject name"
    assert settings_sheet['B1'].value == "Chapter name"
    assert settings_sheet['E1'].value == "* Mandatory Fields"

def test_excel_creator_settings_sheet_demo_data_creates_ok():
    "Testing demo data in settings sheet creation"
    excel = ExcelCreator(demo_data=True)
    settings_sheet = excel.workbook.get_sheet_by_name("Settings")
    assert settings_sheet is not None
    assert settings_sheet['A2'].value == "SMX_M03"
    assert settings_sheet['B2'].value == "Word processor"

def test_excel_creator_mc_sheet_creates_ok():
    "Testing excel and mc sheet creation"
    excel = ExcelCreator(create_multiple_choice= True)
    mc_sheet = excel.workbook.get_sheet_by_name("Multiple choice")
    assert mc_sheet is not None
    assert mc_sheet['A1'].value == "Question *"
    assert mc_sheet['B1'].value == "Correct answer *"
    assert mc_sheet['C1'].value == "Incorrect answer 1 *"
    assert mc_sheet['D1'].value == "Incorrect answer 2"
    assert mc_sheet['E1'].value == "Incorrect answer 3"
    assert mc_sheet['F1'].value == "Incorrect answer 4"
    assert mc_sheet['G1'].value == "Bad answer points"
    assert mc_sheet['H1'].value == "Feedback"
    assert mc_sheet['I1'].value == "Subcategory"

def test_excel_creator_mc_sheet_demo_data_creates_ok():
    """Testing mc demo data creation"""
    excel = ExcelCreator(create_multiple_choice= True, demo_data= True)
    mc_sheet = excel.workbook.get_sheet_by_name("Multiple choice")
    assert mc_sheet is not None
    assert mc_sheet['A2'].value == "Meaning of CPU?"
    assert mc_sheet['B2'].value == "Control process unit"
    assert mc_sheet['C2'].value == "Carpenter public uniform"
    assert mc_sheet['D2'].value == "Car pen use"
    assert mc_sheet['E2'].value == "Coconut private use"
    assert mc_sheet['F2'].value == "Cardigan pickle uniform"
    assert mc_sheet['G2'].value == "-30"
    assert mc_sheet['H2'].value == "That's an important question"
    assert mc_sheet['I2'].value == "Processing"

def test_excel_creator_oa_sheet_creates_ok():
    "Testing excel and oa sheet creation"
    excel = ExcelCreator(create_one_answer= True)
    mc_sheet = excel.workbook.get_sheet_by_name("One answer")
    assert mc_sheet is not None
    assert mc_sheet['A1'].value == "Question *"
    assert mc_sheet['B1'].value == "Correct answer *"
    assert mc_sheet['C1'].value == "Alternate correct answer"
    assert mc_sheet['D1'].value == "Alternate correct answer 2"
    assert mc_sheet['E1'].value == "Alternate correct answer 3"
    assert mc_sheet['F1'].value == "Alternate correct answer 4"
    assert mc_sheet['G1'].value == "Feedback"
    assert mc_sheet['H1'].value == "Subcategory"

def test_excel_creator_oa_demo_data_creates_ok():
    "Testing oa sheet demo data creation"
    excel = ExcelCreator(create_one_answer= True, demo_data= True)
    mc_sheet = excel.workbook.get_sheet_by_name("One answer")
    assert mc_sheet is not None
    assert mc_sheet['A2'].value == "Acronym of the Federal Bureau of Investigation?"
    assert mc_sheet['B2'].value == "FBI"
    assert mc_sheet['C2'].value == "fbi"
    assert mc_sheet['D2'].value == "Fbi"
    assert mc_sheet['E2'].value == "fBi"
    assert mc_sheet['F2'].value == "fbI"
    assert mc_sheet['G2'].value == "That's an important question"
    assert mc_sheet['H2'].value == "Society"

def test_excel_creator_tf_sheet_creates_ok():
    "Testing excel and tf sheet creation"
    excel = ExcelCreator(create_true_false= True)
    tf_sheet = excel.workbook.get_sheet_by_name("True_False")
    assert tf_sheet is not None
    assert tf_sheet['A1'].value == "Question *"
    assert tf_sheet['B1'].value == "True (T) or False (F)? *"
    assert tf_sheet['C1'].value == "Feedback"
    assert tf_sheet['D1'].value == "Subcategory"

def test_excel_creator_tf_sheet_demo_data_creates_ok():
    "Testing tf sheet demo data creation"
    excel = ExcelCreator(create_true_false= True, demo_data= True)
    tf_sheet = excel.workbook.get_sheet_by_name("True_False")
    assert tf_sheet is not None
    assert tf_sheet['A2'].value == "RAM is volatile"
    assert tf_sheet['B2'].value == "T"
    assert tf_sheet['C2'].value == "RAM is volatile memory used to hold instructions and data of currently running programs. It loses integrity after loss of power."
    assert tf_sheet['D2'].value == "Memory"

def test_excel_creator_numeric_sheet_creates_ok():
    "Testing excel and numeric sheet creation"
    excel = ExcelCreator(create_numeric= True)
    numeric_sheet = excel.workbook.get_sheet_by_name("Numeric")
    assert numeric_sheet is not None
    assert numeric_sheet['A1'].value == "Question *"
    assert numeric_sheet['B1'].value == "Correct numeric value *"
    assert numeric_sheet['C1'].value == "Numeric tolerance *"
    assert numeric_sheet['D1'].value == "Feedback"
    assert numeric_sheet['E1'].value == "Subcategory"

def test_excel_creator_numeric_sheet_demo_data_creates_ok():
    "Testing numeric sheet demo data creation"
    excel = ExcelCreator(create_numeric= True, demo_data= True)
    numeric_sheet = excel.workbook.get_sheet_by_name("Numeric")
    assert numeric_sheet is not None
    assert numeric_sheet['A2'].value == "Value of Pi?"
    assert numeric_sheet['B2'].value == "3.14"
    assert numeric_sheet['C2'].value == "0.01"
    assert numeric_sheet['D2'].value == "Value of Pi is 3.141592653589793238"
    assert numeric_sheet['E2'].value == "Math"
