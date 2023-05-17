

def solution(a,b,c):
    if c < 0:
        return 'NO SOLUTION'
    elif a == 0:
        if c*c == b:
            return 'MANY SOLUTION'
        else:
            return 'NO SOLUTION'
    elif (b,c) == (0,0):
        return 0

    elif c == 0:
        x = -b / a
        return x
 

    else:
        x = (c*c-b)/a
        return x
        



while True:
    print('Solve abc')
    a = int(input())
    b = int(input())
    c = int(input())
    print(solution(a,b,c))
