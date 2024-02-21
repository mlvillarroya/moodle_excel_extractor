from excel import ExcelCreator, ExcelExtractor
from MoodleObjects import MultipleChoiceArray, NumericArray, OneAnswerArray, TrueFalseArray
from misc import FileUtils
# create a demo excel file
excel_file = ExcelCreator(demo_data=True,
                          create_multiple_choice=True,
                          create_numeric=True,
                          create_one_answer=True,
                          create_true_false=True)
excel_file.save_excel_file()

# extract questions from the demo excel file
excel_extractor = ExcelExtractor(excel_file.full_path)
excel_questions = excel_extractor.extract_questions_from_workbook()

# excel_questions is a dictionary. Each one of the keys to an object
array_of_answers = []
if "Multiple choice" in excel_questions:
    multiple_choice_array = MultipleChoiceArray(excel_questions["Multiple choice"])
    array_of_answers.append(multiple_choice_array)
if "Numeric" in excel_questions:
    numeric_array = NumericArray(excel_questions["Numeric"])
    array_of_answers.append(numeric_array)
if "One answer" in excel_questions:
    one_answer_array = OneAnswerArray(excel_questions["One answer"])
    array_of_answers.append(one_answer_array)
if "True_false" in excel_questions:
    true_false_array = TrueFalseArray(excel_questions["True_false"])
    array_of_answers.append(true_false_array)

answer = []
for element in array_of_answers:
    answer.append(element.print_all_questions())

FileUtils.create_txt_file("answers.txt", "\n".join(answer))