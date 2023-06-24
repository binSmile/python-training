def getdate(infn):
    dotp = infn.split('.')
    ext = dotp[-1]
    match infn[:3]:
        case 'PXL':
            fp = dotp[0].split('_')[1]
            y = fp[:4]
            m = fp[4:6]
            d = fp[6:8]
        case 'DCI':
            fp = dotp[0].split('-')
            y = fp[1]
            m = fp[2]
            d = fp[3]
        case _:
            fp = dotp[0]
            y = fp[:4]
            m = fp[4:6]
            d = fp[6:8]

    # res = 'DRIFT_%s_%s_%s.%s' % (y,m,d,ext)
    return '_'.join([y,m,d])
def stat(calendar,lines):
    edict = {}
    for p in lines:
        date = getdate(p)
        edict[calendar[date]][1] = edict.setdefault(calendar[date], [date, 0])[1] + 1

    return edict



def eventselector(events):
    calend = {}
    for  e in events:
        p = e.split()
        date = '_'.join(p[1:])
        calend[date] = p[0]
    return calend




def main():
    from sys import stdin

    lines = []
    for line in stdin:
        lines.append(line.rstrip('\n'))
    # lines = ['VACATIONGREECE 2021 11 27', 'CHESSTOURNAMENT 2004 12 18', 'CONFERENCE 2002 08 02', '200208020145-6.jpg', '200208020053-10.jpg', 'DCIM-2021-11-27-0.jpg', 'DCIM-2002-08-02-6.jpg', 'DCIM-2004-12-18-3.jpg', '202111271009-2.jpg', '200412180835-8.jpg', 'DCIM-2002-08-02-10.jpg', '202111270804-5.jpg']
    calendar = eventselector(lines[0:3])
    edict = stat(calendar, lines[3:])
    elist = list(edict.keys())
    elist.sort()
    for e in elist:
        for i in range(edict[e][1]):
            print('%s_%s_%s.jpg' % (e,edict[e][0],i))

if __name__ == '__main__':
    main()



