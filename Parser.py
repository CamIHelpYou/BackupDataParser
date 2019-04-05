import csv
from Class import compiledData


def grabinfo(filepath, info):
    '''
    Takes a CSV file and imports it into a class type for manipulation

    param filepath: file path of the CSV file
    param info: Dictionary of class compiledData
    '''
    with open(filepath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['\ufeff"Computer name"'] not in info:
                tmp = compiledData(row['\ufeff"Computer name"'])
                if 'Group name' in row:
                    tmp.groupname = row['Group name']
                if 'Last seen' in row:
                    tmp.lastseen = row['Last seen']
                if 'Last file backup' in row:
                    if '%' in row['Last file backup']:
                        tmp.lastfile = 'In Progress'
                    else:
                        tmp.lastfile = row['Last file backup']
                if 'Last image backup' in row:
                    if '%' in row['Last image backup']:
                        tmp.lastimage = 'In Progress'
                    else:
                        tmp.lastimage = row['Last image backup']
                if 'Images' in row:
                    tmp.imagesize = row['Images']
                if 'Files' in row:
                    tmp.filesize = row['Files']
                if 'All' in row:
                    tmp.all =  row['All']
                info[row['\ufeff"Computer name"']] = tmp
            else:
                if 'Group name' in row:
                    info[row['\ufeff"Computer name"']].groupname = row['Group name']
                if 'Last seen' in row:
                    info[row['\ufeff"Computer name"']].lastseen = row['Last seen']
                if 'Last file backup' in row:
                    if '%' in row['Last file backup']:
                        info[row['\ufeff"Computer name"']].lastfile = 'In Progress'
                    else:
                        info[row['\ufeff"Computer name"']].lastfile = row['Last file backup']
                if 'Last image backup' in row:
                    if '%' in row['Last image backup']:
                        info[row['\ufeff"Computer name"']].lastimage = 'In Progress'
                    else:
                        info[row['\ufeff"Computer name"']].lastimage = row['Last image backup']
                if 'Images' in row:
                    info[row['\ufeff"Computer name"']].imagesize = row['Images']
                if 'Files' in row:
                    info[row['\ufeff"Computer name"']].filesize = row['Files']
                if 'All' in row:
                    info[row['\ufeff"Computer name"']].all =  row['All']

    return info








