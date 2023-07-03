
################################################
#
# 2nd stage
# Task 2: Print indexes of vectors, which have angle less than *t*
#
# input:
# 1st line: vector v
# 2nd line: quantity of u vectors and threshold angle between v and u
# next n lines: each vector u on each n lines
#
################################################


import math
def solution(v,n,t,u_list):
    res_list = []
    t_rad = math.radians(t)
    magnitude_v = (sum(v_i ** 2 for v_i in v)) ** (0.5)
    if magnitude_v == 0:
        return '-1'

    for u_index in range(n):
        u = u_list[u_index]
        dot_product = sum(v_i * u_i for v_i, u_i in zip(v, u))

        magnitude_u = (sum(u_i ** 2 for u_i in u))**(0.5)
        if magnitude_u == 0:
            continue

        cos_theta = dot_product / (magnitude_u * magnitude_v)
        angle_rad = math.acos(cos_theta)
        if angle_rad <= t_rad:
            res_list.append(u_index)
    if res_list:
        return ' '.join(map(str,res_list))
    else:
        return '-1'


assert solution([1.0, 0.0],
         2,90.0,
         [[-1.0, 1.0], [0.0, 1.0]]) == "1"

assert solution([1.0, 1.0, 1.0, 1.0],
         4, 30.0,
         [[0.0, 0.0, 0.0, 1.0], [1.0, 0.0, 1.0, 0.0], [1.0, 1.0, 1.0, 1.0], [1.0, 1.0, 1.0, 0.0]]) \
        == "2 3"

assert solution([1.0, 1.0, 1.0],
         2, 0.0,
         [[0.0, 0.0, 1.0], [3.0, 0.0, 3.0]]) \
        == "-1"

def main():
    v = list(map(float, input().split()))
    n, t = list(map(float, input().split()))
    n = int(n)
    u_list = []
    for _ in range(n):
        u = list(map(float, input().split()))
        u_list.append(u)

    print(solution(v,n,t, u_list))

if __name__ == '__main__':
    main()


