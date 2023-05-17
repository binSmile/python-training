ntel = input('')
oldtel = []
for i in range(3):
    oldtel.append(input())


def tostd(tel):
    ntel = ''
    for t in tel:
        if t in '+0123456789':
            ntel += t
    tel = ntel     
    if tel[0:2] == '+7':
        tel = '8' + tel[2:]
        return tel

    if len(tel) == 7:
        return '8495'+tel
    return tel

ntel = tostd(ntel)
for i in oldtel:
    if ntel == tostd(i):
        print('YES')
    else:
        print('NO')
