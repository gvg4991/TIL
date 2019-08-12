# 문제
# 부동산 투자로 억대의 돈을 번 상도는 최근 N×N 크기의 땅을 구매했다. 상도는 손쉬운 땅 관리를 위해 땅을 1×1 크기의 칸으로 나누어 놓았다.
# 각각의 칸은 (r, c)로 나타내며, r은 가장 위에서부터 떨어진 칸의 개수, c는 가장 왼쪽으로부터 떨어진 칸의 개수이다. r과 c는 1부터 시작한다.
#
# 상도는 전자통신공학과 출신답게 땅의 양분을 조사하는 로봇 S2D2를 만들었다. S2D2는 1×1 크기의 칸에 들어있는 양분을 조사해 상도에게 전송하고, 모든 칸에 대해서 조사를 한다. 가장 처음에 양분은 모든 칸에 5만큼 들어있다.
#
# 매일 매일 넓은 땅을 보면서 뿌듯한 하루를 보내고 있던 어느 날 이런 생각이 들었다.
#
# 나무 재테크를 하자!
#
# 나무 재테크란 작은 묘목을 구매해 어느정도 키운 후 팔아서 수익을 얻는 재테크이다. 상도는 나무 재테크로 더 큰 돈을 벌기 위해 M개의 나무를 구매해 땅에 심었다. 같은 1×1 크기의 칸에 여러 개의 나무가 심어져 있을 수도 있다.
#
# 이 나무는 사계절을 보내며, 아래와 같은 과정을 반복한다.
#
# 봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가한다. 각각의 나무는 나무가 있는 1×1 크기의 칸에 있는 양분만 먹을 수 있다.
# 하나의 칸에 여러 개의 나무가 있다면, 나이가 어린 나무부터 양분을 먹는다. 만약, 땅에 양분이 부족해 자신의 나이만큼 양분을 먹을 수 없는 나무는 양분을 먹지 못하고 즉시 죽는다.
#
# 여름에는 봄에 죽은 나무가 양분으로 변하게 된다. 각각의 죽은 나무마다 나이를 2로 나눈 값이 나무가 있던 칸에 양분으로 추가된다. 소수점 아래는 버린다.
#
# 가을에는 나무가 번식한다.
# 번식하는 나무는 나이가 5의 배수이어야 하며, 인접한 8개의 칸에 나이가 1인 나무가 생긴다. 어떤 칸 (r, c)와 인접한 칸은 (r-1, c-1), (r-1, c), (r-1, c+1), (r, c-1), (r, c+1), (r+1, c-1), (r+1, c), (r+1, c+1) 이다.
# 상도의 땅을 벗어나는 칸에는 나무가 생기지 않는다.
#
# 겨울에는 S2D2가 땅을 돌아다니면서 땅에 양분을 추가한다. 각 칸에 추가되는 양분의 양은 A[r][c]이고, 입력으로 주어진다.
#
# K년이 지난 후 상도의 땅에 살아있는 나무의 개수를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N, M, K가 주어진다.
#
# 둘째 줄부터 N개의 줄에 A배열의 값이 주어진다. r번째 줄의 c번째 값은 A[r][c]이다.
#
# 다음 M개의 줄에는 상도가 심은 나무의 정보를 나타내는 세 정수 x, y, z가 주어진다. 처음 두 개의 정수는 나무의 위치 (x, y)를 의미하고, 마지막 정수는 그 나무의 나이를 의미한다.
#
# 출력
# 첫째 줄에 K년이 지난 후 살아남은 나무의 수를 출력한다.
#
# 제한
# 1 ≤ N ≤ 10
# 1 ≤ M ≤ N2
# 1 ≤ K ≤ 1,000
# 1 ≤ A[r][c] ≤ 100
# 1 ≤ 입력으로 주어지는 나무의 나이 ≤ 10
# 입력으로 주어지는 나무의 위치는 모두 서로 다름


import sys
sys.stdin = open('input.txt')
import copy

