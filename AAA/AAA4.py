def solution(infn):
    dotp = infn.split('.')
    ext = dotp[-1]
    match infn[:3]:
        case 'PXL':
            fp = dotp[0].split('_')[1]
            y = fp[:4]
            m = fp[4:6]
            d = fp[6:8]
        case 'DCI':
            fp = dotp[0].split('-')
            y = fp[1]
            m = fp[2]
            d = fp[3]
        case _:
            fp = dotp[0]
            y = fp[:4]
            m = fp[4:6]
            d = fp[6:8]

    res = 'DRIFT_%s_%s_%s.%s' % (y,m,d,ext)

    return res


assert solution('PXL_20230430_092422111.jpg') == 'DRIFT_2023_04_30.jpg'
assert solution('PXL_20120427_1433383789.jpg') == 'DRIFT_2012_04_27.jpg'
assert solution('PXL_20190830_143399492.jpg') == 'DRIFT_2019_08_30.jpg'

assert solution('DCIM-2005-07-08-8.jpg') == 'DRIFT_2005_07_08.jpg'
assert solution('DCIM-2009-01-24-10.jpg') == 'DRIFT_2009_01_24.jpg'
assert solution('202304300924-1.jpg') == 'DRIFT_2023_04_30.jpg'
# assert solution('') == ''





def main():
    infn = input()
    print(solution(infn))


if __name__ == '__main__':
    main()



