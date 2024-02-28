import os.path
from tkinter import filedialog


def browse_folder(label_to_change):
    label_to_change.config(text=filedialog.askdirectory(initialdir=label_to_change.cget("text")))


def browse_file(label_to_change):
    original_path = label_to_change.cget("text")
    file = filedialog.askopenfile(mode='r', filetypes=[("Excel files", "*.xlsx")], initialdir=__parent_folder(original_path))
    label_to_change.config(text=file.name)


def __parent_folder(original_path):
    if os.path.isdir(original_path):
        return original_path
    else:
        return os.path.dirname(original_path)