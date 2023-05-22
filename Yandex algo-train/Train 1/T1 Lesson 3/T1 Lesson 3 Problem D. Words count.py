# Link to task
# https://contest.yandex.ru/contest/27663/problems/D/

# Updated solution. .read() is better then readline()

def solution(text):
    return set(text.split()).__len__()


test_input = '''She sells sea shells on the sea shore;
The shells that she sells are sea shells I'm sure.
So if she sells sea shells on the sea shore,
I'm sure that the shells are sea shore shells.'''

assert solution(test_input) == 19


def main():
    import sys
    text = sys.stdin.read()
    print(solution(text))


if __name__ == '__main__':
    main()



