# K1, M, K2, P2, N2 = map(int,input().split(' '))
K1, M, K2, P2, N2 = 89, 29, 41, 1, 11

def solution(K1, M, K2, P2, N2):
    PN2 = N2 + (P2-1) * M
    Vmax = (K2 / PN2) //1+1


        Vmin = ((K2-1) // (PN2-1))+1

    PN1min = K1 // Vmax
    PN1max = K1 // Vmin
    if PN1min == 0 or PN1max == 0:
        return (-1, -1)
    P1min = (PN1min // M) + 1
    P1max = (PN1max // M) + 1
    if P1min == P1max:
        P1 = P1min
    else:
        P1 = 0
    N1min = PN1min - (P1min - 1) * M + 1
    N1max = PN1max - (P1max - 1) * M + 1
    if N1min == N1max:
        N1 = N1min
    else:
        N1 = 0

    return (P1, N1)


P1, N1 = solution(K1, M, K2, P2, N2)
print(P1, N1)
