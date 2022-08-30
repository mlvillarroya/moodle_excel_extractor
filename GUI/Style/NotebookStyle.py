from tkinter import ttk

def createNotebookStyle(style):
    style.theme_create("NotebookStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [5] } },
            "TNotebook.Tab": {"configure": {"padding": [5, 5] ,
                                            "font" : ('Calibri', '15', 'normal')},
                                "map": {"background": [("selected", "#727a75"), 
                                                        ("active", "#c2d1c8")],
                                        "foreground": [("selected", "#ffffff"),
                                                        ("active", "#000000")]
                                        }}
            })
    style.theme_use("NotebookStyle")