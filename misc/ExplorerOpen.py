import subprocess
import os
import sys


def open_folder(path):
    if 'linux' in sys.platform:
        subprocess.Popen(['xdg-open',path])
    elif 'win32' in sys.platform:
        os.startfile(path)  # type: ignore
    elif 'darwin' in sys.platform:
        subprocess.Popen(['open',path])
    else:
        raise RuntimeError("Unsupported operating system: {}".format(sys.platform))
    