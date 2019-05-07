# 문제
# 인체에 치명적인 바이러스를 연구하던 연구소에 승원이가 침입했고, 바이러스를 유출하려고 한다.
# 바이러스는 활성 상태와 비활성 상태가 있다. 가장 처음에 모든 바이러스는 비활성 상태이고, 활성 상태인 바이러스는 상하좌우로 인접한 모든 빈 칸으로 모두 복제되며,
# 1초가 걸린다. 승원이는 연구소의 바이러스 M개를 활성 상태로 변경하려고 한다.
#
# 연구소는 크기가 N×N인 정사각형으로 나타낼 수 있으며, 정사각형은 1×1 크기의 정사각형으로 나누어져 있다.
# 연구소는 빈 칸, 벽, 바이러스로 이루어져 있으며, 벽은 칸 하나를 가득 차지한다. 활성 바이러스가 비활성 바이러스가 있는 칸으로 가면 비활성 바이러스가 활성으로 변한다.
#
# 예를 들어, 아래와 같이 연구소가 생긴 경우를 살펴보자. 0은 빈 칸, 1은 벽, 2는 바이러스의 위치이다.
#
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 2 0 1 1
# 0 1 0 0 0 0 0
# 2 1 0 0 0 0 2
# M = 3이고, 바이러스를 아래와 같이 활성 상태로 변경한 경우 6초면 모든 칸에 바이러스를 퍼뜨릴 수 있다.
# 벽은 -, 비활성 바이러스는 *, 활성 바이러스는 0, 빈 칸은 바이러스가 퍼지는 시간으로 표시했다.
#
# * 6 5 4 - - 2
# 5 6 - 3 - 0 1
# 4 - - 2 - 1 2
# 3 - 2 1 2 2 3
# 2 2 1 0 1 - -
# 1 - 2 1 2 3 4
# 0 - 3 2 3 4 *
# 시간이 최소가 되는 방법은 아래와 같고, 4초만에 모든 칸에 바이러스를 퍼뜨릴 수 있다.
#
# 0 1 2 3 - - 2
# 1 2 - 3 - 0 1
# 2 - - 2 - 1 2
# 3 - 2 1 2 2 3
# 3 2 1 0 1 - -
# 4 - 2 1 2 3 4
# * - 3 2 3 4 *
# 연구소의 상태가 주어졌을 때, 모든 빈 칸에 바이러스를 퍼뜨리는 최소 시간을 구해보자.
#
# 입력
# 첫째 줄에 연구소의 크기 N(4 ≤ N ≤ 50), 놓을 수 있는 바이러스의 개수 M(1 ≤ M ≤ 10)이 주어진다.
#
# 둘째 줄부터 N개의 줄에 연구소의 상태가 주어진다. 0은 빈 칸, 1은 벽, 2는 바이러스를 놓을 수 있는 위치이다. 2의 개수는 M보다 크거나 같고, 10보다 작거나 같은 자연수이다.
#
# 출력
# 연구소의 모든 빈 칸에 바이러스가 있게 되는 최소 시간을 출력한다. 바이러스를 어떻게 놓아도 모든 빈 칸에 바이러스를 퍼뜨릴 수 없는 경우에는 -1을 출력한다.


import sys
sys.stdin = open('input.txt')
from collections import deque

def combination(n,r,i,d):
    global comb
    if r == 0:
        comb.append(d)
        return
    if i == n:
        return
    combination(n,r-1,i+1,d+[start[i]])
    combination(n,r,i+1,d)

def issafe(y,x):
    return 0<=y<size and 0<=x<size


size, num = map(int,input().split())
datas = [[0]*size for _ in range(size)]
start = []
wall = []
for row in range(size):
    datas[row] = list(map(int,input().split()))
    for col in range(len(datas[row])):
        if datas[row][col] == 2:
            start.append((row,col))
        elif datas[row][col] == 1:
            wall.append((row,col))

# print(datas)
# print(start)

# 활성 바이러스 조합
comb = []
n = len(start)
r = num
i = 0
d = []
combination(n,r,i,d)
# print(comb)

# 확산
dy = [-1,0,1,0]
dx = [0,1,0,-1]
ans = 987654321
for begin in comb: #좌표 세개 들어있는 리스트
    q = deque([])
    visited = [[0]*size for _ in range(size)]
    result = [[-1]*size for _ in range(size)]
    for wy,wx in wall:
        result[wy][wx] = 'w'
    for vy,vx in start:
        result[vy][vx] = 'v'

    for y,x in begin:
        q.append((y,x))
        visited[y][x] = 1
        result[y][x] = 0
        # print(q)
    while q:
        y,x = q.popleft()

        if ans < result[y][x]+1:
            break

        end = True
        for row in result:
            if -1 in row:
                end = False
                break
        if end == True:
            break

    # peojida(y,x)
        for delta in range(4):
            new_y = y+dy[delta]
            new_x = x+dx[delta]
            if issafe(new_y,new_x) and not visited[new_y][new_x] and (datas[new_y][new_x] == 0 or datas[new_y][new_x] == 2):
                q.append((new_y,new_x))
                visited[new_y][new_x] = 1
                result[new_y][new_x] = result[y][x]+1
                # mountain = result[new_y][new_x]
    # print(result)
    target = 0
    change = True
    for row in result:
        if -1 in row:
            change = False
            break
        for val in row:
            if type(val) == int and target < val:
                target = val
    # print(target)
    if change == True and ans > target:
        ans = target
if ans == 987654321:
    ans = -1
    # print(ans)
print(ans)
