from re import S
from tkinter import ttk

class CreateExcelFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        # main frame: two rows (selector and buttons)
        self.rowconfigure(0, weight = 4)
        self.rowconfigure(1, weight = 1)
        self.columnconfigure(0, weight = 1)
        # selector frame
        sheetChooseFrame = ttk.Frame(self)
        sheetChooseFrame.grid(padx=100, sticky="NSEW")
        selectorTitle = ttk.Label(sheetChooseFrame,text="Create sheet for", style='selectorTitle.TLabel')
        selectorTitle.grid(pady=50)
        multipleChoiceCheckbox = ttk.Checkbutton(sheetChooseFrame,text="Multiple choice")
        multipleChoiceCheckbox.grid(sticky='NW')
        oneAnswerCheckbox = ttk.Checkbutton(sheetChooseFrame,text="One answer")
        oneAnswerCheckbox.grid(sticky='NW')
        numericCheckbox = ttk.Checkbutton(sheetChooseFrame,text="Numeric")
        numericCheckbox.grid(sticky='NW')
        trueFalseCheckbox = ttk.Checkbutton(sheetChooseFrame,text="True / false")
        trueFalseCheckbox.grid(sticky='NW')
        createDemoDataCheckbox = ttk.Checkbutton(sheetChooseFrame, text="Create demo data")
        createDemoDataCheckbox.grid(sticky='NW', pady=50)
        # buttons frame
        buttonsFrame = ttk.Frame(self)
        buttonsFrame.grid(row=1, column=0)
        buttonsFrame.columnconfigure(0, weight = 1)
        buttonsFrame.columnconfigure(1, weight = 1)
        buttonsFrame.columnconfigure(2, weight = 1)
        button = ttk.Button(buttonsFrame, text = "Create file", style = "Custom.TButton")
        button2 = ttk.Button(buttonsFrame, text = "Open file", style = "Custom.TButton")
        button3 = ttk.Button(buttonsFrame, text = "Open folder", style = "Custom.TButton")
        button.grid(row=0,column=0, sticky="NS", padx=25, pady=5)
        button2.grid(row=0,column=1, sticky="NS", padx=25, pady=5)
        button2.state(['disabled'])
        button3.grid(row=0,column=2, sticky="NS", padx=25, pady=5)
        button3.state(['disabled'])