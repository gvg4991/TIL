# Shuffle-O-Matic 은 카드의 순서를 섞는데 사용하는, 카드 셔플러이다.
# [그림 1] 과 같이, 양쪽에 카드를 절반씩 올려놓고, 동작 버튼을 누르면 카드가 가운데로 떨어지면서 섞이게 된다.
#
#
#
#
#
#                                                 [그림 1]
#
#
# 이 카드 셔플러는 특이하게도, 카드가 섞이기 시작하는 시점인 x 값을 사용자가 조정할 수 있다.
# 카드 셔플러의 사용 방법은 아래와 같다.
#
#
#
#
# 1. N 개로 이루어진 덱을 절반으로 나누어 올려둔다.
#
#
# 1 ~ N/2 번째 카드는 왼쪽 (L), N/2 + 1 ~ N 번째 카드는 오른쪽 (R) 에 올려둔다.
#
#
#
#
# 2. 카드 셔플러의 측면에 있는 다이얼로 x 값을 조정한 후, 동작 버튼을 누른다.
#
#
#
# 다이얼로 조정할 수 있는 x 값은 0 ~ N-1 이며, x 값에 따라 카드가 섞이는 순서가 달라진다.
# N = 6이고, 기존 카드의 순서가 오름차순으로 정렬된 상태일 때, 아래 [그림 2] 와 같은 순서로 셔플이 된다.
#
#
#
#
#                                                       [그림 2]
#
#
#
#
# Shuffle-O-Matic 의 기능을 활용하여, 카드의 순서가 오름차순 또는 내림차순이 되도록 정렬하려고 한다.
#
#
#
#
# 입력으로 N 장의 카드와, 정리되지 않은 상태의 카드 순서가 주어질 때,
# 최소 몇 번의 셔플로 카드를 정렬할 수 있는지를 계산하는 프로그램을 작성하라.
#
#
#
#
# 정답으로 오름차순으로 정렬했을 때와 내림차순으로 정렬했을 때 중, 셔플 횟수의 최소값을 출력한다.
#
#
#
#
# 단, 정렬이 불가능한 경우나 셔플 횟수가 5 회를 초과할 경우, 정답으로 -1 을 출력한다.
#
#
#
#
# [제약사항]
#
#
# 1. 카드의 개수 N 은 4 이상 12 이하의 짝수이다. (4 ≤ N ≤ 12)
# 2. 각각의 카드는 1 ~ N 번까지 숫자가 표기되어 있다.
#
#
#
#
# [입력]
#
#
# 입력은 첫 줄에 총 테스트 케이스의 개수 T 가 온다. 다음 줄 부터 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 줄에는 카드의 갯수 N 이 주어진다.
# 두 번째 줄에는 정렬되지 않은 상태의 카드 번호가 순서대로 나열된다.
#
#
#
#
# [출력]
#
#
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
# (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
# 정답으로 정렬에 필요한 최소 셔플 횟수를 출력한다.
#
#
#
# ------------------------------------------------------------------------------------------------------------------------
# 5
# 4
# 1 2 3 4
# 4
# 4 2 3 1
# 6
# 6 5 4 2 3 1
# 8
# 6 1 4 7 2 5 8 3
# 12
# 2 7 4 1 3 5 8 10 12 9 6 11




import sys
sys.stdin = open('input.txt')
import collections


def four(datas, cnt):
    global q, ans
    if datas == result or datas == result[::-1]:
        ans = cnt
        return
    if cnt == 6:
        ans = -1
        return
    q += ([datas[0],datas[2],datas[1],datas[3]],
             [datas[1],datas[3],datas[0],datas[2]],
             [datas[2],datas[3],datas[0],datas[1]])
    target = q.popleft()
    four(target,cnt+1)

def six(datas, cnt):
    global q, ans
    if datas == result or datas == result[::-1]:
        ans = cnt
        return
    if cnt == 6:
        ans = -1
        return
    q += ([datas[0],datas[1],datas[3],datas[2],datas[4],datas[5]],
            [datas[0],datas[2],datas[4],datas[1],datas[3],datas[5]],
            [datas[1],datas[3],datas[5],datas[0],datas[2],datas[4]],
            [datas[2],datas[4],datas[5],datas[0],datas[1],datas[3]],
            [datas[3],datas[4],datas[5],datas[0],datas[1],datas[2]])
    target = q.popleft()
    six(target,cnt+1)

