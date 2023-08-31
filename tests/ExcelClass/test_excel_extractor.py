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
        extractor = ExcelExtractor(path)
        assert str(exc_info) == "A sheet named Settings is missing. Please, create one"
    ## Remove files
    excel.remove_excel_file()

def test_excel_extractor_extract_questions_ok():
    """Testing the object creation"""
    ## Setup
    folder = "tests"
    filename = "okExcel.xlsx"
    # excel = ExcelCreator(folder, filename, create_multiple_choice= True, demo_data= True)
    # excel.save_excel_file()
    ## Test
    path = os.path.join(folder,filename)
    extractor = ExcelExtractor(path)
    a = extractor.extract_questions()
    ## Remove files
    # excel.remove_excel_file()
    pass