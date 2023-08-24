"""Class for answers"""

class Answer:
    """Class for answers"""
    def __init__(self, answer, feedback='', value='0', numeric_tolerance="0"):
        if answer is None:
            raise ValueError("Value cannot be null")
        self.__answer = answer
        self.__feedback = feedback
        self.__value = value
        self.__numeric_tolerance = numeric_tolerance

    @property
    def answer(self):
        """Property: answer"""
        return self.__answer

    @property
    def feedback(self):
        """Property: feedback"""
        return self.__feedback

    @property
    def value(self):
        """Property: value"""
        return self.__value

    @property
    def numeric_tolerance(self):
        """Property: numeric tolerance"""
        return self.__numeric_tolerance
