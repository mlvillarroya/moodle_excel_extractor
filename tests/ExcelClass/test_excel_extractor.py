"""Testing ExcelCreator class"""
from pathlib import Path
import pytest
import os
from excel import ExcelExtractor, ExcelCreator

def test_excel_extractor_ok():
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