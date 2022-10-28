from tkinter import END, Tk, ttk, IntVar
from tkinter import filedialog
import os
from excel.ExcelCreator import ExcelCreator
from misc.ExplorerOpen import ExplorerOpen

class CreateExcelFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        # main frame: two rows (selector and buttons)
        self.rowconfigure(0, weight = 4)
        self.rowconfigure(1, weight = 3)
        self.rowconfigure(2, weight = 1)
        self.columnconfigure(0, weight = 1)
        self.columnconfigure(1, weight = 1)
        self.columnconfigure(2, weight = 1)
        # selector frame
        multipleChoiceSelected = IntVar()
        oneAnswerSelected = IntVar()
        numericSelected = IntVar()
        trueFalseSelected = IntVar()
        createDemoDataSelected = IntVar()
        sheetChooseFrame = ttk.Frame(self)
        sheetChooseFrame.columnconfigure(0, weight= 1)
        sheetChooseFrame.grid(row=0, column=1, sticky='W')
        selectorTitle = ttk.Label(sheetChooseFrame,text="Create sheet for", style='selectorTitle.TLabel')
        selectorTitle.grid(pady=50, sticky="NW")
        multipleChoiceCheckbox = ttk.Checkbutton(sheetChooseFrame,text="Multiple choice",variable=multipleChoiceSelected)
        multipleChoiceCheckbox.grid(sticky='NW')
        oneAnswerCheckbox = ttk.Checkbutton(sheetChooseFrame,text="One answer", variable=oneAnswerSelected)
        oneAnswerCheckbox.grid(sticky='NW')
        numericCheckbox = ttk.Checkbutton(sheetChooseFrame,text="Numeric", variable = numericSelected)
        numericCheckbox.grid(sticky='NW')
        trueFalseCheckbox = ttk.Checkbutton(sheetChooseFrame,text="True / false", variable = trueFalseSelected)
        trueFalseCheckbox.grid(sticky='NW')
        createDemoDataCheckbox = ttk.Checkbutton(sheetChooseFrame, text="Create demo data", variable = createDemoDataSelected)
        createDemoDataCheckbox.grid(sticky='NW', pady=50)

        def selectFolder(folderNameLabel):
            self.folder = filedialog.askdirectory()
            if self.folder:
              try:
                    folderNameLabel.config(text=getFolderName())
              except:  # <- naked except is a bad idea
                    Tk.showerror("Select folder", "Failed to select folder\n'%s'" % self.folder)
              return
          
        def getFolderName():
            return os.path.basename(os.path.normpath(self.folder))

        def createExcelFile():
            self.template = ExcelCreator(multipleChoiceSelected.get()==1,trueFalseSelected.get()==1,oneAnswerSelected.get()==1,numericSelected.get()==1,self.folder,createDemoDataSelected.get()==1)
            button2.state(['!disabled'])
        
        fileSelectorFrame = ttk.Frame(self)
        fileSelectorFrame.columnconfigure(0, weight=1)
        fileSelectorFrame.grid(row=1, column=1, sticky='W')
        #button to select folder
        self.folder = os.getcwd()
        fileSelectorButton = ttk.Button(fileSelectorFrame, text="Folder", command=lambda:selectFolder(fileSelectorPath))
        fileSelectorButton.grid(row=0,column=0,pady="5")
        #folder name
        fileSelectorPath=ttk.Label(fileSelectorFrame,width="30", text=getFolderName())
        fileSelectorPath.grid(row=0,column=1,sticky="e",padx=10)

        # buttons frame
        buttonsFrame = ttk.Frame(self)
        buttonsFrame.columnconfigure(0, weight = 1)
        buttonsFrame.columnconfigure(1, weight = 1)
        buttonsFrame.grid(row=2, column=0, columnspan=3)
        button = ttk.Button(buttonsFrame, text = "Create file", style = "Custom.TButton", command=lambda:createExcelFile())
        button2 = ttk.Button(buttonsFrame, text = "Open folder", style = "Custom.TButton", command=lambda:ExplorerOpen.ExplorerOpen(self.template.path))
        button.grid(row=0,column=0, sticky="NS", padx=25, pady=5)
        button2.grid(row=0,column=1, sticky="NS", padx=25, pady=5)
        button2.state(['disabled'])        
        
