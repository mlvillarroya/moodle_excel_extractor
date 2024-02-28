# Create a txt file and save it into a path
def create_txt_file(path, content):
    # if there is some error, raise it
    try:
        file = open(path, "w")
        file.write(content)
        file.close()
    except Exception as e:
        raise e
    return path


def crop_path_folders(path, number_of_folders):
    # split the path into folders
    folders = path.split("\\")
    # crop the folders and return the last part of the path beginning by dots
    return "...\\{}".format("\\".join(folders[-number_of_folders:]))
