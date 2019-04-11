# 문제
# N×N 크기의 공간에 물고기 M마리와 아기 상어 1마리가 있다. 공간은 1×1 크기의 정사각형 칸으로 나누어져 있다. 한 칸에는 물고기가 최대 1마리 존재한다.
# 아기 상어와 물고기는 모두 크기를 가지고 있고, 이 크기는 자연수이다. 가장 처음에 아기 상어의 크기는 2이고, 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동한다.
# 아기 상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있다.
# 아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있다. 따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있다.
# 아기 상어가 어디로 이동할지 결정하는 방법은 아래와 같다.
# 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다.
# 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최소값이다.
# 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
# 아기 상어의 이동은 1초 걸리고, 물고기를 먹는데 걸리는 시간은 없다고 가정한다.
# 즉, 아기 상어가 먹을 수 있는 물고기가 있는 칸으로 이동했다면, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면, 그 칸은 빈 칸이 된다.
# 아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때 마다 크기가 1 증가한다. 예를 들어, 크기가 2인 아기 상어는 물고기를 2마리 먹으면 크기가 3이 된다.
# 공간의 상태가 주어졌을 때, 아기 상어가 몇 초 동안 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는지 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 공간의 크기 N(2 ≤ N ≤ 20)이 주어진다.
# 둘째 줄부터 N개의 줄에 공간의 상태가 주어진다. 공간의 상태는 0, 1, 2, 3, 4, 5, 6, 9로 이루어져 있고, 아래와 같은 의미를 가진다.
# 0: 빈 칸
# 1, 2, 3, 4, 5, 6: 칸에 있는 물고기의 크기
# 9: 아기 상어의 위치
# 아기 상어는 공간에 한 마리 있다.
# 출력
# 첫째 줄에 아기 상어가 엄마 상어에게 도움을 요청하지 않고 물고기를 잡아먹을 수 있는 시간을 출력한다.


import sys
sys.stdin = open('input.txt')

def issafe(y,x):
    return 0<=y<n and 0<=x<n

# def find(y,x,t):
#     if datas[y][x] < t:
#         size[datas[y][x]] -= 1
#         size_cnt[datas[y][x]] += 1
#         if size_cnt[t] == t:
#             t += 1
#         find(y,x,t)
#
#     while q!=[]
#     y,x = q.pop(0)
#     for delta in range(4):
#         new_y = y + dy[delta]
#         new_x = x + dx[delta]
#         if issafe(new_y,new_x) and not visited[new_y][new_x] and datas[new_y][new_x]<=t:
#             visited[new_y][new_x] = visited[y][x]+1
#             q.append((new_y,new_x))


datas = []
size = [0,0,0,0,0,0,0]
size_cnt = [0,0,0,0,0,0,0]
n = int(input())
for row in range(n):
    r = list(map(int, input().split()))
    for val in r:
        if val != 9:
            size[val] += 1
        else:
            col = r.index(val)
            start_y,start_x = row,col
    datas.append(r)
t=2
# print(datas)
# print(one,two,three,four,five,six)
# print(start_y,start_x)

dy = [-1,0,0,1]
dx = [0,-1,1,0]
visited = [[0]*n for _ in range(n)]
# distance = [[0]*n for _ in range(n)]
result = []
ans = 0

q = [(start_y,start_x,t)]
while sum(size[1:t])!=0: #q != [] and
    y,x,t = q.pop(0)
    if 0 < datas[y][x] < t:
        size[datas[y][x]] -= 1
        size_cnt[datas[y][x]] += 1
        datas[y][x] = 0
        if size_cnt[t] == t:
            t += 1
        ans += visited[y][x]
        visited = [[0]*n for _ in range(n)]
        q=[]

    for delta in range(4):
        new_y = y + dy[delta]
        new_x = x + dx[delta]
        if issafe(new_y, new_x) and not visited[new_y][new_x] and datas[new_y][new_x] <= t:
            visited[new_y][new_x] = visited[y][x] + 1
            # distance[new_y][new_x] = distance[y][x] + 1
            q.append((new_y, new_x,t))
print(ans)




































































# def find(y, x, t):
#     if datas[y][x] < t:
#         if datas[y][x] == 1:
#             one -= 1
#             one_cnt += 1
#             if one_cnt >= 2:
#                 t += 1
#         elif datas[y][x] == 2:
#             two -= 1
#             two_cnt += 1
#         elif datas[y][x] == 3:
#             three -= 1
#             three_cnt += 1
#         elif datas[y][x] == 4:
#             four -= 1
#             four_cnt += 1
#         elif datas[y][x] == 5:
#             five -= 1
#             five_cnt += 1
#         elif datas[y][x] == 6:
#             six -= 1
#             six_cnt += 1
#         find(y, x, t)
#
#     for delta in range(4):
#         new_y = y + dy[delta]
#         new_x = x + dx[delta]
#         if issafe(new_y, new_x) and not visited[new_y][new_x] and datas[new_y][new_x] <= t:
#             visited[new_y][new_x] = visited[y][x] + 1
#             q.append((new_y, new_x))
#
#
# datas = []
# one = two = three = four = five = six = 0
# n = int(input())
# for row in range(n):
#     r = list(map(int, input().split()))
#     for val in r:
#         if val == 1:
#             one += 1
#         elif val == 2:
#             two += 1
#         elif val == 3:
#             three += 1
#         elif val == 4:
#             four += 1
#         elif val == 5:
#             five += 1
#         elif val == 6:
#             six += 1
#         elif val == 9:
#             col = r.index(val)
#             start_y, start_x = row, col
#     datas.append(r)
# # print(datas)
# # print(one,two,three,four,five,six)
# # print(start_y,start_x)
#
# dy = [-1, 0, 1, 0]
# dx = [0, -1, 0, 1]
# one_cnt = two_cnt = three_cnt = four_cnt = five_cnt = six_cnt = 0
# visited = [[0] * n for _ in range(n)]
# q = []
# result = []
# ans = 0