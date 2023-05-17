
n,k,m = map(int,input().split())


def solutin(n, k, m):
    if n >= k >= m:
        residual = n % k
        nk = n // k
        residual += (k % m) * nk
        km = k // m
        return km*nk + solutin(residual, k, m)
    else:
        return 0

solutin(n,k,m)



print(solutin(10,5,2) == 4)
print(solutin(13,5,3) == 3)
print(solutin(14,5,3) == 4)
