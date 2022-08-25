import subprocess

class ExplorerOpen:
    def ExplorerOpen(path):
        subprocess.Popen(r'explorer ' + path)