import os
from . import Constants


def get_project_path():
    # Get the current working directory, that is the parent of current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    list_without_current_dir = current_dir.split(os.sep)[:-1]
    path = os.sep.join(list_without_current_dir)
    return path


def get_static_path():
    return os.path.join(get_project_path(), Constants.STATIC_DIR_NAME)


def get_constants_path():
    return os.path.join(get_static_path(), Constants.EXCEL_CREATION_CONSTANTS_FILE)


def get_output_path():
    return os.path.join(get_project_path(), Constants.OUTPUT_DIR_NAME)


def get_tests_path():
    return os.path.join(get_project_path(), "tests")