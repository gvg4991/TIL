# 문제
# 크기가 3×3인 배열 A가 있다. 1초가 지날때마다 배열에 연산이 적용된다.
#
# R 연산: 배열 A의 모든 행에 대해서 정렬을 수행한다. 행의 개수 ≥ 열의 개수인 경우에 적용된다.
# C 연산: 배열 A의 모든 열에 대해서 정렬을 수행한다. 행의 개수 < 열의 개수인 경우에 적용된다.
# 한 행 또는 열에 있는 수를 정렬하려면, 각각의 수가 몇 번 나왔는지 알아야 한다. 그 다음, 수의 등장 횟수가 커지는 순으로, 그러한 것이 여러가지면 수가 커지는 순으로 정렬한다.
# 그 다음에는 배열 A에 정렬된 결과를 다시 넣어야 한다. 정렬된 결과를 배열에 넣을 때는, 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저이다.
#
# 예를 들어, [3, 1, 1]에는 3이 1번, 1가 2번 등장한다. 따라서, 정렬된 결과는 [3, 1, 1, 2]가 된다. 다시 이 배열에는 3이 1번, 1이 2번, 2가 1번 등장한다. 다시 정렬하면 [2, 1, 3, 1, 1, 2]가 된다.
#
# 정렬된 결과를 배열에 다시 넣으면 행 또는 열의 크기가 커질 수 있다.
# R 연산이 적용된 경우에는 행의 크기가 가장 큰 행을 기준으로 모든 행의 크기가 커지고, C 연산이 적용된 경우에는 열의 크기가 가장 큰 열을 기준으로 모든 열의 크기가 커진다.
# 행 또는 열의 크기가 커진 곳에는 0이 채워진다. 수를 정렬할 때 0은 무시해야 한다. 예를 들어, [3, 2, 0, 0]을 정렬한 결과는 [3, 2]를 정렬한 결과와 같다.
#
# 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.
#
# 배열 A에 들어있는 수와 r, c, k가 주어졌을 때, A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간을 구해보자.
#
# 입력
# 첫째 줄에 r, c, k가 주어진다. (1 ≤ r, c, k ≤ 100)
#
# 둘째 줄부터 3개의 줄에 배열 A에 들어있는 수가 주어진다. 배열 A에 들어있는 수는 100보다 작거나 같은 자연수이다.
#
# 출력
# A[r][c]에 들어있는 값이 k가 되기 위한 연산의 최소 시간을 출력한다. 이 값이 100을 넘어가는 경우에는 -1을 출력한다.


import sys
sys.stdin = open('input.txt')


def col_change(d):
    global datas
    size = 0
    for row in range(len(datas)):
        # for val in datas[row]:
        values = sorted(list(set(datas[row])))
        if values[0] == 0:
            values.pop(0)
        check = [[0,0]]*len(values)
        for val_idx in range(len(values)):
            cnt = datas[row].count(values[val_idx])
            check[val_idx] = [values[val_idx],cnt]
        check.sort(key=lambda t:t[1])
        target = [0]*(2*len(values))
        for idx in range(len(check)):
            target[2*idx] = check[idx][0]
            target[2*idx+1] = check[idx][1]
        datas[row] = target
        if size < len(target):
            size = len(target)
    for row in range(len(datas)):
        if len(datas[row])<size:
            supply = size-len(datas[row])
            datas[row] = datas[row]+([0]*supply)
    return

def row_change(d):
    global datas
    datas = list(map(list,zip(*datas)))
    col_change(datas)
    datas = list(map(list,zip(*datas)))
    return


yy,xx,rr = map(int,input().split())
datas = [[0]*3 for _ in range(3)]
for row in range(3):
    datas[row] = list(map(int,input().split()))
# print(datas)

ans = 0
while ans<=100:
    if len(datas)>yy-1 and len(datas[0])>xx-1 and datas[yy-1][xx-1]==rr:
        break

    if len(datas)>=len(datas[0]):
        col_change(datas)
    elif len(datas)<len(datas[0]):
        row_change(datas)
    ans += 1

if ans > 100:
    ans = -1
print(ans)