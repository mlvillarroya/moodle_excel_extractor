class Answer:
    def __init__(self, answer, feedback='', value='0', numericTolerance="0"):
        if answer is None: raise Exception("Value cannot be null")
        self.answer = answer
        self.feedback = feedback
        self.value= value
        self.numericTolerance= numericTolerance

    