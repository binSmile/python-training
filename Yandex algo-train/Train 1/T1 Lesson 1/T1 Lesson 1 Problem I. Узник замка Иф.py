inparams = []
for i in range(5):
    inparams.append(int(input()))
#  A, B, C, || D, E.


def soulution(A,B,C,D,E):
    brik = [A,B,C]
    brik.sort()


    if D > E:
        hole = (D,E)
    else:
        hole = (E,D)


    if brik[0] <= hole[0] and brik[1] <= hole[1]:
        return 'YES'
    else:
        return 'NO'


print(soulution(*inparams))
# print(soulution(1,1,1,1,1) == 'YES')
# print(soulution(2,2,2,1,1) == 'NO')