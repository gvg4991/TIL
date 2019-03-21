# 0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 run, 같은 숫자가 3개 이상이면 triplet이라고 한다.
# 게임을 시작하면 플레이어1과 플레이어 2가 교대로 한 장 씩 카드를 가져가며, 6장을 채우기 전이라도 먼저 run이나 triplet이 되는 사람이 승자가 된다.
# 두 사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를 알아내는 프로그램을 작성하시오. 만약 무승부인 경우 0을 출력한다.
# 예를 들어 9 9 5 6 5 6 1 1 4 2 2 1인 경우, 플레이어 1은 9, 5, 5, 1, 4, 2카드를, 플레이어2는 9, 6, 6, 1, 2, 1을 가져가게 된다.
# 이때는 카드를 모두 가져갈 때 까지 run이나 triplet이 없으므로 무승부가 된다.
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 각 줄에 0에서 9사이인 12개의 숫자가 주어진다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


import sys
sys.stdin = open('input.txt')


def babyjin(lst,value):
    global ans
    cnt = [0] * (max(lst) + 1)
    ans = False

    for i in lst:
        cnt[i] += 1
    # print(cnt)

    for cnt_triple in range(len(cnt)):
        if cnt[cnt_triple] >= 6:
            cnt[cnt_triple] -= 6
            ans = True
        elif cnt[cnt_triple] >= 3:
            cnt[cnt_triple] -= 3
            ans = True
    # print(cnt)

    for cnt_run in range(len(cnt) - 2):
        if cnt[cnt_run] >= 2 and cnt[cnt_run + 1] >= 2 and cnt[cnt_run + 2] >= 2:
            cnt[cnt_run] -= 2
            cnt[cnt_run + 1] -= 2
            cnt[cnt_run + 2] -= 2
            ans = True
        elif cnt[cnt_run] >= 1 and cnt[cnt_run + 1] >= 1 and cnt[cnt_run + 2] >= 1:
            cnt[cnt_run] -= 1
            cnt[cnt_run + 1] -= 1
            cnt[cnt_run + 2] -= 1
            ans = True
    # print(cnt)

    if ans == True:
        return True
    else:
        return False



test = int(input())
for tc in range(test):
    datas = list(map(int,input().split()))
    first = []
    second = []
    result = 0
    ans = False
    for case in range(len(datas)//2):
        first.append(datas[2*case])
        second.append(datas[2*case+1])

        if babyjin(first,datas[2*case]):
            result = 1
            break
        elif babyjin(second,datas[2*case+1]):
            result = 2
            break
    print('#{} {}'.format(tc+1,result))





























    #
    # empty=[0]*len(datas//2)
    # cnt=[0]*(max(datas)+1)
    #
    # for i in datas:
    #     cnt[i]+=1
    # # print(cnt)
    #
    # for cnt_triple in range(len(cnt)):
    #     if cnt[cnt_triple]>=6:
    #         cnt[cnt_triple]-=6
    #     elif cnt[cnt_triple]>=3:
    #         cnt[cnt_triple]-=3
    # # print(cnt)
    #
    # for cnt_run in range(len(cnt)-2):
    #         if cnt[cnt_run]>=2 and cnt[cnt_run+1]>=2 and cnt[cnt_run+2]>=2:
    #                 cnt[cnt_run]-=2
    #                 cnt[cnt_run+1]-=2
    #                 cnt[cnt_run+2]-=2
    #         elif cnt[cnt_run]>=1 and cnt[cnt_run+1]>=1 and cnt[cnt_run+2]>=1:
    #                 cnt[cnt_run]-=1
    #                 cnt[cnt_run+1]-=1
    #                 cnt[cnt_run+2]-=1
    # # print(cnt)
    #
    # if sum(cnt) == 0:
    #         print(True)
    # else:
    #         print(False)