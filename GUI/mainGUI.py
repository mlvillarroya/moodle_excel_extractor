import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

from misc import ProjectPaths, FileUtils
from GUI import create_excel_frame, create_excel_file, browse_folder, browse_file

class ExcelGUI:
    def __init__(self):
        self.__excel_path = ProjectPaths.get_output_path()
        self.__excel_filename = ""
        self.root = tk.Tk()
        self.__excel_path_string_variable = tk.StringVar(master=self.root, value=self.excel_shorten_path)

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
        return FileUtils.crop_path_folders(self.__excel_path, 2)

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

        first_tab_left_frame_button = ttk.Button(first_tab_left_frame_subframe_1, text="Browse", command=lambda: self.browse_file())
        first_tab_left_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
        first_tab_left_frame_button = ttk.Button(first_tab_left_frame_subframe_1, text="Open", command=lambda: self.open_function())
        first_tab_left_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

        first_tab_left_frame_title_1 = ttk.Label(first_tab_left_frame_subframe_2, text="Analyze data")
        first_tab_left_frame_title_1.pack(anchor="w")

        first_tab_left_frame_option_1 = ttk.Button(first_tab_left_frame_subframe_2, text="Analyze")
        first_tab_left_frame_option_1.pack(padx=10, pady=5)


        first_tab_center_frame_title = ttk.Label(first_tab_center_frame_subframe_1, text="Output")
        first_tab_center_frame_title.pack(anchor="w")

        first_tab_center_frame_option_1 = tk.Label(first_tab_center_frame_subframe_2, text="Multiple choice\t0/0")
        first_tab_center_frame_option_1.pack(anchor="w")

        first_tab_center_frame_option_2 = tk.Label(first_tab_center_frame_subframe_2, text="True / false\t0/0")
        first_tab_center_frame_option_2.pack(anchor="w")

        first_tab_center_frame_option_3 = tk.Label(first_tab_center_frame_subframe_2, text="Numeric\t\t0/0")
        first_tab_center_frame_option_3.pack(anchor="w")

        first_tab_center_frame_option_4 = tk.Label(first_tab_center_frame_subframe_2, text="One answer\t0/0")
        first_tab_center_frame_option_4.pack(anchor="w")

        first_tab_center_frame_option_5 = tk.Label(first_tab_center_frame_subframe_2, text="")
        first_tab_center_frame_option_5.pack(anchor="w", pady=10)

        first_tab_right_frame_success_message = ttk.Label(first_tab_right_frame, text="")
        first_tab_right_frame_button = ttk.Button(first_tab_right_frame, text="Create GIFT")
        first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        first_tab_right_frame_success_message.pack(anchor="center")

    def browse_file(self):
        file_path = os.path.join(self.__excel_path, self.__excel_filename)
        file = filedialog.askopenfile(mode='r', filetypes=[("Excel files", "*.xlsx")], initialdir=self.excel_path)
        self.excel_path = os.path.normpath(os.path.dirname(file.name))
        self.excel_filename = os.path.basename(file.name)
        self.__excel_path_string_variable.set(self.excel_shorten_path)
        pass

    def open_function(self):
        os.startfile(self.excel_path)

    def __parent_folder(original_path):
        if os.path.isdir(original_path):
            return original_path
        else:
            return os.path.dirname(original_path)