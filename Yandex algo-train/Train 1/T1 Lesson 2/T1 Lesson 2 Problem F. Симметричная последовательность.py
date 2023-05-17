# N = int(input())
# seq = tuple(map(int,input().split(' ')))

with open('input.txt', 'r') as fin:
    N = int(fin.readline()) # число из первой строки
    seq = tuple(map(int,fin.readline().split(' ')))

def solution(N, seq):
    i = 0
    j = 0
    while i < N + j -1:
        if seq[i] == seq[j-1]:
            i += 1
            j -= 1
        else:
            j = 0
            if seq[i] != seq[j-1]:
                i += 1

    M = i + j
    if M != 0:
        addnums = tuple(map(str,seq[:M][::-1]))
        addstr = ' '.join(addnums)
    else:
        addstr = ''
    return (M,addstr)

M, addstr = solution(N, seq)
print(M)
print(addstr, end=' ')
# print(addstr == '1 3 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1 2 1')



# def is_symmetric(nums):
#     for i in range(len(nums) // 2):
#         if nums[i] != nums[-1 - i]:
#             return False
#     return True
#
#
# def symmetric_sequence(nums):
#     for i in range(len(nums)):
#         if is_symmetric(nums[i:]):
#             return list(reversed(nums[:i]))
#
#
# assert symmetric_sequence([1, 2, 3, 4, 5, 4, 3, 2, 1]) == []
# assert symmetric_sequence([1, 2, 1, 2, 2]) == [1, 2, 1]
# assert symmetric_sequence([1, 2, 3, 4, 5]) == [4, 3, 2, 1]
#
#
# def main():
#     n = int(input())
#     nums = list(map(int, input().split()))
#     result = symmetric_sequence(nums)
#     print(len(result))
#     if len(result):
#         print(' '.join(map(str, result)))
#
#
# if __name__ == '__main__':
#     main()
