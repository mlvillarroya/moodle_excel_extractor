"""Multiple choice questions. Inherits from Question"""
from MoodleQuestions.Question_answer import Question

class MultipleChoice(Question):
    """Class MultipleChoice inherits from Question"""
    def __init__(self,category,code,question,answers_list,general_feedback):
        if len(answers_list) < 2 or answers_list[1].value is None:
            raise ValueError('Argument cannot be None')
        super().__init__(category,code,question,answers_list,general_feedback)

    def create_answer_from_list(self):
        """Function to create custom text for multiple choice questions"""
        complete_answer = ''
        for index,answer in enumerate(self.__answers_list):
            value = "%" + answer.value + "%" if answer.value != '' else ''
            answer_value = "=" if index == 0 else "~" + value
            feedback = "#" + answer.feedback if answer.feedback != '' else ''
            next_line = "\n" if index < len(self.__answers_list) - 1 else ''
            complete_answer = complete_answer + answer_value + answer.answer + feedback + next_line
        return complete_answer
