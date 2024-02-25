import tkinter as tk
import tkinter.ttk as ttk

def create_excel_frame(create_excel_tab):
    # Frame izquierdo
    first_tab_left_frame = tk.Frame(create_excel_tab)
    first_tab_left_frame.pack(side="left", fill=tk.BOTH, expand=True)
    # Frame central
    first_tab_center_frame = tk.Frame(create_excel_tab)
    first_tab_center_frame.pack(side="left", fill=tk.BOTH, expand=True)
    # Frame derecho
    first_tab_right_frame = tk.Frame(create_excel_tab)
    first_tab_right_frame.pack(side="left", fill=tk.BOTH, expand=True)

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
    first_tab_center_frame_button.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    first_tab_right_frame_button = tk.Button(first_tab_right_frame, text="Create excel")
    first_tab_right_frame_button.pack(fill=tk.BOTH, expand=True, padx=20, pady=30)
