import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog
from enum import Enum

from MoodleObjects import MultipleChoiceArray, TrueFalseArray, NumericArray, OneAnswerArray
from misc import ProjectPaths, FileUtils
from excel import ExcelExtractor


class QuestionTypes(Enum):
    MULTIPLE_CHOICE = "Multiple choice"
    TRUE_FALSE = "True_false"
    NUMERIC = "Numeric"
    ONE_ANSWER = "One answer"


class ExcelGUI:
    def __init__(self):
        self.__excel_path = ProjectPaths.get_output_path()
        self.__excel_filename = ""
        self.root = tk.Tk()
        self.__excel_path_string_variable = tk.StringVar(master=self.root, value=self.excel_shorten_path)
        self.__multiple_choice_questions_string_variable = tk.StringVar(master=self.root, value="Multiple choice\t0/0")
        self.__true_false_questions_string_variable = tk.StringVar(master=self.root, value="True / false\t0/0")
        self.__numeric_questions_string_variable = tk.StringVar(master=self.root, value="Numeric\t\t0/0")
        self.__one_answer_questions_string_variable = tk.StringVar(master=self.root, value="One answer\t0/0")
        self.__numeric_questions = {'successful': 0,
                                    'failed': 0,
                                    'questions': []}
        self.__true_false_questions = {'successful': 0,
                                       'failed': 0,
                                       'questions': []}
        self.__multiple_choice_questions = {'successful': 0,
                                            'failed': 0,
                                            'questions': []}
        self.__one_answer_questions = {'successful': 0,
                                       'failed': 0,
                                       'questions': []}

    @property
    def excel_path(self):
        return self.__excel_path

    @excel_path.setter
    def excel_path(self, value):
        self.__excel_path = value

    @property
    def excel_filename(self):
        return self.__excel_filename

    @excel_filename.setter
    def excel_filename(self, value):
        self.__excel_filename = value

    @property
    def excel_shorten_path(self):
        return FileUtils.crop_path_folders(os.path.join(self.excel_path,self.excel_filename), 3)

    def create_GUI(self):
        # Creación de la ventana principal
        self.root.title("Excel creator")
        self.root.geometry("700x204")

        # Creación del frame principal
        main_frame = tk.Frame(self.root, padx=10, pady=0)
        main_frame.pack(fill=tk.BOTH, expand=True)
        # Asignar el mismo peso a cada columna del frame principal

        notebook = ttk.Notebook(main_frame)
        # Creación de las pestañas
        create_excel_tab = tk.Frame(notebook)
        extract_excel_tab = tk.Frame(notebook)
        help_tab = tk.Frame(notebook)

        # Añadir las pestañas al notebook
        notebook.add(create_excel_tab, text="Create excel")
        notebook.add(extract_excel_tab, text="Extract excel")
        notebook.add(help_tab, text="Help")
        notebook.pack(fill=tk.BOTH, expand=True)

        # Creación de los frames de cada pestaña
        # create_excel_frame(create_excel_tab, browse_folder, open_folder, create_excel_file)
        self.create_extract_excel_frame(create_excel_tab)

        # Mostrar la ventana principal
        self.root.mainloop()

    def create_extract_excel_frame(self, extract_excel_tab):
        #TODO create class and use SELF
        # Frame izquierdo
        first_tab_left_frame = ttk.Frame(extract_excel_tab)
        first_tab_left_frame.pack(side="left", fill=tk.BOTH, expand=True)
        # Frame central
        first_tab_center_frame = ttk.Frame(extract_excel_tab)
        first_tab_center_frame.pack(side="left", fill=tk.BOTH, expand=True)
        # Frame derecho
        first_tab_right_frame = ttk.Frame(extract_excel_tab)
        first_tab_right_frame.pack(side="left", fill=tk.BOTH, expand=True)

        # El frame izquierdo tiene tres frames dentro
        first_tab_left_frame_subframe_1 = ttk.Frame(first_tab_left_frame)
        first_tab_left_frame_subframe_2 = ttk.Frame(first_tab_left_frame)

        first_tab_left_frame_subframe_1.pack(fill=tk.BOTH, expand=True)
        first_tab_left_frame_subframe_2.pack(fill=tk.BOTH, expand=True)

        # El frame derecho tiene tres frames dentro
        first_tab_center_frame_subframe_1 = ttk.Frame(first_tab_center_frame)
        first_tab_center_frame_subframe_2 = ttk.Frame(first_tab_center_frame)

        first_tab_center_frame_subframe_1.pack(fill=tk.BOTH, expand=True)
        first_tab_center_frame_subframe_2.pack(fill=tk.BOTH, expand=True)

        first_tab_left_frame_title_2 = ttk.Label(first_tab_left_frame_subframe_1, text="Filled Excel path")
        first_tab_left_frame_title_2.pack(anchor="w")

        first_tab_left_frame_text_block = ttk.Label(first_tab_left_frame_subframe_1, textvariable=self.__excel_path_string_variable)
        first_tab_left_frame_text_block.pack(fill=tk.BOTH, expand=True)

        first_tab_left_frame_button = ttk.Button(first_tab_left_frame_subframe_1, text="Browse", command=lambda: self.browse_file(first_tab_left_frame_option_1))
        first_tab_left_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        first_tab_left_frame_button = ttk.Button(first_tab_left_frame_subframe_1, text="Open", command=lambda: self.open_function())
        first_tab_left_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        first_tab_left_frame_title_1 = ttk.Label(first_tab_left_frame_subframe_2, text="Analyze data")
        first_tab_left_frame_title_1.pack(anchor="w")

        first_tab_left_frame_option_1 = ttk.Button(first_tab_left_frame_subframe_2, text="Analyze", command=lambda: self.extract_excel(first_tab_right_frame_button))
        first_tab_left_frame_option_1.config(state="disabled")
        first_tab_left_frame_option_1.pack(padx=10, pady=5)


        first_tab_center_frame_title = ttk.Label(first_tab_center_frame_subframe_1, text="Output")
        first_tab_center_frame_title.pack(anchor="w")

        first_tab_center_frame_option_1 = tk.Label(first_tab_center_frame_subframe_2, textvariable=self.__multiple_choice_questions_string_variable)
        first_tab_center_frame_option_1.pack(anchor="w")

        first_tab_center_frame_option_2 = tk.Label(first_tab_center_frame_subframe_2, text="True / false\t0/0")
        first_tab_center_frame_option_2.pack(anchor="w")

        first_tab_center_frame_option_3 = tk.Label(first_tab_center_frame_subframe_2, text="Numeric\t\t0/0")
        first_tab_center_frame_option_3.pack(anchor="w")

        first_tab_center_frame_option_4 = tk.Label(first_tab_center_frame_subframe_2, text="One answer\t0/0")
        first_tab_center_frame_option_4.pack(anchor="w")

        first_tab_center_frame_option_5 = tk.Label(first_tab_center_frame_subframe_2, text="")
        first_tab_center_frame_option_5.pack(anchor="w", pady=10)

        first_tab_right_frame_button = ttk.Button(first_tab_right_frame, text="Create GIFT")
        first_tab_right_frame_button.config(state="disabled")
        first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def browse_file(self, enable_button: ttk.Button):
        file_path = os.path.join(self.__excel_path, self.__excel_filename)
        file = filedialog.askopenfile(mode='r', filetypes=[("Excel files", "*.xlsx")], initialdir=self.excel_path)
        self.excel_path = os.path.normpath(os.path.dirname(file.name))
        self.excel_filename = os.path.basename(file.name)
        self.__excel_path_string_variable.set(self.excel_shorten_path)
        enable_button.config(state="normal")

    def extract_excel(self, enable_button: ttk.Button):
        if not os.path.isfile(os.path.join(self.excel_path,self.excel_filename)):
            return
        excel = ExcelExtractor(os.path.join(self.excel_path,self.excel_filename))
        excel_questions = excel.extract_questions_from_workbook()
        if "Multiple choice" in excel_questions:
            multiple_choice_array = MultipleChoiceArray(excel_questions["Multiple choice"])
            self.__multiple_choice_questions['successful'] = multiple_choice_array.successful_answers
            self.__multiple_choice_questions['failed'] = multiple_choice_array.failed_answers
            self.__multiple_choice_questions['questions'] = multiple_choice_array.question_array
            self.update_text_variable(QuestionTypes.MULTIPLE_CHOICE)
        if not excel_questions["Numeric"] is None:
            numeric_array = NumericArray(excel_questions["Numeric"])
            self.__numeric_questions['successful'] = numeric_array.successful_answers
            self.__numeric_questions['failed'] = numeric_array.failed_answers
            self.__numeric_questions['questions'] = numeric_array.question_array
        if not excel_questions["One answer"] is None:
            one_answer_array = OneAnswerArray(excel_questions["One answer"])
            self.__one_answer_questions['successful'] = one_answer_array.successful_answers
            self.__one_answer_questions['failed'] = one_answer_array.failed_answers
            self.__one_answer_questions['questions'] = one_answer_array.question_array
        if not excel_questions["True_false"] is None:
            true_false_array = TrueFalseArray(excel_questions["True_false"])
            self.__true_false_questions['successful'] = true_false_array.successful_answers
            self.__true_false_questions['failed'] = true_false_array.failed_answers
            self.__true_false_questions['questions'] = true_false_array.question_array
        enable_button.config(state="normal")

    def open_function(self):
        os.startfile(self.excel_path)

    def __parent_folder(original_path):
        if os.path.isdir(original_path):
            return original_path
        else:
            return os.path.dirname(original_path)

    def update_text_variable(self, variable_type: QuestionTypes):
        if variable_type == QuestionTypes.MULTIPLE_CHOICE:
            self.__multiple_choice_questions_string_variable.set("Multiple choice\t{}/{}".format(self.__multiple_choice_questions['successful'], self.__multiple_choice_questions['failed']))
        elif variable_type == QuestionTypes.TRUE_FALSE:
            self.__true_false_questions_string_variable.set("True / false\t{}/{}".format(self.__true_false_questions['successful'], self.__true_false_questions['failed']))
        elif variable_type == QuestionTypes.NUMERIC:
            self.__numeric_questions_string_variable.set("Numeric\t\t{}/{}".format(self.__numeric_questions['successful'], self.__numeric_questions['failed']))
        elif variable_type == QuestionTypes.ONE_ANSWER:
            self.__one_answer_questions_string_variable.set("One answer\t{}/{}".format(self.__one_answer_questions['successful'], self.__one_answer_questions['failed']))
