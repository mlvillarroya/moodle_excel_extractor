from GUI import ExcelGUI


def main():
    try:
        excel_gui = ExcelGUI()
        excel_gui.create_GUI()
    except Exception as e:
        print(f"Error: {e}")
        input("Press Enter to continue...")


if __name__ == "__main__":
    main()

# pyinstaller --name moodle_excel_extractor --add-data static:static --add-data output:output --contents-directory contents --windowed main.py
