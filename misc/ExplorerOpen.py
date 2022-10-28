import subprocess
import os

class ExplorerOpen:
    # def ExplorerOpen(path):
    #     subprocess.Popen(r'explorer ' + path)
    def ExplorerOpen(path):
        import sys
        if 'linux' in sys.platform: 
            os.system('xdg-open "%s"' % path)
        elif 'win32' in sys.platform: 
            os.startfile(path)  # type: ignore
        else:
            raise RuntimeError("Unsupported operating system: {}".format(sys.platform))