"""Base class for questions array"""
import misc.Constants as CS
class BaseArray:
    """Class for base arrays"""
    def __init__(self, dictionary_array, main_category = 'Category'):
        if  not self.__is_list_of_dict(dictionary_array):
            raise ValueError(CS.EXCEPTION_LIST_DICT_NEEDED)
        self.__questions_array = []
        self.__successfull_answers = 0
        self.__failed_answers = 0
        for question in dictionary_array:
            try:
                self.__questions_array.append(self.__create_question(question,main_category))
            except Exception:
                self.__failed_answers += 1
            else:
                self.__successfull_answers += 1

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

    def __create_question(self, question, main_category= 'Category'):
        """Function to create the questions"""
        category = self._extract_category(question, main_category)
        answer = self._extract_answer_list(question)
        return self._extract_question(category,question,answer)

    def _extract_category(self, question, main_category):
        """MUST BE OVERRIDEN Function: extract main category"""
        return ''

    def _extract_answer_list(self, question):
        """MUST BE OVERRIDEN Function: extract answer list"""
        return ''

    def _extract_question(self,category, question, answers):
        """MUST BE OVERRIDEN Function: create question"""
        return ''

    def __is_list_of_dict(self,dict_array):
        """Internal function to check if a parameter is a list of Answer class"""
        if not isinstance(dict_array,list):
            return False
        for element in dict_array:
            if not isinstance(element,dict):
                return False
        return True

    def print_all_questions(self):
        """Function that prints all the questions in array"""
        questions_printed = ''
        for question in self.__questions_array:
            questions_printed += question.print_question() + '\n'
        return  questions_printed