size, tree, year = map(int,input().split())
yangboon = [[5]*size for _ in range(size)]
supply = [[0] for _ in range(size)]
for row in range(size):
    supply[row] = list(map(int,input().split()))
datas = [[[] for ___ in range(size)] for __ in range(size) for _ in range(size)]
# print(datas)
for cnt in range(tree):
    y,x,age = map(int,input().split())
    datas[y-1][x-1].append(age)
# print(datas)

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
while year != 0:
    dtree = [[0]*size for _ in range(size)]
    #봄
    for sero in range(size):
        for garo in range(size):
            die = 0
            target = []
            beonsik = 0
            if datas[sero][garo]:
                for namu in range(len(datas[sero][garo])):
                    if yangboon[sero][garo] >= datas[sero][garo][namu]: #양분이 나무 나이보다 많을 경우
                        yangboon[sero][garo] -= datas[sero][garo][namu] #양문을 먹고
                        target.append(datas[sero][garo][namu] + 1) #나이 한살 먹음
                        if (datas[sero][garo][namu] + 1)%5 == 0:
                            beonsik += 1
                    else:
                        die += datas[sero][garo][namu]//2 #나이의 반만큼 양분을 남김
                datas[sero][garo] = copy.copy(target) #죽은 나무 제거(살아있는 나무만 남김)
    #여름
                yangboon[sero][garo] += die #죽은 나무들의 양분을 땅에 공급
    #가을
                if beonsik:
                    for b in range(beonsik):
                        for delta in range(8):
                            if 0 <= (sero+dy[delta]) < size and 0 <= (garo+dx[delta]) < size:
                                dtree[sero+dy[delta]][garo+dx[delta]] += 1
    #겨울
            yangboon[sero][garo] += supply[sero][garo] #땅에 양분 공급

    #가을 번식
    for sero in range(size):
        for garo in range(size):
            if dtree[sero][garo]:
                for t in range(dtree[sero][garo]):
                    datas[sero][garo].append(1)
                datas[sero][garo] = sorted(datas[sero][garo])
    year -= 1
    # print(datas)

ans = 0
for sero in range(size):
    for garo in range(size):
        ans += len(datas[sero][garo])
print(ans)














# s,c,t = map(int,input().split())
# datas = [[5]*s for _ in range(s)] #양분량
# supply = [[0]*s for _ in range(s)] #추가되는 양분 크기
# for row in range(s):
#     supply[row] = list(map(int,input().split()))
# trees = [[[] for i in range(s)] for _ in range(s)] #나무나이(아마 필요없을수도! why? 같은 위치에 여러 나무가 존재)
# # tree_datas = [] # 나무들 정보(x,y,나이)
# for cnt in range(c):
#     y,x,a = map(int,input().split())
#     trees[y-1][x-1].append(a)
#     trees[y-1][x-1].sort()
# # print(trees)
#
# for sero in range(s):
#     for garo in range(s):
#         death = False
#         for idx in range(len(trees[sero][garo])):
#             if death == False and trees[sero][garo][idx] <= datas[sero][garo]:
#                 datas[sero][garo] -= trees[sero][garo][idx]
#                 trees[sero][garo][idx] += 1
#             else:
#                 death = True
#                 datas[sero][garo] += trees[sero][garo][idx]//2
















































#
# s,c,t = map(int,input().split())
# datas = [[5]*s for _ in range(s)] #양분량
# supply = [[0]*s for _ in range(s)] #추가되는 양분 크기
# for row in range(s):
#     supply[row] = list(map(int,input().split()))
# trees = [[[0]]*s for _ in range(s)] #나무나이(아마 필요없을수도! why? 같은 위치에 여러 나무가 존재)
# # tree_datas = [] # 나무들 정보(x,y,나이)
# for cnt in range(c):
#     x,y,a = map(int,input().split())
#     trees[y][x].append(a)
#     # tree_datas.append((x,y,a))
# # print(supply)
# # print(datas)
#
# # while t != 0:
# #     trees.sort(key=lambda t:t[2])
# #     for ti in range(len(trees)):
# #         tx,ty,ta = trees[ti]
# #         if datas[ty][tx] >= ta:
# #             datas[ty][tx] -= ta #나이만큼 양분 먹기
# #             trees[ti][2] += 1 #나이 1 증가
# #         else:

























































