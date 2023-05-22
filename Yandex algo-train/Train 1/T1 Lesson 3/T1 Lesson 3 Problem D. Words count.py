# Link to task
# https://contest.yandex.ru/contest/27663/problems/D/

# Algorithm
#
# Asymptotic

def solution(lines):
    return set(' '.join(lines).split()).__len__()


test_input = ['She sells sea shells on the sea shore;',
"""The shells that she sells are sea shells I'm sure.""",
"""So if she sells sea shells on the sea shore,""",
"""I'm sure that the shells are sea shore shells."""]

assert solution(test_input) == 19


def main():
    import sys
    lines = sys.stdin.readlines()
    print(solution(lines))


if __name__ == '__main__':
    main()