# def eight(datas, cnt):
#     global q, ans
#     if datas == result or datas == result[::-1]:
#         ans = cnt
#         return
#     if cnt == 6:
#         ans = -1
#         return
#     q += ([datas[0],datas[1],datas[2],datas[4],datas[3],datas[5],datas[6],datas[7]],
#           [datas[0],datas[1],datas[3],datas[5],datas[2],datas[4],datas[6],datas[7]],
#           [datas[0],datas[2],datas[4],datas[6],datas[1],datas[3],datas[5],datas[7]],
#           [datas[1],datas[3],datas[5],datas[7],datas[0],datas[2],datas[4],datas[6]],
#           [datas[2],datas[4],datas[6],datas[7],datas[0],datas[1],datas[3],datas[5]],
#           [datas[3],datas[5],datas[6],datas[7],datas[0],datas[1],datas[2],datas[4]],
#           [datas[4],datas[5],datas[6],datas[7],datas[0],datas[1],datas[2],datas[3]])
#     target = q.popleft()
#     eight(target,cnt+1)
#
# def ten(datas, cnt):
#     global q, ans
#     if datas == result or datas == result[::-1]:
#         ans = cnt
#         return
#     if cnt == 6:
#         ans = -1
#         return
#     q += ([datas[0],datas[1],datas[2],datas[3],datas[5],datas[4],datas[6],datas[7],datas[8],datas[9]],
#           [datas[0],datas[1],datas[2],datas[4],datas[6],datas[3],datas[5],datas[7],datas[8],datas[9]],
#           [datas[0],datas[1],datas[3],datas[5],datas[7],datas[2],datas[4],datas[6],datas[8],datas[9]],
#           [datas[0],datas[2],datas[4],datas[6],datas[8],datas[1],datas[3],datas[5],datas[7],datas[9]],
#           [datas[1],datas[3],datas[5],datas[7],datas[9],datas[0],datas[2],datas[4],datas[6],datas[8]],
#           [datas[2],datas[4],datas[6],datas[8],datas[9],datas[0],datas[1],datas[3],datas[5],datas[7]],
#           [datas[3],datas[5],datas[7],datas[8],datas[9],datas[0],datas[1],datas[2],datas[4],datas[6]],
#           [datas[4],datas[6],datas[7],datas[8],datas[9],datas[0],datas[1],datas[2],datas[3],datas[5]],
#           [datas[5],datas[6],datas[7],datas[8],datas[9],datas[0],datas[1],datas[2],datas[3],datas[4]])
#     target = q.popleft()
#     ten(target,cnt+1)
#
# def twlv(datas, cnt):
#     global q, ans
#     if datas == result or datas == result[::-1]:
#         ans = cnt
#         return
#     if cnt == 6:
#         ans = -1
#         return
#     q += ([datas[0],datas[1],datas[2],datas[3],datas[4],datas[6],datas[5],datas[7],datas[8],datas[9],datas[10],datas[11]],
#           [datas[0],datas[1],datas[2],datas[3],datas[5],datas[7],datas[4],datas[6],datas[8],datas[9],datas[10],datas[11]],
#           [datas[0],datas[1],datas[2],datas[4],datas[6],datas[8],datas[3],datas[5],datas[7],datas[9],datas[10],datas[11]],
#           [datas[0],datas[1],datas[3],datas[5],datas[7],datas[9],datas[2],datas[4],datas[6],datas[8],datas[10],datas[11]],
#           [datas[0],datas[2],datas[4],datas[6],datas[8],datas[10],datas[1],datas[3],datas[5],datas[7],datas[9],datas[11]],
#           [datas[1],datas[3],datas[5],datas[7],datas[9],datas[11],datas[0],datas[2],datas[4],datas[6],datas[8],datas[10]],
#           [datas[2],datas[4],datas[6],datas[8],datas[10],datas[11],datas[0],datas[1],datas[3],datas[5],datas[7],datas[9]],
#           [datas[3],datas[5],datas[7],datas[9],datas[10],datas[11],datas[0],datas[1],datas[2],datas[4],datas[6],datas[8]],
#           [datas[4],datas[6],datas[8],datas[9],datas[10],datas[11],datas[0],datas[1],datas[2],datas[3],datas[5],datas[7]],
#           [datas[5],datas[7],datas[8],datas[9],datas[10],datas[11],datas[0],datas[1],datas[2],datas[3],datas[4],datas[6]],
#           [datas[6],datas[7],datas[8],datas[9],datas[10],datas[11],datas[0],datas[1],datas[2],datas[3],datas[4],datas[5]],)
#     target = q.popleft()
#     twlv(target,cnt+1)


test = int(input())
for tc in range(test):
    case = int(input())
    datas = list(map(int,input().split()))

    result = sorted(datas)
    q = collections.deque([])
    ans = 0

    if case == 4:
        four(datas,0)
    elif case == 6:
        six(datas,0)
    # elif case == 8:
    #     eight(datas,0)
    # elif case == 10:
    #     ten(datas,0)
    # elif case == 12:
    #     twlv(datas,0)
    print(ans)