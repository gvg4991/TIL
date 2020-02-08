# 문제
# 캐슬 디펜스는 성을 향해 몰려오는 적을 잡는 턴 방식의 게임이다.
# 게임이 진행되는 곳은 크기가 N×M인 격자판으로 나타낼 수 있다.
# 격자판은 1×1 크기의 칸으로 나누어져 있고, 각 칸에 포함된 적의 수는 최대 하나이다.
# 격자판의 N번행의 바로 아래(N+1번 행)의 모든 칸에는 성이 있다.
# 성을 적에게서 지키기 위해 궁수 3명을 배치하려고 한다.
# 궁수는 성이 있는 칸에 배치할 수 있고, 하나의 칸에는 최대 1명의 궁수만 있을 수 있다.
# 각각의 턴마다 궁수는 적 하나를 공격할 수 있고, 모든 궁수는 동시에 공격한다.
# 궁수가 공격하는 적은 거리가 D이하인 적 중에서 가장 가까운 적이고, 그러한 적이 여럿일 경우에는 가장 왼쪽에 있는 적을 공격한다.
# 같은 적이 여러 궁수에게 공격당할 수 있다. 공격받은 적은 게임에서 제외된다. 궁수의 공격이 끝나면, 적이 이동한다.
# 적은 아래로 한 칸 이동하며, 성이 있는 칸으로 이동한 경우에는 게임에서 제외된다. 모든 적이 격자판에서 제외되면 게임이 끝난다.
# 게임 설명에서 보다시피 궁수를 배치한 이후의 게임 진행은 정해져있다.
# 따라서, 이 게임은 궁수의 위치가 중요하다. 격자판의 상태가 주어졌을 때, 궁수의 공격으로 제거할 수 있는 적의 최대 수를 계산해보자.
# 격자판의 두 위치 (r1, c1), (r2, c2)의 거리는 |r1-r2| + |c1-c2|이다.
# 입력
# 첫째 줄에 격자판 행의 수 N, 열의 수 M, 궁수의 공격 거리 제한 D가 주어진다.
# 둘째 줄부터 N개의 줄에는 격자판의 상태가 주어진다. 0은 빈 칸, 1은 적이 있는 칸이다.
# 출력
# 첫째 줄에 궁수의 공격으로 제거할 수 있는 적의 최대 수를 출력한다.
# 제한
# 3 ≤ N, M ≤ 15
# 1 ≤ D ≤ 10


import sys
sys.stdin = open('input.txt')
import collections
import copy


def combination(n,r,i,c):
    if r == 0:
        comb.append(c)
        return
    if i<len(n):
        combination(n,r-1,i+1,c+[n[i]])
        combination(n,r,i+1,c)

def issafe(y,x):
    return 0<=y<sero and 0<=x<garo

def kill(y,x,dist): #지금은 k가 문제의 원인, 그리고 dist도 이용하기
    global flag
    if target[y][x]:
        result.append((y,x))
        return
    visited[y][x] = 1
    q.append((y,x))
    while q and flag==0 and visited[y][x]<=dist:
        y,x = q.popleft()
        # print(y,x)
        if not visited[y][x]+1<=dist:
            return

        for delta in range(3):
            new_y = y+dy[delta]
            new_x = x+dx[delta]
            if issafe(new_y,new_x) and not visited[new_y][new_x]: #and visited[y][x]+1<=dist
                if target[new_y][new_x]:
                    result.append((new_y,new_x))
                    flag = 1
                    break
                visited[new_y][new_x] = visited[y][x]+1
                q.append((new_y,new_x))


# 인풋받고 베이스데이터 만들기
sero,garo,dist = map(int,input().split())
datas = [[0]*garo for _ in range(sero)]
for row in range(sero):
    datas[row] = list(map(int,input().split()))
# print(datas)
# target = copy.deepcopy(datas)

#조합 함수에 넣기위한 데이터
n = [loca for loca in range(garo)] #가로줄 인덱스 리스트
# print(n)
comb = []
c = []
combination(n,3,0,c)
# print(comb)

#kill함수에 넣기위한 데이터
dy = [0,-1,0]
dx = [-1,0,1]
visited = [[0]*garo for _ in range(sero)]
q = collections.deque()
dq = collections.deque()
ans = 0


for loca_x in comb:
    target = copy.deepcopy(datas)
    result = []
    for loca_y in range(sero-1,-1,-1): #공수 위로 전진하기 전
        for killer in range(3):
            flag = 0
            visited = [[0] * garo for _ in range(sero)]
            q = dq
            kill(loca_y,loca_x[killer],dist)
        result = list(set(result))
        # print(result)
        for ty,tx in result:
            target[ty][tx] = 0
        # print(target)
    # print(result)
    if ans < len(result):
        ans = len(result)
print(ans)




























# import collections
# import copy
#
#
# def combination(n,r,i,c):
#     if r == 0:
#         comb.append(c)
#         return
#     if i<len(n):
#         combination(n,r-1,i+1,c+[n[i]])
#         combination(n,r,i+1,c)
#
# def issafe(y,x):
#     return 0<=y<sero and 0<=x<garo
#
# def kill(y,x,k): #지금은 k가 문제의 원인, 그리고 dist도 이용하기
#     global now_d, next_d
#     if target[y-1][x]:
#         result.append((y-1,x))
#         return
#     distance[now_d] = 1
#     q.append((y-1,x))
#     while q!=[] and k==0:
#         val = q.popleft()
#         y,x = val[0],val[1]
#         for delta in range(3):
#             new_y = y+dy[delta]
#             new_x = x+dx[delta]
#             if issafe(new_y,new_x) and not visited[new_y][new_x]:
#                 if target[new_y][new_x]:
#                     q.append((new_y,new_x))
#                     k = 1
#                     break
#                 visited[new_y][new_x] = 1
#                 next_d += 1
#                 distance[next_d] = distance[now_d] + 1
#         now_d += 1
#
#
#
#
# sero,garo,dist = map(int,input().split())
# datas = [[0]*garo for _ in range(sero)]
# for row in range(sero):
#     datas[row] = list(map(int,input().split()))
# # print(datas)
# # target = copy.deepcopy(datas)
#
# #조합 함수에 넣기위한 데이터
# n = [loca for loca in range(garo)] #가로줄 인덱스 리스트
# # print(n)
# comb = []
# c = []
# combination(n,3,0,c)
# # print(comb)
#
# #kill함수에 넣기위한 데이터
# dy = [0,-1,0]
# dx = [-1,0,1]
# visited = [[0]*garo for _ in range(sero)]
# distance = [0]*100
# now_d = next_d = 0
# q = collections.deque()
# result = []
# ans = 0
#
#
# for loca_x in comb:
#     target = copy.deepcopy(datas)
#     result = []
#     for loca_y in range(sero,0,-1):
#         for killer in range(3):
#             visited = [[0] * garo for _ in range(sero)]
#             distance = [0] * 100
#             now_d = next_d = 0
#             q = collections.deque()
#             kill(loca_y,loca_x[killer],dist)
#         result = list(set(result))
#         for ty,tx in result:
#             target[ty][tx] = 0
#         # print(target)
#     if ans < len(result):
#         ans = len(result)
# print(ans)


