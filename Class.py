import datetime


class compiledData(object):
    '''
    Object for compiling users data
    '''
    def __init__(self, computername):
        self.computername = computername
        self.groupname = None
        self.lastseen = None
        self.lastfile = None
        self.lastimage = None
        self.imagesize = None
        self.filesize = None
        self.all = None


monthMatch = {'1': 'January', '2': 'February', '3': 'March', '4': 'April', '5': 'May', '6': 'June',
              '7': 'July', '8': 'Augst', '9': 'September', '10': 'October', '11': 'November', '12': 'December'}

