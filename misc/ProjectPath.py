import os

def getProjectPath():
    # Get the current working directory, that is the parent of current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    list_without_current_dir = current_dir.split(os.sep)[:-1]
    path = os.sep.join(list_without_current_dir)
    return path