# ax + by = e
# cx + dy = f

# inparams = []
# for i in range(6):
#     inparams.append(int(input()))

def solution(a,b,c,d,e,f):
    if a / e == b / d and c / e == f / d:
        print("The system has infinite solutions.")
    else:
        D = a * d - b * c
        if D != 0:
            x = (e * d - b * f) / D
            y = (a * f - e * c) / D
            return 2, x, y
        else:
            return 0



# print(solution(*inparams))
print(solution(1,0,0,1,3,3) == '2 3 3')
print(solution(1,0,0,1,3,3))
# print(solution(1,1,2,2,1,2) == '1 -1 1')
# print(solution(0,2,0,4,1,2) == '4 0.5')