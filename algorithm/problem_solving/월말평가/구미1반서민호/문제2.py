import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    sero,garo = map(int,input().split())
    datas = [[0]*garo for _ in range(sero)]
    for row in range(sero):
        datas[row] = list(map(int,input().split()))
    # print(datas)

    ans = 0
    for tb in range(1,sero):
        top = datas[0:tb]
        bottom = datas[tb:sero]
        # print(top)
        # print(bottom)
        turn_t = list(map(list,zip(*top)))
        turn_b = list(map(list,zip(*bottom)))
        # print(turn_t)
        # print(turn_b)
        for left in range(1,garo-2):
            for right in range(left+1,garo):
                sumtl = sumtm = sumtr = sumbl = sumbm = sumbr = 0
                # print('{} {} {}'.format(tb,left,right))
                tl = list(map(list,zip(*turn_t[0:left])))
                for lv in tl:
                    for v in lv:
                        sumtl += v
                tm = list(map(list,zip(*turn_t[left:right])))
                for lv in tm:
                    for v in lv:
                        sumtm += v
                tr = list(map(list,zip(*turn_t[right:garo])))
                for lv in tr:
                    for v in lv:
                        sumtr += v
                bl = list(map(list,zip(*turn_b[0:left])))
                for lv in bl:
                    for v in lv:
                        sumbl += v
                bm = list(map(list,zip(*turn_b[left:right])))
                for lv in bm:
                    for v in lv:
                        sumbm += v
                br = list(map(list,zip(*turn_b[right:garo])))
                for lv in br:
                    for v in lv:
                        sumbr += v
                # print('{} {} {} {} {} {}'.format(sumtl, sumtm, sumtr, sumbl, sumbm, sumbr))
                target = [sumtl, sumtm, sumtr, sumbl, sumbm, sumbr]

                result = 0
                for first in range(0,4):
                    for second in range(first+1,5):
                        for third in range(second+1,6):
                            result = abs(target[first]-target[second])+abs(target[second]-target[third])+abs(target[third]-target[first])
                            if ans < result:
                                ans = result
    print('#{} {}'.format(tc+1,ans))

