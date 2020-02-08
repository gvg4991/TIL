# 스타트링크의 사무실은 1×1크기의 정사각형으로 나누어져 있는 N×M 크기의 직사각형으로 나타낼 수 있다.
# # 사무실에는 총 K개의 CCTV가 설치되어져 있는데, CCTV는 5가지 종류가 있다. 각 CCTV가 감시할 수 있는 방법은 다음과 같다.
# #
# #
# # 1번	2번	3번	4번	5번
# # 1번 CCTV는 한 쪽 방향만 감시할 수 있다. 2번과 3번은 두 방향을 감시할 수 있는데, 2번은 감시하는 방향이 서로 반대방향이어야 하고, 3번은 직각 방향이어야 한다.
# # 4번은 세 방향, 5번은 네 방향을 감시할 수 있다.
# #
# # CCTV는 감시할 수 있는 방향에 있는 칸 전체를 감시할 수 있다. 사무실에는 벽이 있는데, CCTV는 벽을 통과할 수 없다.
# # CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
# #
# # CCTV는 회전시킬 수 있는데, 회전은 항상 90도 방향으로 해야 하며, 감시하려고 하는 방향이 가로 또는 세로 방향이어야 한다.
# #
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # 0 0 1 0 6 0
# # 0 0 0 0 0 0
# # 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV의 번호이다. 위의 예시에서 1번의 방향에 따라 감시할 수 있는 영역을 '#'로 나타내면 아래와 같다.
# #
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # 0 0 1 # 6 0
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # # # 1 0 6 0
# # 0 0 0 0 0 0
# # 0 0 # 0 0 0
# # 0 0 # 0 0 0
# # 0 0 1 0 6 0
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # 0 0 0 0 0 0
# # 0 0 1 0 6 0
# # 0 0 # 0 0 0
# # →	←	↑	↓
# # CCTV는 벽을 통과할 수 없기 때문에, 1번이 → 방향을 감시하고 있을 때는 6의 오른쪽에 있는 벽을 감시할 수 없다.
# #
# # 0 0 0 0 0 0
# # 0 2 0 0 0 0
# # 0 0 0 0 6 0
# # 0 6 0 0 2 0
# # 0 0 0 0 0 0
# # 0 0 0 0 0 5
# # 위의 예시에서 감시할 수 있는 방향을 알아보면 아래와 같다.
# #
# # 0 0 0 0 0 #
# # # 2 # # # #
# # 0 0 0 0 6 #
# # 0 6 # # 2 #
# # 0 0 0 0 0 #
# # # # # # # 5
# # 0 0 0 0 0 #
# # # 2 # # # #
# # 0 0 0 0 6 #
# # 0 6 0 0 2 #
# # 0 0 0 0 # #
# # # # # # # 5
# # 0 # 0 0 0 #
# # 0 2 0 0 0 #
# # 0 # 0 0 6 #
# # 0 6 # # 2 #
# # 0 0 0 0 0 #
# # # # # # # 5
# # 0 # 0 0 0 #
# # 0 2 0 0 0 #
# # 0 # 0 0 6 #
# # 0 6 0 0 2 #
# # 0 0 0 0 # #
# # # # # # # 5
# # 왼쪽 상단 2: ↔, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↔, 오른쪽 하단 2: ↕
# # 왼쪽 상단 2: ↕, 오른쪽 하단 2: ↔	왼쪽 상단 2: ↕, 오른쪽 하단 2: ↕
# # CCTV는 CCTV를 통과할 수 있다. 아래 예시를 보자.
# #
# # 0 0 2 0 3
# # 0 6 0 0 0
# # 0 0 6 6 0
# # 0 0 0 0 0
# # 위와 같은 경우에 2의 방향이 ↕ 3의 방향이 ←와 ↓인 경우 감시받는 영역은 다음과 같다.
# #
# # # # 2 # 3
# # 0 6 # 0 #
# # 0 0 6 6 #
# # 0 0 0 0 #
# # 사무실의 크기와 상태, 그리고 CCTV의 정보가 주어졌을 때, CCTV의 방향을 적절히 정해서, 사각 지대의 최소 크기를 구하는 프로그램을 작성하시오.
# #
# # 입력
# # 첫째 줄에 사무실의 세로 크기 N과 가로 크기 M이 주어진다. (1 ≤ N, M ≤ 8)
# #
# # 둘째 줄부터 N개의 줄에는 사무실 각 칸의 정보가 주어진다. 0은 빈 칸, 6은 벽, 1~5는 CCTV를 나타내고, 문제에서 설명한 CCTV의 종류이다.
# #
# # CCTV의 최대 개수는 8개를 넘지 않는다.
# #
# # 출력
# # 첫째 줄에 사각 지대의 최소 크기를 출력한다.


