from Parser import grabinfo
from FileManipulation import outputemail
from tkinter import Tk
from tkinter.filedialog import askopenfilenames

info = {}
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filenames = askopenfilenames() # show an "Open" dialog box and return the path to the selected file

for file in filenames:
    grabinfo(file, info)
outputemail(info)