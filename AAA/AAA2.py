N1, M1, N2, M2 = map(int, input().split())
values = []
for _ in range(N1):
    values += input().split()
# print(values)

for i in range(N2):
    print(' '.join(values[M2*i:M2+M2*i]))