import tkinter as tk
import tkinter.ttk as ttk
from misc import ProjectPaths


def create_excel_frame(create_excel_tab, browse_function, open_function, create_excel_function):
    # Frame izquierdo
    first_tab_left_frame = ttk.Frame(create_excel_tab)
    first_tab_left_frame.pack(side="left", fill=tk.BOTH, expand=True)
    # Frame central
    first_tab_center_frame = ttk.Frame(create_excel_tab)
    first_tab_center_frame.pack(side="left", fill=tk.BOTH, expand=True)
    # Frame derecho
    first_tab_right_frame = ttk.Frame(create_excel_tab)
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

    first_tab_left_frame_title = ttk.Label(first_tab_left_frame_subframe_1, text="Question types")
    first_tab_left_frame_title.pack(anchor="w")

    first_tab_left_frame_option_1 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="Multiple choice", variable=multiple_choice_var)
    first_tab_left_frame_option_1.pack(anchor="w")

    first_tab_left_frame_option_2 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="True / false", variable=true_false_var)
    first_tab_left_frame_option_2.pack(anchor="w")

    first_tab_left_frame_option_3 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="Numeric", variable=numeric_var)
    first_tab_left_frame_option_3.pack(anchor="w")

    first_tab_left_frame_option_4 = tk.Checkbutton(first_tab_left_frame_subframe_2, text="One answer 4", variable=one_answer_var)
    first_tab_left_frame_option_4.pack(anchor="w")

    first_tab_center_frame_title_1 = ttk.Label(first_tab_center_frame_subframe_1, text="Demo data")
    first_tab_center_frame_title_1.pack(anchor="w")

    first_tab_center_frame_option_1 = tk.Checkbutton(first_tab_center_frame_subframe_1, text="Include demo data", variable=demo_data_var)
    first_tab_center_frame_option_1.pack(anchor="w")

    first_tab_center_frame_title_2 = ttk.Label(first_tab_center_frame_subframe_2, text="File path")
    first_tab_center_frame_title_2.pack(anchor="w")

    first_tab_center_frame_text_block = ttk.Label(first_tab_center_frame_subframe_2, text=ProjectPaths.get_output_path())
    first_tab_center_frame_text_block.pack(fill=tk.BOTH, expand=True)

    first_tab_center_frame_button = ttk.Button(first_tab_center_frame_subframe_2, text="Browse", command=lambda: browse_function(first_tab_center_frame_text_block))
    first_tab_center_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)
    first_tab_center_frame_button = ttk.Button(first_tab_center_frame_subframe_2, text="Open folder", command=lambda: open_function(first_tab_center_frame_text_block.cget("text")))
    first_tab_center_frame_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=5)

    first_tab_right_frame_success_message = ttk.Label(first_tab_right_frame, text="")
    first_tab_right_frame_button = ttk.Button(first_tab_right_frame, text="Create excel", command=lambda: create_excel_function(demo_data_var.get(), multiple_choice_var.get(), true_false_var.get(), numeric_var.get(), one_answer_var.get(), first_tab_center_frame_text_block.cget("text"), first_tab_right_frame_success_message))
    first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    first_tab_right_frame_success_message.pack(anchor="center")
