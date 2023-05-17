import random
# troom, tcond = map(int,input().split(' '))
# mode = input()

troom, tcond = 10, 20
mode = 'heat'

# freeze auto heat freeze
def cond(troom, tcond, mode):
    match mode:
    	case 'auto':
    	     return tcond
    	case 'fan':
    	     return troom
    	case 'heat':
    	     return max(troom,tcond)
    	case 'freeze':
    	     return min(troom,tcond)

def condf(troom, tcond, mode):
    match mode:
    	case 'auto':
    	     return tcond
    	case 'fan':
    	     return troom
    	case 'heat':
    	     return max(troom,tcond)
    	case _:
    	     return min(troom,tcond)
#print(cond(troom, tcond, mode))

def condif(troom, tcond, mode):
    if mode == 'auto':
        return tcond
    elif mode == 'fan':
        return troom
    elif mode == 'heat':
        return max(troom, tcond)
    else:
        return min(troom, tcond)


troomlist, tcondlist, modelist = [],[], []
for i in range(0,100):
    t = random.randint(-50,50)
    troomlist.append(t)
    t = random.randint(-50,50)
    tcondlist.append(t)
    n = random.randint(0,3)
    modelist.append(n)

def dotest(troomlist, tcondlist, modelist,func):
    mode = ['auto','fan','heat','freeze']
    for i in range(len(troomlist)):
        r = func(troomlist[i], tcondlist[i], mode[modelist[i]])
        

import timeit

for f in ['cond', 'condf', 'condif']:
    print(f, end='  ')
    print(timeit.timeit("dotest(troomlist, tcondlist, modelist, %s)" % f, globals=globals()))
