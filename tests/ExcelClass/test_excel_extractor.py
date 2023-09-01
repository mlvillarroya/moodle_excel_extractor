"""Testing ExcelCreator class"""
from pathlib import Path
import pytest
import os
from excel import ExcelExtractor, ExcelCreator

def test_excel_extractor_without_category_ok():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    excel = ExcelCreator(folder, filename)
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    assert extractor is not None
    assert extractor.workbook is not None
    assert extractor.main_category == ''
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_with_category_ok():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    excel = ExcelCreator(folder, filename, demo_data= True)
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    assert extractor is not None
    assert extractor.workbook is not None
    assert extractor.main_category == 'SMX_M03/Word processor'
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_wrong_path_raises_exception():
    """Testing the object creation"""
    with pytest.raises(FileNotFoundError) as exc_info:
        extractor = ExcelExtractor("FakeFile.xlsx")
    assert str(exc_info.value) == "File not found. Please check the path"

def test_excel_extractor_no_settings_sheet_raises_exception():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "errorExcel.xlsx"
    excel = ExcelCreator(folder, filename)
    excel.workbook["Settings"].title = "Wrong sheet"
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    with pytest.raises(KeyError) as exc_info:
        ExcelExtractor(path)
        assert str(exc_info) == "A sheet named Settings is missing. Please, create one"
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_extract_questions_from_sheet_ok():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    excel = ExcelCreator(folder, filename, create_multiple_choice= True, demo_data= True)
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    multiple_choice_questions = extractor.extract_questions_from_sheet("Multiple choice")
    assert multiple_choice_questions is not None
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_extract_questions_from_incorrect_sheet_returns_none():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    excel = ExcelCreator(folder, filename, create_multiple_choice= True, demo_data= True)
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    no_questions = extractor.extract_questions_from_sheet("Fake sheet")
    assert no_questions is None
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_extract_questions_from_sheet_without_mandatory_column_raises_exception():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    excel = ExcelCreator(folder, filename, create_multiple_choice= True, demo_data= True)
    excel.workbook['Multiple choice'].delete_cols(1, 1)
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    with pytest.raises(ValueError) as exc_info:
        extractor.extract_questions_from_sheet("Multiple choice")
        assert str(exc_info) == "Worksheet Multiple choice has not the mandatory columns"
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_extract_questions_from_all_sheets_ok():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    excel = ExcelCreator(folder, filename, create_multiple_choice= True, demo_data= True)
    excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    questions = extractor.extract_questions_from_workbook()
    assert questions is not None
    assert "Multiple choice" in questions.keys()
    assert "True_false" in questions.keys()
    assert "Numeric" in questions.keys()
    assert "One answer" in questions.keys()
    ## Remove files
    excel.remove_excel_file()
