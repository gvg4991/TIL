import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    datas = list(map(int,input().split()))

    now = 1
    stop = 0
    cnt = 0
    while now < datas[0]:
        can = datas[now]
        next = now+can
        if next >= datas[0]:
            break
        for station in range(next,now,-1):
            if stop < station+datas[station]:
                stop = station+datas[station] #범위내 정류장에서 가장 멀리갈 수 있는 거리
                now = station #그 정류장을 다음정류장으로 지정
        cnt += 1

    print('#{} {}'.format(tc+1,cnt))