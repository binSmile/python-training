income = input()
lastin = -2000000000


def twocomp(a, b):
    if a == b:
        return 'const'
    elif a > b:
        return 'down'
    else:
        return 'up'


anyconst, anyup, anydown = 0, 0, 0
while income != '-2000000000':
    income = int(income)
    if not lastin == -2000000000:
        seqdir = twocomp(lastin, income)
        if seqdir == 'const':
            anyconst = True
        elif seqdir == 'down':
            anydown = True
        elif seqdir == 'up':
            anyup = True
    lastin = income
    income = input()

if anyconst and not (anydown or anyup):
    print('CONSTANT')
elif anyconst and anydown and not anyup:
    print('WEAKLY DESCENDING')
elif not anyconst and anydown and not anyup:
    print('DESCENDING')
elif anyconst and anyup and not anydown:
    print('WEAKLY ASCENDING')
elif not anyconst and anyup and not anydown:
    print('ASCENDING')
else:
    print('RANDOM')
