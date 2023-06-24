def solution(infn):
    dotp = infn.split('.')
    ext = dotp[-1]
    fp = dotp[0].split('_')[1]
    res = 'DRIFT_%s_%s_%s.%s' % (fp[:4],fp[4:6],fp[6:8],ext)

    return res


assert solution('PXL_20230430_092422111.jpg') == 'DRIFT_2023_04_30.jpg'
assert solution('PXL_20120427_1433383789.jpg') == 'DRIFT_2012_04_27.jpg'
assert solution('PXL_20190830_143399492.jpg') == 'DRIFT_2019_08_30.jpg'




def main():
    infn = input()
    print(solution(infn))


if __name__ == '__main__':
    main()