import sys
sys.stdin = open('input.txt')
import copy

def issafe(y,x):
    return 0<=x<garo and 0<=y<sero

def right(y,x):
    global result
    if not issafe(y,x) or datas[y][x] == 6:
        return
    if not visited[y][x]:
        visited[y][x] = 1
        result += 1
        right(y,x+1)
    else:
        right(y,x+1)

def left(y,x):
    global result
    if not issafe(y,x) or datas[y][x] == 6:
        return
    if not visited[y][x]:
        visited[y][x] = 1
        result += 1
        left(y,x-1)
    else:
        left(y,x-1)

def up(y,x):
    global result
    if not issafe(y,x) or datas[y][x] == 6:
        return
    if not visited[y][x]:
        visited[y][x] = 1
        result += 1
        up(y-1,x)
    else:
        up(y-1,x)

def down(y,x):
    global result
    if not issafe(y,x) or datas[y][x] == 6:
        return
    if not visited[y][x]:
        visited[y][x] = 1
        result += 1
        down(y+1,x)
    else:
        down(y+1,x)

def watch(y,x,c,n,visited,target):
    global ans, result

    already = copy.deepcopy(visited)
    # target = result
    print(visited)
    if n == (len(cctv)-1): #마지막 CCTV면
        if c == 1:
            right(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            left(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            up(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            down(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
        elif c == 2:
            right(y,x)
            left(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            up(y,x)
            down(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
        elif c == 3:
            right(y,x)
            up(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            right(y,x)
            down(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            left(y,x)
            down(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            left(y,x)
            up(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
        elif c == 4:
            left(y,x)
            up(y,x)
            right(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            up(y,x)
            right(y,x)
            down(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            right(y,x)
            down(y,x)
            left(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
            down(y,x)
            left(y,x)
            up(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
        elif c == 5:
            up(y,x)
            right(y,x)
            left(y,x)
            down(y,x)
            if ans > (garo*sero-result):
                ans = garo*sero-result
            visited = copy.deepcopy(already)
            result = target
        return

    if c == 1:
        right(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        left(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        up(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        down(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
    elif c == 2:
        right(y,x)
        left(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        up(y,x)
        down(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
    elif c == 3:
        right(y,x)
        up(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        right(y,x)
        down(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        left(y,x)
        down(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        left(y,x)
        up(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
    elif c == 4:
        left(y,x)
        up(y,x)
        right(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        up(y,x)
        right(y,x)
        down(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        right(y,x)
        down(y,x)
        left(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
        down(y,x)
        left(y,x)
        up(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target
    elif c == 5:
        up(y,x)
        right(y,x)
        left(y,x)
        down(y,x)
        watch(cctv[n+1][0],cctv[n+1][1],cctv[n+1][2],n+1,visited,result)
        visited = copy.deepcopy(already)
        result = target




sero, garo = map(int,input().split())
datas = [[0] for _ in range(sero)]
# one = []
# two = []
# three = []
# four = []
# five = []
cctv = []
six = []
visited = [[0]*garo for _ in range(sero)]
result = 0
ans = garo*sero
for row in range(sero):
    datas[row] = list(map(int,input().split()))
    for col in range(garo):
        if datas[row][col] == 1:
            # one.append((row,col))
            cctv.append((row,col,1))
            visited[row][col] = 1
            result += 1
        elif datas[row][col] == 2:
            # two.append((row,col))
            cctv.append((row,col,2))
            visited[row][col] = 1
            result += 1
        elif datas[row][col] == 3:
            # three.append((row,col))
            cctv.append((row,col,3))
            visited[row][col] = 1
            result += 1
        elif datas[row][col] == 4:
            # four.append((row,col))
            cctv.append((row,col,4))
            visited[row][col] = 1
            result += 1
        elif datas[row][col] == 5:
            # five.append((row,col))
            cctv.append((row,col,5))
            visited[row][col] = 1
            result += 1
        elif datas[row][col] == 6:
            six.append((row,col))
            visited[row][col] = 1
            result += 1
# print(datas)
# print(cctv)
# print(visited)
# print(result)

# print(cctv[0][0])
if len(cctv):
    watch(cctv[0][0],cctv[0][1],cctv[0][2],0,visited,result)
print(ans)
