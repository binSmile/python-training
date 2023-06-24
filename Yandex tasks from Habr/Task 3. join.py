#  to realize joint function
import random
import pandas as pd



def main():
    # initialize test data
    MAXTEST = 10
    n1 = MAXTEST # rows in T1
    t1 = []
    for i in range(2):
        t1.append([random.randint(1, MAXTEST) for _ in range(n1)])

    n2 = MAXTEST # rows in T2
    t2 = []
    for i in range(2):
        t2.append([random.randint(1, MAXTEST) for _ in range(n2)])

    OPERATION = ('INNER', 'LEFT', 'RIGHT', 'FULL')[random.randint(0,3)]

    print(slow_solution(t1, t2, OPERATION), pandas_solition(t1,t2,OPERATION))

def slow_solution(t1,t2,OPERATION):
    res_table = [[],[],[]]
    checkI = {}


    match_right = [0]*len(t2[0])
    for a1 in range(len(t1[0])):
        match = 0
        for a2 in range(len(t2[0])):
            if t1[0][a1] == t2[0][a2]:
                res_table[0].append(t1[0][a1])
                res_table[1].append(t1[1][a1])
                res_table[2].append(t2[1][a1])
                match += 1
                match_right[a2] += 1

        if not match and OPERATION in ('LEFT','FULL'):
            res_table[0].append(t1[0][a1])
            res_table[1].append(t1[1][a1])
            res_table[2].append('NULL')
    if OPERATION in ('RIGHT','FULL'):
        for a2 in range(len(t2[0])):
            if match_right[a2] == 0:
                res_table[0].append(t2[0][a2])
                res_table[1].append('NULL')
                res_table[2].append(t2[1][a2])

    # return res_table
    return len(res_table[0])



def pandas_solition(t1,t2,OPERATION):
    # Testing
    if OPERATION == 'FULL':
        OPERATION = 'outer'
    df_l = pd.DataFrame(t1).T
    df_r = pd.DataFrame(t2).T
    # df_res = pd.DataFrame(result).T

    df_l.set_index(0, inplace=True)
    df_r.set_index(0, inplace=True)


    result = df_l.join(df_r, how=OPERATION.lower(), lsuffix='_l', rsuffix='_r').shape[0]
    return result

if __name__ == '__main__':
    main()