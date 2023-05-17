N, M, K = map(int, input().split(' '))
bombs = []
for i in range(K):
    bombs.append(tuple(map(int,input().split(' '))))


def update(b, bf):
    for i in range(b[0]-1,b[0]+2):
        for j in range(b[1]-1,b[1]+2):
            if bf[i][j] != '*':
                bf[i][j] += 1
    return bf

# N - строк i
# M - столбцов j
def solution(N,M,bombs):
    bf = [[0] * (M+2) for i in range(N+2)]
    # bf[row][col]
    for b in bombs:
        bf[b[0]][b[1]] = '*'
        bf = update(b,bf)

    return bf


field = solution(N,M,bombs)
for l in field[1:-1]:
    print(*l[1:-1])