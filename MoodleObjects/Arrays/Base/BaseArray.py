"""Base class for questions array"""
class BaseArray:
    """Class for base arrays"""
    def __init__(self):
        self.__questions_array = None
        self.__successfull_answers = 0
        self.__failed_answers = 0

    @property
    def question_array(self):
        """Property: questions array"""
        return self.__questions_array

    @property
    def successfull_answers(self):
        """Property: successfull answers"""
        return self.__successfull_answers

    @property
    def failed_answers(self):
        """Property: questions array"""
        return self.__failed_answers

    def extract_category(self, question, main_category):
        """Function: extract main category"""
        if not isinstance(question,dict):
            raise ValueError("Question needs to be in dictionary format")
        return ''

    def extract_answer_list(self, question):
        """Function: extract answer list"""
        return ''

    def create_question(self,category, question, answers):
        """Function: create question"""
        return ''

    def create_questions_array_from_dictionary_array(self, dictionary_array, main_category = ''):
        """Function: create questions from dictionary"""
        for question in dictionary_array:
            try:
                category = self.extract_category(question, main_category)
                answer = self.extract_answer_list(question)
                question = self.create_question(category,question,answer)
                self.__questions_array.append(question)
            except Exception:
                self.__failed_answers += 1
            else:
                self.__successfull_answers += 1
