from excel import ExcelCreator

def create_excel_file(has_demo_data, create_multiple_choice, create_true_false, create_numeric, create_one_answer, save_path, message_element):
    try:
        excel_file = ExcelCreator(folder_path=save_path,
                                  demo_data=has_demo_data,
                                  create_multiple_choice=create_multiple_choice,
                                  create_numeric=create_numeric,
                                  create_one_answer=create_one_answer,
                                  create_true_false=create_true_false)
        excel_file.save_excel_file()
        message_element.config(text="EXCEL CREATED!")
    except:
        message_element.config(text="ERROR IN CREATION")
