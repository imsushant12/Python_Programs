import subprocess as sp

programName = "notepad.exe"
fileName = "file.txt"
sp.Popen([programName , fileName])