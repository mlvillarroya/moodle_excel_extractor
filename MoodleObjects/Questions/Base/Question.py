"""Generic question class"""
from typing import List

import misc.Constants as CS
import misc.StringFunctions as SF
from MoodleObjects.Answers import Answer

class Question:
    """Generic question class"""
    def __init__(self, category, code, question, answers_list: List[Answer], general_feedback):
        if code is None or \
            question is None or \
            answers_list is None:
            raise ValueError(CS.EXCEPTION_NONE_ARGUMENT)
        if  not self.__is_list_of_answers(answers_list):
            raise ValueError(CS.EXCEPTION_LIST_ANSWERS_NEEDED)
        self.__category = category or ''
        self.__code = code
        self.__question = question
        self.__answers_list = answers_list
        self.__general_feedback = general_feedback
        self.__feedback = "####" + general_feedback + "\n" if general_feedback else ''

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
    def answer(self):
        """Property: answers"""
        return self.create_answer_from_list()

    def create_question_text(self):
        """Function to create the text for a question"""
        return "::" + self.__code + "::" + self.__question + "{" + "\n" \
                + self.answer + "\n" \
                + self.__feedback \
                + "}"

    def create_answer_from_list(self):
        """Function to create the answer from a list"""
        return ""

    def print_question(self):
        """Function to print the entiry question"""
        category = "$CATEGORY: " + self.__category + "\n" + "\n" if not SF.string_empty_or_whitespace(self.__category) else ''
        return  category \
                + self.create_question_text() \
                + "\n"

    def __is_list_of_answers(self,answers_list):
        """Internal function to check if a parameter is a list of Answer class"""
        if not isinstance(answers_list,list): return False
        for element in answers_list:
            if not isinstance(element,Answer): return False
        return True
