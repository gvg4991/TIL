import sys
sys.stdin = open("input.txt")

test = int(input())
for tc in range(test):
    case = int(input())
    datas = list(map(int,input().split()))
    #print(datas)

    target = []
    for now in range(case-1):
        for daum in range(now+1,case):
            target.append(datas[now]*datas[daum])
    result = sorted(target)
    yo = -1
    for r in result[::-1]:
        ans = list(map(int,(" ".join(str(r))).split()))
        if ans == sorted(ans):
            yo = r
            break
    print('#{} {}'.format(tc+1,yo))












