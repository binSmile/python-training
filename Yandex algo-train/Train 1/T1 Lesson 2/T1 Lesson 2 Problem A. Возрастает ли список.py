instr = list(map(int, input().split(' ')))
def solution(instr):

    for i in range(1,len(instr)):
        if instr[i] <= instr[i-1]:
            return 'NO'
    return 'YES'

print(solution(instr))