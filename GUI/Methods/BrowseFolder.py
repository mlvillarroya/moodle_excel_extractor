from tkinter import filedialog


def browse_folder(label_to_change):
    label_to_change.config(text=filedialog.askdirectory(initialdir=label_to_change.cget("text")))