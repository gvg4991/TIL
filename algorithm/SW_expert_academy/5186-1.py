import sys
sys.stdin = open("5186.txt")

test = int(input())
for tc in range(test):
    case = float(input())
    datas = case
    val = 1
    long = 0
    result = 1
    ans = 0

    while datas != 0 and long < 13:
        val = val/2
        result = result*10
        if datas >= val:
            ans += 1/result
            datas -= val
        long += 1

    if datas != 0:
        ans = 'overflow'

    print('#{} {}'.format(tc+1, ans))
