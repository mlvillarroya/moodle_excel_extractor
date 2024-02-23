from excel import ExcelCreator, ExcelExtractor
from MoodleObjects import MultipleChoiceArray, NumericArray, OneAnswerArray, TrueFalseArray
from misc import FileUtils

# create a demo excel file
# excel_file = ExcelCreator(demo_data=True,
#                           create_multiple_choice=True,
#                           create_numeric=True,
#                           create_one_answer=True,
#                           create_true_false=True)
# excel_file.save_excel_file()
#
# # extract questions from the demo excel file
# excel_extractor = ExcelExtractor(excel_file.full_path)
# excel_questions = excel_extractor.extract_questions_from_workbook()
#
# # excel_questions is a dictionary. Each one of the keys to an object
# array_of_answers = []
# if "Multiple choice" in excel_questions:
#     multiple_choice_array = MultipleChoiceArray(excel_questions["Multiple choice"])
#     array_of_answers.append(multiple_choice_array)
# if "Numeric" in excel_questions:
#     numeric_array = NumericArray(excel_questions["Numeric"])
#     array_of_answers.append(numeric_array)
# if "One answer" in excel_questions:
#     one_answer_array = OneAnswerArray(excel_questions["One answer"])
#     array_of_answers.append(one_answer_array)
# if "True_false" in excel_questions:
#     true_false_array = TrueFalseArray(excel_questions["True_false"])
#     array_of_answers.append(true_false_array)
#
# answer = []
# for element in array_of_answers:
#     answer.append(element.print_all_questions())
#
# FileUtils.create_txt_file("answers.txt", "\n".join(answer))

# GUI creation

import tkinter as tk
import tkinter.ttk as ttk

# Creación de la ventana principal
root = tk.Tk()
root.title("Excel creator")
root.geometry("500x204")

# Creación del frame principal
main_frame = tk.Frame(root, padx=10, pady=0)
main_frame.pack(fill=tk.BOTH, expand=True)
# Asignar el mismo peso a cada columna del frame principal

notebook = ttk.Notebook(main_frame)
# Creación de las pestañas
create_excel_tab = tk.Frame(notebook)
extract_excel_tab = tk.Frame(notebook)
help_tab = tk.Frame(notebook)

# Añadir las pestañas al notebook

notebook.add(create_excel_tab, text="Create excel", padding=20)
notebook.add(extract_excel_tab, text="Extract excel")
notebook.add(help_tab, text="Help")
notebook.pack(fill=tk.BOTH, expand=True)

# Diseño de la primera pestaña
# Hay un frame con el título y otro frame con dos subframes

# Frame izquierdo
first_tab_left_frame = tk.Frame(create_excel_tab)
first_tab_left_frame.pack(side="left", fill=tk.BOTH, expand=True)
# Frame derecho
first_tab_center_frame = tk.Frame(create_excel_tab)
first_tab_center_frame.pack(side="right", fill=tk.BOTH, expand=True)

# El frame izquierdo tiene tres frames dentro
first_tab_left_frame_subframe_1 = tk.Frame(first_tab_left_frame)
first_tab_left_frame_subframe_2 = tk.Frame(first_tab_left_frame)

first_tab_left_frame_subframe_1.pack(fill=tk.BOTH, expand=True)
first_tab_left_frame_subframe_2.pack(fill=tk.BOTH, expand=True)

# El frame derecho tiene tres frames dentro
first_tab_center_frame_subframe_1 = tk.Frame(first_tab_center_frame)
first_tab_center_frame_subframe_2 = tk.Frame(first_tab_center_frame)

first_tab_center_frame_subframe_1.pack(fill=tk.BOTH, expand=True)
first_tab_center_frame_subframe_2.pack(fill=tk.BOTH, expand=True)

is_multiple_choice = tk.BooleanVar()
is_true_false = tk.BooleanVar()
is_numeric = tk.BooleanVar()
is_one_answer = tk.BooleanVar()
is_demo_data = tk.BooleanVar()

first_tab_left_frame_title = tk.Label(first_tab_left_frame_subframe_1, text="Question types")
first_tab_left_frame_title.pack(anchor="w")

first_tab_left_frame_option_1 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="Multiple choice", variable=is_multiple_choice)
first_tab_left_frame_option_1.pack(anchor="w")

first_tab_left_frame_option_2 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="True / false", variable=is_true_false)
first_tab_left_frame_option_2.pack(anchor="w")

first_tab_left_frame_option_3 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="Numeric", variable=is_numeric)
first_tab_left_frame_option_3.pack(anchor="w")

first_tab_left_frame_option_4 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="One answer 4", variable=is_one_answer)
first_tab_left_frame_option_4.pack(anchor="w")

first_tab_center_frame_title_1 = tk.Label(first_tab_center_frame_subframe_1, text="Demo data")
first_tab_center_frame_title_1.pack(anchor="w")

first_tab_center_frame_option_1 = tk.Checkbutton(first_tab_center_frame_subframe_1, text="Include demo data", variable=is_demo_data)
first_tab_center_frame_option_1.pack(anchor="w")

first_tab_center_frame_title_2 = tk.Label(first_tab_center_frame_subframe_2, text="File path")
first_tab_center_frame_title_2.pack(anchor="w")

first_tab_center_frame_text_block = tk.Entry(first_tab_center_frame_subframe_2)
first_tab_center_frame_text_block.pack(fill=tk.BOTH, expand=True)

first_tab_center_frame_button = tk.Button(first_tab_center_frame_subframe_2, text="Browse")
first_tab_center_frame_button.pack(fill=tk.BOTH, expand=True, padx=10)

# Ejecución de la ventana principal
root.mainloop()