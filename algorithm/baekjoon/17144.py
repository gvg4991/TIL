# 문제
# 미세먼지를 제거하기 위해 구사과는 공기청정기를 설치하려고 한다.
# 공기청정기의 성능을 테스트하기 위해 구사과는 집을 크기가 R×C인 격자판으로 나타냈고,
# 1×1 크기의 칸으로 나눴다. 구사과는 뛰어난 코딩 실력을 이용해 각 칸 (r, c)에 있는 미세먼지의 양을 실시간으로 모니터링하는 시스템을 개발했다.
# (r, c)는 r행 c열을 의미한다.
#
# 공기청정기는 항상 왼쪽 열에 설치되어 있고, 크기는 두 행을 차지한다.
# 공기청정기가 설치되어 있지 않은 칸에는 미세먼지가 있고, (r, c)에 있는 미세먼지의 양은 Ar,c이다.
# 1초 동안 아래 적힌 일이 순서대로 일어난다.
#
# 미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
# 공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.
# 다음은 확산의 예시이다.
#
# 왼쪽과 오른쪽에 칸이 없기 때문에, 두 방향으로만 확산이 일어났다.
#
# 인접한 네 방향으로 모두 확산이 일어난다.
#
# 공기청정기가 있는 칸으로는 확산이 일어나지 않는다.
#
# 공기청정기의 바람은 다음과 같은 방향으로 순환한다.
#
# 방의 정보가 주어졌을 때, T초가 지난 후 구사과의 방에 남아있는 미세먼지의 양을 구해보자.
#
# 입력
# 첫째 줄에 R, C, T (6 ≤ R, C ≤ 50, 1 ≤ T ≤ 1,000) 가 주어진다.
#
# 둘째 줄부터 R개의 줄에 Ar,c (-1 ≤ Ar,c ≤ 1,000)가 주어진다. 공기청정기가 설치된 곳은 Ar,c가 -1이고, 나머지 값은 미세먼지의 양이다.
# -1은 2번 위아래로 붙어져 있고, 가장 윗 행, 아랫 행과 두 칸이상 떨어져 있다.
#
# 출력
# 첫째 줄에 T초가 지난 후 구사과 방에 남아있는 미세먼지의 양을 출력한다.


import sys
sys.stdin = open('input.txt')
import copy

def issafe(y,x):
	return 0<=y<sero and 0<=x<garo

def peojida(y,x):
	for delta in range(4):
		new_y = y+dy[delta]
		new_x = x+dx[delta]
		if issafe(new_y,new_x) and not (new_y,new_x) in cleaner:
			peojim[new_y][new_x] += datas[y][x]//5
			peojim[y][x] -= datas[y][x]//5



# 공기 위치
sero, garo, sigan = map(int,input().split())
datas = [[0]*garo for _ in range(sero)]
cleaner = []
for row in range(sero):
	datas[row] = list(map(int,input().split()))
	if -1 in datas[row]:
		cleaner.append((row,0))
# print(datas)


#데이터 정의
# 먼지 이동 좌표
wi = []
wi_y,wi_x = cleaner[0]
for wi_r in range(1,garo-1):
	wi.append((wi_y,wi_r))
for wi_u in range(wi_y,-1,-1):
	wi.append((wi_u,garo-1))
for wi_l in range(garo-1-1,0,-1):
	wi.append((0,wi_l))
for wi_d in range(wi_y):
	wi.append((wi_d,0))
# print(wi)
arae = []
arae_y, arae_x = cleaner[1]
for arae_r in range(1,garo-1):
	arae.append((arae_y,arae_r))
for arae_d in range(arae_y,sero):
	arae.append((arae_d,garo-1))
for arae_l in range(garo-1-1,0,-1):
	arae.append((sero-1,arae_l))
for arae_u in range(sero-1,arae_y,-1):
	arae.append((arae_u,0))
# print(arae)
# 먼지 확산 변화량
dy = [-1,0,1,0]
dx = [0,1,0,-1]


