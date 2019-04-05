import datetime
from Class import monthMatch
from tabulate import tabulate


def Group(info):
    '''
    Organizes by object by group name for output
    '''
    groupnames = {}
    for key, value in info.items():
        if value.groupname is None:
            continue
        if value.groupname not in groupnames:
            groupnames[value.groupname] = []
        groupnames[value.groupname].append(value)
    return groupnames

def comparetime(computer):
    '''
    Takes a computer and sees if backups done in last 14 days
    '''
    if len(computer.lastfile) + len(computer.lastimage) is not 28:
        return True

    lasttime = datetime.datetime.strptime(computer.lastseen, "%m/%d/%y %H:%M")
    backuptime = datetime.datetime.strptime(computer.lastfile, "%m/%d/%y %H:%M")
    imagetime =  datetime.datetime.strptime(computer.lastimage, "%m/%d/%y %H:%M")

    if (lasttime - backuptime) > datetime.timedelta(days=14):
        return True
    if (lasttime - imagetime) > datetime.timedelta(days=14):
        return True
    return False



def outputemail(info):
    '''
    Outputs emails for each group
    '''
    groupnames = Group(info)
    today = datetime.datetime.now()
    headers1 = ['Computer Name', 'Last Seen', 'Last File', 'Last Image', 'Images Size', 'Files Size', 'Total Size']
    headers2 = ['Computer Name', 'Last Seen', 'Last File', 'Last Image']
    headers3 = ['Computer Name', 'Last Seen']
    for group, array in groupnames.items():
        data1 = []
        data2 = []
        data3 = []
        longtimeFlag = False
        backup = False
        with open(str(group) + '.txt', 'w') as file:
            file.write('Hey ' + str(group) + ',\n\n\n')
            file.write("It looks like it's that time of the month again! Here are your " + monthMatch[str(today.month - 1)] + ' results.\n\n')
            for computer in array:
                data1.append([computer.computername, computer.lastseen, computer.lastfile, computer.lastimage, computer.imagesize, computer.filesize, computer.all])
                lasttime = datetime.datetime.strptime(computer.lastseen, "%m/%d/%y %H:%M")
            file.write(tabulate(data1, headers=headers1))

            # Checks time conditions for messages
            for computer in array:
                if (today - lasttime) > datetime.timedelta(days = 14):
                    data3.append([computer.computername, computer.lastseen, computer.lastfile, computer.lastimage])
                    longtimeFlag = True
                if comparetime(computer):
                    data2.append([computer.computername, computer.lastseen])
                    backup = True

            if backup:
                file.write("\n\nYou may want to check the following computers as they are online but we haven't seen a backup in over 2 weeks\n")
                file.write(tabulate(data2, headers=headers2))
            if longtimeFlag:
                file.write("\n\nWe wanted to let you know these computers haven't reached our servers in over two weeks.\nThis may just be due to them being powered off and withotuuse for quite some time. It may also be possible that the backup software was deleted.\n")
                file.write(tabulate(data3, headers=headers3))






