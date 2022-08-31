from tkinter import ttk

def ConfigureGuiStyle():
    style = ttk.Style()

    # Generic style for notebooks
    # style.configure('TNotebook.Tab', background="Red")
    # style.map("TNotebook", background= [("selected", "red")])
    # style.map('TNotebook.Tab', 
    #           background=[('selected','#727a75'),('active','#c2d1c8"')],
    #           foreground=[('selected','#ffffff'),('active','#000000"')])
    style.theme_create("NotebookStyle", parent="alt", settings={
            "TNotebook": {"configure": {"tabmargins": [0,5,5,1],
                                        "background": "gray"} },   
            "TNotebook.Tab": {"configure": {"padding": [25, 5] ,
                                            "font" : ('Calibri', '15', 'normal')},
                                "map": {"background": [("selected", "#641c34"), 
                                                        ("active", "#c2d1c8")],
                                        "foreground": [("selected", "#ffffff"),
                                                        ("active", "#000000")]
                                        }},
            "customFrame.TFrame": {"configure": {"background": "red"}},
            "selectorTitle.TLabel": {"configure": {"font" : ('Calibri', '20', 'bold')}},
            "TCheckbutton": {"configure": {"font" : ('Calibri', '15', 'normal')}},
            "TButton": {"configure" : {"foreground": "white",
                                              "background": "#2980b9",
                                              "padding": [10],
                                              'font': "Verdana 12 "},
                                "map" : {"foreground" : [('active', '!disabled', 'white'),('!active','!disabled','white'),('disabled','gray')],
                                         "background" : [('active', '#6c25be'),('disabled','#bea925')]}}
            })
    style.theme_use("NotebookStyle")
