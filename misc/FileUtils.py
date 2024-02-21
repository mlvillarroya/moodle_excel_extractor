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
