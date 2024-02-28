import tkinter as tk
import tkinter.ttk as ttk
from misc import ProjectPaths, FileUtils


def extract_excel_frame(extract_excel_tab, browse_function, open_function, create_gift_function):
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

    multiple_choice_var = tk.BooleanVar()
    true_false_var = tk.BooleanVar()
    numeric_var = tk.BooleanVar()
    one_answer_var = tk.BooleanVar()
    demo_data_var = tk.BooleanVar()

    file_path = ProjectPaths.get_output_path()
    first_tab_left_frame_title_2 = ttk.Label(first_tab_left_frame_subframe_1, text="Filled Excel path")
    first_tab_left_frame_title_2.pack(anchor="w")

    first_tab_left_frame_text_block = ttk.Label(first_tab_left_frame_subframe_1, text=file_path)
    first_tab_left_frame_text_block.pack(fill=tk.BOTH, expand=True)

    first_tab_left_frame_button = ttk.Button(first_tab_left_frame_subframe_1, text="Browse", command=lambda: browse_function(first_tab_left_frame_text_block))
    first_tab_left_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
    first_tab_left_frame_button = ttk.Button(first_tab_left_frame_subframe_1, text="Open", command=lambda: open_function(first_tab_left_frame_text_block.cget("text")))
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
    first_tab_right_frame_button = ttk.Button(first_tab_right_frame, text="Create GIFT", command=lambda: create_gift_function(demo_data_var.get(), multiple_choice_var.get(), true_false_var.get(), numeric_var.get(), one_answer_var.get(), first_tab_center_frame_text_block.cget("text"), first_tab_right_frame_success_message))
    first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    first_tab_right_frame_success_message.pack(anchor="center")
