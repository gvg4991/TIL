# 마법사 상어와 파이어스톰
#
# 문제
# 마법사 상어는 파이어볼과 토네이도를 조합해 파이어스톰을 시전할 수 있다.
# 오늘은 파이어스톰을 크기가 2N × 2N인 격자로 나누어진 얼음판에서 연습하려고 한다.
# 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 얼음의 양을 의미한다.
# A[r][c]가 0인 경우 얼음이 없는 것이다.
#
# 파이어스톰을 시전하려면 시전할 때마다 단계 L을 결정해야 한다.
# 파이어스톰은 먼저 격자를 2L × 2L 크기의 부분 격자로 나눈다. 그 후, 모든 부분 격자를 시계 방향으로 90도 회전시킨다.
# 이후 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않은 칸은 얼음의 양이 1 줄어든다.
# (r, c)와 인접한 칸은 (r-1, c), (r+1, c), (r, c-1), (r, c+1)이다.
# 아래 그림의 칸에 적힌 정수는 칸을 구분하기 위해 적은 정수이다.
#
#
# 마법을 시전하기 전	L = 1	L = 2
# 마법사 상어는 파이어스톰을 총 Q번 시전하려고 한다. 모든 파이어스톰을 시전한 후, 다음 2가지를 구해보자.
#
# 남아있는 얼음 A[r][c]의 합
# 남아있는 얼음 중 가장 큰 덩어리가 차지하는 칸의 개수
# 얼음이 있는 칸이 얼음이 있는 칸과 인접해 있으면, 두 칸을 연결되어 있다고 한다. 덩어리는 연결된 칸의 집합이다.
#
# 입력
# 첫째 줄에 N과 Q가 주어진다. 둘째 줄부터 2N개의 줄에는 격자의 각 칸에 있는 얼음의 양이 주어진다.
# r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
#
# 마지막 줄에는 마법사 상어가 시전한 단계 L1, L2, ..., LQ가 순서대로 주어진다.
#
# 출력
# 첫째 줄에 남아있는 얼음 A[r][c]의 합을 출력하고, 둘째 줄에 가장 큰 덩어리가 차지하는 칸의 개수를 출력한다.
# 단, 덩어리가 없으면 0을 출력한다.
#
# 제한
# 2 ≤ N ≤ 6
# 1 ≤ Q ≤ 1,000
# 0 ≤ A[r][c] ≤ 100
# 0 ≤ Li ≤ N



import sys, collections
sys.stdin = open('input.txt')


def issafe(y,x):
    return 0<=y<2**size and 0<=x<2**size


size, test = map(int,input().split())
datas = list([0] for _ in range(2**size))
for row in range(2**size):
    datas[row] = list(map(int,input().split()))
case = list(map(int,input().split()))

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for tc in case:
    for y_part in range(0,2**size,2**tc):
        for x_part in range(0,2**size,2**tc):
            tmp = list([0]*(2**tc) for _ in range(2**tc))
            for y_p in range(2**tc):
                for x_p in range(2**tc):
                    tmp[x_p][2**tc-1-y_p] = datas[y_part+y_p][x_part+x_p]
            for y_p in range(2**tc):
                for x_p in range(2**tc):
                    datas[y_part+y_p][x_part+x_p] = tmp[y_p][x_p]
    # print(datas)
    water = []
    for row in range(2**size):
        for col in range(2**size):
            target = 0
            for dt in range(4):
                new_y = row+dy[dt]
                new_x = col+dx[dt]
                if issafe(new_y,new_x) and datas[new_y][new_x] > 0:
                    target += 1
                # if target == 3:
                #     break
            if target < 3 and datas[row][col] > 0:
                water.append([row,col])
    if water:
        for y,x in water:
            datas[y][x] -= 1\


# BFS
def ice(y,x):
    global total_ice, group
    target_ice = collections.deque([[y,x]])
    while target_ice:
        [target_y,target_x] = target_ice.popleft()
        total_ice += datas[target_y][target_x]
        visited[target_y][target_x] = 1
        ice_group[group] += 1
        for dt in range(4):
            next_y, next_x = target_y+dy[dt], target_x+dx[dt]
            if issafe(next_y,next_x) and not visited[next_y][next_x] and datas[next_y][next_x]:
                target_ice.append([next_y,next_x])
                visited[next_y][next_x] = 1


visited = [[0]*(2**size) for _ in range(2**size)]
total_ice = 0
ice_group = [0]*((2**size)**2)
group = 0
for y in range(2**size):
    for x in range(2**size):
        if not datas[y][x]:
            visited[y][x] = 1
        elif not visited[y][x]:
            ice(y,x)
            group += 1

print(total_ice)
print(max(ice_group))



# # DFS
# def ice(y,x):
#     global total_ice, group
#     if issafe(y,x) and not visited[y][x] and datas[y][x]:
#         total_ice += datas[y][x]
#         visited[y][x] = 1
#         ice_group[group] += 1
#         for dt in range(4):
#             next_y, next_x = y+dy[dt], x+dx[dt]
#             ice(next_y,next_x)
#
#
# visited = [[0]*(2**size) for _ in range(2**size)]
# total_ice = 0
# ice_group = [0]*(2**size)
# group = 0
# for y in range(2**size):
#     for x in range(2**size):
#         if not datas[y][x]:
#             visited[y][x] = 1
#         elif not visited[y][x]:
#             ice(y,x)
#             group += 1
#
# print(total_ice)
# print(max(ice_group))