#
# import collections
# N,M,K = list(map(int,input().split()))
#
# charge_data_map=[]
# for n in range(N):
#     line = list(map(int,input().split()))
#     charge_data_map.append(line)
#
# namu_map=[]
# for n in range(N):
#     line = [0]*N
#     namu_map.append(line)
# for y in range(N):
#     for x in range(N):
#         namu_map[y][x]=collections.deque()
#
# namu_fuel_map=[]
# for n in range(N):
#     line = [5]*N
#     namu_fuel_map.append(line)
#
# dead_namu_map=[]
# for n in range(N):
#     line = [0]*N
#     dead_namu_map.append(line)
# ##초기 나무심기
# for m in range(M):
#     line=list(map(int,input().split()))
#     namu_map[line[0]-1][line[1]-1].appendleft(line[2])
#
# def spring_act():
#     global N
#     ##나무가 자기 나이만큼 양분 먹고, 나이 1 증가, 나이 어린순으로 양분 먹기, 나이만큼 양분 못먹으면 뒤짐
#
#     for y in range(0,N):
#         for x in range(0,N):
#             if namu_map[y][x]: ## 나무가 있는 칸이라면
#                 temp=collections.deque()
#                 while(namu_map[y][x]):
#                     if namu_fuel_map[y][x] - namu_map[y][x][0] >=0: ## 지금 나무가 더 성장할 수 있으면
#                         namu_fuel_map[y][x] = namu_fuel_map[y][x] - namu_map[y][x][0] ## 토지 연료 깎아내리고
#                         next=namu_map[y][x].popleft()
#                         temp.append(next+1)
#                     else: ## 이놈 양분 줬을때 연료가 0보다 떨어지는 경우
#                         break
#                 dead_namu_map[y][x]=namu_map[y][x] ## 양분 후보로 넣어주기
#                 namu_map[y][x]=temp ## 나무 상황 갱신
#     return
#
# def summer_act(): ##뒤진 나무는 양분으로 추가
#     global N
#
#     for y in range(N):
#         for x in range(N):
#             if dead_namu_map[y][x]!=0:
#                 while(dead_namu_map[y][x]):
#                     now=dead_namu_map[y][x].pop()
#                     namu_fuel_map[y][x]=namu_fuel_map[y][x]+now//2
#                 dead_namu_map[y][x]=0
#     return
#
# def is_safe(Y,X):
#     global N
#     if -1<Y<N and -1<X<N:
#         return True
#     else:
#         return False
#
# dy=[-1,-1,0,1,1,1,0,-1]
# dx=[0,1,1,1,0,-1,-1,-1]
# def fall_act(): ## 5의 배수 8방향 번식
#     global N
#
#     for y in range(N):
#         for x in range(N): ## 전 셀 돌기
#             for i in range(len(namu_map[y][x])):## 이 셀에서, deque 전부 확인해서 5의 배수 확인
#                 if namu_map[y][x][i]!=0 and namu_map[y][x][i]%5==0: ## 5의 배수라면 번식 ㄱㄱ
#                     for dir in range(0,8): ## 8 방향 번식 시작
#                         if is_safe(y+dy[dir],x+dx[dir]):
#                             namu_map[y+dy[dir]][x+dx[dir]].appendleft(1)
#     return
#
# def winter_act(): ## 초기 셋팅 만큼 연료충전
#     global N
#
#     for y in range(N):
#         for x in range(N):
#             namu_fuel_map[y][x] = namu_fuel_map[y][x]+charge_data_map[y][x]
#     return
#
# t=0
# while(1): ## 1년
#
#     if t==K:
#         break
#     spring_act()
#     summer_act()
#     fall_act()
#     winter_act()
#
#     t = t + 1
#
# tree_num=0
# for y in range(N):
#     for x in range(N):
#         tree_num=tree_num+len(namu_map[y][x])
#
# print(tree_num)