for t in range(sigan):
	# 확산
	# dy = [-1,0,1,0]
	# dx = [0,1,0,-1]
	peojim = copy.deepcopy(datas)
	# peojim = [[0]*garo for _ in range(sero)]
	for y in range(sero):
		for x in range(garo):
			if datas[y][x] and not (y,x) in cleaner:
				peojida(y,x)
	# print(datas)
	# print(peojim)
	datas = copy.deepcopy(peojim)
	# print(datas)

	#이동
	# wi = []
	# wi_y,wi_x = cleaner[0]
	# for wi_r in range(1,garo-1):
	# 	wi.append((wi_y,wi_r))
	# for wi_u in range(wi_y,-1,-1):
	# 	wi.append((wi_u,garo-1))
	# for wi_l in range(garo-1-1,0,-1):
	# 	wi.append((0,wi_l))
	# for wi_d in range(wi_y):
	# 	wi.append((wi_d,0))
	# # print(wi)
	# arae = []
	# arae_y, arae_x = cleaner[1]
	# for arae_r in range(1,garo-1):
	# 	arae.append((arae_y,arae_r))
	# for arae_d in range(arae_y,sero):
	# 	arae.append((arae_d,garo-1))
	# for arae_l in range(garo-1-1,0,-1):
	# 	arae.append((sero-1,arae_l))
	# for arae_u in range(sero-1,arae_y,-1):
	# 	arae.append((arae_u,0))
	# # print(arae)
	for wi_next in range(len(wi)-1,0,-1):
		datas[wi[wi_next][0]][wi[wi_next][1]] = datas[wi[wi_next-1][0]][wi[wi_next-1][1]]
		datas[wi[wi_next-1][0]][wi[wi_next-1][1]] = 0
	for arae_next in range(len(arae)-1,0,-1):
		datas[arae[arae_next][0]][arae[arae_next][1]] = datas[arae[arae_next-1][0]][arae[arae_next-1][1]]
		datas[arae[arae_next-1][0]][arae[arae_next-1][1]] = 0
	# print(datas)

#남은 미세먼지 합
ans = 0
for dust in range(sero):
	ans += sum(datas[dust])
print(ans+2)


# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0




# import copy
#
# def issafe(y,x):
# 	return 0<=y<sero and 0<=x<garo
#
# def peojida(y,x):
# 	for delta in range(4):
# 		new_y = y+dy[delta]
# 		new_x = x+dx[delta]
# 		if issafe(new_y,new_x) and not (new_y,new_x) in cleaner:
# 			peojim[new_y][new_x] += datas[y][x]//5
# 			peojim[y][x] -= datas[y][x]//5
#
# sero, garo, sigan = map(int,input().split())
# datas = [[0]*garo for _ in range(sero)]
# cleaner = []
# for row in range(sero):
# 	datas[row] = list(map(int,input().split()))
# 	if -1 in datas[row]:
# 		cleaner.append((row,0))
# wi = []
# wi_y,wi_x = cleaner[0]
# for wi_r in range(1,garo-1):
# 	wi.append((wi_y,wi_r))
# for wi_u in range(wi_y,-1,-1):
# 	wi.append((wi_u,garo-1))
# for wi_l in range(garo-1-1,0,-1):
# 	wi.append((0,wi_l))
# for wi_d in range(wi_y):
# 	wi.append((wi_d,0))
# arae = []
# arae_y, arae_x = cleaner[1]
# for arae_r in range(1,garo-1):
# 	arae.append((arae_y,arae_r))
# for arae_d in range(arae_y,sero):
# 	arae.append((arae_d,garo-1))
# for arae_l in range(garo-1-1,0,-1):
# 	arae.append((sero-1,arae_l))
# for arae_u in range(sero-1,arae_y,-1):
# 	arae.append((arae_u,0))
# dy = [-1,0,1,0]
# dx = [0,1,0,-1]
#
#
# for t in range(sigan):
# 	peojim = copy.deepcopy(datas)
# 	for y in range(sero):
# 		for x in range(garo):
# 			if datas[y][x] and not (y,x) in cleaner:
# 				peojida(y,x)
# 	datas = copy.deepcopy(peojim)
#
# 	for wi_next in range(len(wi)-1,0,-1):
# 		datas[wi[wi_next][0]][wi[wi_next][1]] = datas[wi[wi_next-1][0]][wi[wi_next-1][1]]
# 		datas[wi[wi_next-1][0]][wi[wi_next-1][1]] = 0
# 	for arae_next in range(len(arae)-1,0,-1):
# 		datas[arae[arae_next][0]][arae[arae_next][1]] = datas[arae[arae_next-1][0]][arae[arae_next-1][1]]
# 		datas[arae[arae_next-1][0]][arae[arae_next-1][1]] = 0
#
# ans = 0
# for dust in range(sero):
# 	ans += sum(datas[dust])
# print(ans+2)
