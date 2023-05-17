K1, M, K2, P2, N2 = map(int,input().split(' '))

def solution(K1, M, K2, P2, N2):
    PN2 = M*(P2-1)+N2
    vm = 1
    check = False
    while not check:
        if (PN2-1)*vm <= K2 <= PN2*vm:
                check = True
        elif K2 <= PN2*vm:
            vm += 1
        else:
            break
    if check:
        PN1 = (K1 // vm) + 1
        P1 = 1 + PN1 // M
        N1 = PN1 % M
    else:
        return (-1,-1)
    

   

    return (P1, N1)


P1, N1 = solution(K1, M, K2, P2, N2)
print(P1, N1)
