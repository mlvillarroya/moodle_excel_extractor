import subprocess
import os


def open_folder(path):
    import sys
    if 'linux' in sys.platform:
        os.system('xdg-open "%s"' % path)
    elif 'win32' in sys.platform:
        os.startfile(path)  # type: ignore
    elif 'darwin' in sys.platform:
        os.system('open "%s"' % path)
    else:
        raise RuntimeError("Unsupported operating system: {}".format(sys.platform))