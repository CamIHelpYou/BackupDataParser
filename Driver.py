from Parser import grabinfo
from FileManipulation import outputemail

info = {}
grabinfo('UrBackup - Keeps your data safe.csv', info)
grabinfo('UrBackup - Keeps your data safe(1).csv', info)
outputemail(info)