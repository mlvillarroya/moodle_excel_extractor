from tkinter import ttk

class CreateInstructionsFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        # main frame: two rows (selector and buttons)
        self.rowconfigure(0, weight = 1)
        self.columnconfigure(0, weight = 1)

        outputFrame = ttk.Frame(self)
        outputFrame.rowconfigure(0, weight=1)
        outputFrame.grid(row=0, column=0)
        outputText = ttk.Label(outputFrame,
                               style="instructionsFont.TLabel",
                               text=" 1 - Generate Excel workbook with the needed sheets.\n \
2 - Fill the workbook with the questions. Fields with (*) are mandatory.\n \
3 - Import the workbook and generate a GIFT .txt file.\n \
4 - Use the GIFT .txt file to import directly to Moodle")
        outputText.grid()
