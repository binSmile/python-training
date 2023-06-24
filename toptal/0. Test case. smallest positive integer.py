
A = [-1,-2]

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # Implement your solution here
    A = set(A)
    i = 1
    while i  in A:
        print('i: ',i)
        i += 1
    return i


solution(A)