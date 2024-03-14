import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog, messagebox
from enum import Enum

from MoodleObjects import MultipleChoiceArray, TrueFalseArray, NumericArray, OneAnswerArray
from misc import ProjectPaths, FileUtils, ExplorerOpen
from excel import ExcelExtractor, ExcelCreator


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
        self.__excel_file_path_string_variable = tk.StringVar(master=self.root, value=self.excel_file_shorten_path)
        self.__excel_folder_path_string_variable = tk.StringVar(master=self.root, value=self.excel_folder_shorten_path)
        self.__multiple_choice_questions_string_variable = tk.StringVar(master=self.root, value="Multiple choice\t0/0")
        self.__true_false_questions_string_variable = tk.StringVar(master=self.root, value="True / false\t0/0")
        self.__numeric_questions_string_variable = tk.StringVar(master=self.root, value="Numeric\t\t0/0")
        self.__one_answer_questions_string_variable = tk.StringVar(master=self.root, value="One answer\t0/0")
        self.__numeric_questions = {'successful': 0,
                                    'failed': 0,
                                    'questions_txt': ""}
        self.__true_false_questions = {'successful': 0,
                                       'failed': 0,
                                       'questions_txt': ""}
        self.__multiple_choice_questions = {'successful': 0,
                                            'failed': 0,
                                            'questions_txt': ""}
        self.__one_answer_questions = {'successful': 0,
                                       'failed': 0,
                                       'questions_txt': ""}

    @property
    def excel_folder_path(self):
        return self.__excel_path

    @excel_folder_path.setter
    def excel_folder_path(self, value):
        self.__excel_path = value

    @property
    def excel_filename(self):
        return self.__excel_filename

    @excel_filename.setter
    def excel_filename(self, value):
        self.__excel_filename = value

    @property
    def excel_file_shorten_path(self):
        return FileUtils.crop_path_folders(os.path.join(self.excel_folder_path, self.excel_filename), 3)

    @property
    def excel_folder_shorten_path(self):
        return FileUtils.crop_path_folders(self.excel_folder_path, 3)

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
        create_excel_tab = tk.Frame(notebook, padx=10)
        extract_excel_tab = tk.Frame(notebook, padx=10)
        # help_tab = tk.Frame(notebook) # Maybe later

        # Añadir las pestañas al notebook
        notebook.add(create_excel_tab, text="Create excel")
        notebook.add(extract_excel_tab, text="Extract excel")
        notebook.bind("<<NotebookTabChanged>>", lambda _:self.update_text_variables())
        #notebook.add(help_tab, text="Help") # Maybe later
        notebook.pack(fill=tk.BOTH, expand=True)

        # Creación de los frames de cada pestaña
        self.create_create_excel_frame(create_excel_tab)
        self.create_extract_excel_frame(extract_excel_tab)

        # Mostrar la ventana principal
        self.root.mainloop()

    def create_create_excel_frame(self, create_excel_tab):
        # Frame izquierdo
        first_tab_left_frame = ttk.Frame(create_excel_tab)
        first_tab_left_frame.pack(side="left", fill=tk.BOTH, expand=True, pady=10)
        # Frame central
        first_tab_center_frame = ttk.Frame(create_excel_tab)
        first_tab_center_frame.pack(side="left", fill=tk.BOTH, expand=True, pady=10)
        # Frame derecho
        first_tab_right_frame = ttk.Frame(create_excel_tab)
        first_tab_right_frame.pack(side="left", fill=tk.BOTH, expand=True, pady=10)

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

        multiple_choice_var = tk.BooleanVar()
        true_false_var = tk.BooleanVar()
        numeric_var = tk.BooleanVar()
        one_answer_var = tk.BooleanVar()
        demo_data_var = tk.BooleanVar()

        first_tab_left_frame_title = ttk.Label(first_tab_left_frame_subframe_1, text="Question types")
        first_tab_left_frame_title.pack(anchor="w")

        first_tab_left_frame_option_1 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="Multiple choice",
                                                       variable=multiple_choice_var)
        first_tab_left_frame_option_1.pack(anchor="w")

        first_tab_left_frame_option_2 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="True / false",
                                                       variable=true_false_var)
        first_tab_left_frame_option_2.pack(anchor="w")

        first_tab_left_frame_option_3 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="Numeric",
                                                       variable=numeric_var)
        first_tab_left_frame_option_3.pack(anchor="w")

        first_tab_left_frame_option_4 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="One answer",
                                                       variable=one_answer_var)
        first_tab_left_frame_option_4.pack(anchor="w")

        first_tab_center_frame_title_1 = ttk.Label(first_tab_center_frame_subframe_1, text="Demo data")
        first_tab_center_frame_title_1.pack(anchor="w")

        first_tab_center_frame_option_1 = tk.Checkbutton(first_tab_center_frame_subframe_1, text="Include demo data",
                                                         variable=demo_data_var)
        first_tab_center_frame_option_1.pack(anchor="w")

        first_tab_center_frame_title_2 = ttk.Label(first_tab_center_frame_subframe_2, text="File path")
        first_tab_center_frame_title_2.pack(anchor="w")

        first_tab_center_frame_text_block = ttk.Label(first_tab_center_frame_subframe_2,
                                                      textvariable=self.__excel_folder_path_string_variable)
        first_tab_center_frame_text_block.pack(fill=tk.BOTH, expand=True)

        first_tab_center_frame_button = ttk.Button(first_tab_center_frame_subframe_2, text="Browse",
                                                   command=lambda: self.browse_folder())
        first_tab_center_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        first_tab_center_frame_button = ttk.Button(first_tab_center_frame_subframe_2, text="Open folder",
                                                   command=lambda: self.open_function())
        first_tab_center_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        first_tab_right_frame_success_message = ttk.Label(first_tab_right_frame, text="")
        first_tab_right_frame_button = ttk.Button(first_tab_right_frame, text="Create excel",
                                                  command=lambda: self.create_excel_file(demo_data_var.get(),
                                                                                         multiple_choice_var.get(),
                                                                                         true_false_var.get(),
                                                                                         numeric_var.get(),
                                                                                         one_answer_var.get()))
        first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        first_tab_right_frame_success_message.pack(anchor="center")

    def create_extract_excel_frame(self, extract_excel_tab):
        # Frame izquierdo
        first_tab_left_frame = ttk.Frame(extract_excel_tab)
        first_tab_left_frame.pack(side="left", fill=tk.BOTH, expand=True, pady=10)
        # Frame central
        first_tab_center_frame = ttk.Frame(extract_excel_tab)
        first_tab_center_frame.pack(side="left", fill=tk.BOTH, expand=True, pady=10)
        # Frame derecho
        first_tab_right_frame = ttk.Frame(extract_excel_tab)
        first_tab_right_frame.pack(side="left", fill=tk.BOTH, expand=True, pady=10)

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

        first_tab_left_frame_text_block = ttk.Label(first_tab_left_frame_subframe_1, textvariable=self.__excel_file_path_string_variable)
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

        first_tab_center_frame_option_2 = tk.Label(first_tab_center_frame_subframe_2, textvariable=self.__true_false_questions_string_variable)
        first_tab_center_frame_option_2.pack(anchor="w")

        first_tab_center_frame_option_3 = tk.Label(first_tab_center_frame_subframe_2, textvariable=self.__numeric_questions_string_variable)
        first_tab_center_frame_option_3.pack(anchor="w")

        first_tab_center_frame_option_4 = tk.Label(first_tab_center_frame_subframe_2, textvariable=self.__one_answer_questions_string_variable)
        first_tab_center_frame_option_4.pack(anchor="w")

        first_tab_center_frame_option_5 = tk.Label(first_tab_center_frame_subframe_2, text="")
        first_tab_center_frame_option_5.pack(anchor="w", pady=10)

        first_tab_right_frame_button = ttk.Button(first_tab_right_frame, text="Create GIFT")
        first_tab_right_frame_button.config(state="disabled", command=lambda: self.export_to_gift())
        first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    def update_text_variables(self):
        self.__excel_folder_path_string_variable.set(self.excel_folder_shorten_path)
        self.__excel_file_path_string_variable.set(self.excel_file_shorten_path)

    def browse_file(self, enable_button: ttk.Button):
        file_path = os.path.join(self.__excel_path, self.__excel_filename)
        file = filedialog.askopenfile(mode='r', filetypes=[("Excel files", "*.xlsx")], initialdir=self.excel_folder_path)
        self.excel_folder_path = os.path.normpath(os.path.dirname(file.name))
        self.excel_filename = os.path.basename(file.name)
        self.__excel_file_path_string_variable.set(self.excel_file_shorten_path)
        enable_button.config(state="normal")

    def browse_folder(self):
        text = filedialog.askdirectory(initialdir=self.excel_folder_path)
        self.excel_folder_path = os.path.normpath(text)
        self.__excel_folder_path_string_variable.set(self.excel_folder_shorten_path)

    def extract_excel(self, enable_button: ttk.Button):
        if not os.path.isfile(os.path.join(self.excel_folder_path, self.excel_filename)):
            return
        try:
            excel = ExcelExtractor(os.path.join(self.excel_folder_path, self.excel_filename))
        except Exception as e:
            messagebox.showerror("Error", f"There's been an error with the file: {e.__str__()} ")
            return
        excel_questions = excel.extract_questions_from_workbook()
        if "Multiple choice" in excel_questions:
            multiple_choice_array = MultipleChoiceArray(excel_questions["Multiple choice"])
            self.__multiple_choice_questions['successful'] = multiple_choice_array.successful_answers
            self.__multiple_choice_questions['failed'] = multiple_choice_array.failed_answers
            self.__multiple_choice_questions['questions_txt'] = multiple_choice_array.print_all_questions()
            self.update_text_variable(QuestionTypes.MULTIPLE_CHOICE)
        if not excel_questions["Numeric"] is None:
            numeric_array = NumericArray(excel_questions["Numeric"])
            self.__numeric_questions['successful'] = numeric_array.successful_answers
            self.__numeric_questions['failed'] = numeric_array.failed_answers
            self.__numeric_questions['questions_txt'] = numeric_array.print_all_questions()
            self.update_text_variable(QuestionTypes.NUMERIC)
        if not excel_questions["One answer"] is None:
            one_answer_array = OneAnswerArray(excel_questions["One answer"])
            self.__one_answer_questions['successful'] = one_answer_array.successful_answers
            self.__one_answer_questions['failed'] = one_answer_array.failed_answers
            self.__one_answer_questions['questions_txt'] = one_answer_array.print_all_questions()
            self.update_text_variable(QuestionTypes.ONE_ANSWER)
        if not excel_questions["True_false"] is None:
            true_false_array = TrueFalseArray(excel_questions["True_false"])
            self.__true_false_questions['successful'] = true_false_array.successful_answers
            self.__true_false_questions['failed'] = true_false_array.failed_answers
            self.__true_false_questions['questions_txt'] = true_false_array.print_all_questions()
            self.update_text_variable(QuestionTypes.TRUE_FALSE)
        enable_button.config(state="normal")
        messagebox.showinfo("Excel extracted", "Excel has been extracted. You can check the output to see how many questions can be created.")

    def open_function(self):
        ExplorerOpen.open_folder(self.excel_folder_path)

    def create_excel_file(self, has_demo_data, create_multiple_choice, create_true_false, create_numeric, create_one_answer):
        try:
            excel_file = ExcelCreator(folder_path=self.excel_folder_path,
                                      demo_data=has_demo_data,
                                      create_multiple_choice=create_multiple_choice,
                                      create_numeric=create_numeric,
                                      create_one_answer=create_one_answer,
                                      create_true_false=create_true_false)
            excel_file.save_excel_file()
            messagebox.showinfo("Excel created",
                                "Excel has been created. You open the folder and edit it with your exam questions.")
        except:
            messagebox.showerror("Error in creation",
                                 "There's been an error in the creation of the excel file. Please try again.")


    def export_to_gift(self):
        answer = []
        if self.__true_false_questions['questions_txt'] != "":
            answer.append(self.__true_false_questions['questions_txt'])
        if self.__multiple_choice_questions['questions_txt'] != "":
            answer.append(self.__multiple_choice_questions['questions_txt'])
        if self.__numeric_questions['questions_txt'] != "":
            answer.append(self.__numeric_questions['questions_txt'])
        if self.__one_answer_questions['questions_txt'] != "":
            answer.append(self.__one_answer_questions['questions_txt'])
        if len(answer) > 0:
            FileUtils.create_txt_file(os.path.join(self.__excel_path,"answers.txt"), "\n".join(answer))
            messagebox.showinfo("GIFT created",
                                "Gift file created! Now you can import it on moodle")
            self.open_function()


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
