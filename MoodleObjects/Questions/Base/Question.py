
class Question:
    """Generic question class"""
    def __init__(self, category, code, question, answers_list, general_feedback):
        if code is None or \
            question is None or \
            answers_list is None or \
            answers_list[0].value is None:
            raise ValueError('Argument cannot be None')
        self.__category = category
        self.__code = code
        self.__question = question
        self.__answers_list = answers_list
        self.__general_feedback = general_feedback
        self.__feedback = "####" + general_feedback + "\n" if general_feedback else ''
        self.__answer = self.create_answer_from_list()

    @property
    def answers_list(self):
        """Property: answers_list"""
        return self.__answers_list

    @property
    def general_feedback(self):
        """Property: general_feedback"""
        return self.__general_feedback

    @property
    def category(self):
        """Property: category"""
        return self.__category

    @property
    def code(self):
        """Property: code"""
        return self.__code

    @property
    def question(self):
        """Property: question"""
        return self.__question

    @property
    def feedback(self):
        """Property: feedback"""
        return self.__feedback

    @property
    def answers(self):
        """Property: answers"""
        return self.__answer

    def create_question_text(self):
        """Function to create the text for a question"""
        return "::" + self.__code + "::" + self.__question + "{" + "\n" \
                + self.__answer + "\n" \
                + self.__feedback \
                + "}"

    def create_answer_from_list(self):
        """Function to create the answer from a list"""
        return ""

    def print_question(self):
        """Function to print the entiry question"""
        category = "$CATEGORY: " + self.__category + "\n" + "\n" if self.__category != '' else ''
        return  category \
                + self.create_question_text() \
                + "\n"
