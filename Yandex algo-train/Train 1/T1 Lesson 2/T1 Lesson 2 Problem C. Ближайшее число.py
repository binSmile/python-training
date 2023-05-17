N = int(input())
numlist = list(map(int, input().split(' ')))
aim = int(input())

def findclose(N, numlist, aim):
    if N == 1:
        return numlist[0]
    else:
        mm = numlist[0]
        md = abs(mm-aim)
        for i in range(1,len(numlist)):
            d = abs(aim-numlist[i])
            if d < md:
                md = d
                mm = numlist[i]
        return mm

print(findclose(N, numlist, aim),end='')