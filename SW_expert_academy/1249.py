# 2차 세계 대전에서 연합군과 독일군의 전투가 점점 치열해지고 있다.
# 전투가 진행중인 지역은 대규모 폭격과 시가전 등으로 인해 도로 곳곳이 파손된 상태이다.
# 그림 1(a)에서와 같이 도로들은 전투로 인해 트럭이나 탱크와 같은 차량들이 지날 갈 수 없다.
# 전투에서 승리하기 위해서는 기갑사단과 보급부대가 신속하게 이동하기 위한 도로가 있어야 한다.
# 공병대는 출발지(S) 에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려고 한다.
# 도로가 파여진 깊이에 비례해서 복구 시간은 증가한다.
# 출발지에서 도착지까지 가는 경로 중에 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하시오.
# 깊이가 1이라면 복구에 드는 시간이 1이라고 가정한다.
# 지도 정보는 그림1(b)와 같이 2차원 배열 형태로 표시된다.
# 출발지는 좌상단의 칸(S)이고 도착지는 우하단의 칸(G)가 된다.
# 이동 경로는 상하좌우 방향으로 진행할 수 있으며, 한 칸씩 움직일 수 있다.
# 지도 정보에는 각 칸마다 파여진 도로의 깊이가 주어진다. 현재 위치한 칸의 도로를 복구해야만 다른 곳으로 이동할 수 있다.
# 그림 2 지도 정보
# 이동하는 시간에 비해 복구하는데 필요한 시간은 매우 크다고 가정한다.
# 따라서, 출발지에서 도착지까지 거리에 대해서는 고려할 필요가 없다.
# 지도 정보는 그림2에서 보듯이 2차원 배열의 형태이다.
# 출발지(S)와 도착지(G)는 좌상단과 우하단이 되고 입력 데이터에서는 0으로 표시된다.
# 출발지와 도착지를 제외한 곳이 0인 것은 복구 작업이 불필요한 곳이다.
# 다음과 같은 지도에서 복구 작업 시간이 최소인 시간은 2이고 회색으로 칠해진 경로가 된다.
# [입력]
# 가장 첫 줄은 전체 테스트케이스의 수이다.
# 각 테스트 케이스마다 지도의 크기(N x N)가 주어진다. 지도의 크기는 최대 100 x 100이다.
# 그 다음줄 부터 지도의 크기만큼 2차원 배열 형태의 지도 정보가 주어진다.
# [출력]
# 각 테스트 케이스의 답을 순서대로 출력하며, 각 케이스마다 줄의 시작에 “#C”를 출력하여야 한다.
# 이때 C는 케이스의 번호이다.
# 같은 줄에 빈 칸을 하나 두고, 주어진 입력에서 출발지에서 도착지까지 가는 경로 중에 복구 작업에 드는 시간이 가장 작은 경로의 복구 시간을 출력하시오.


import sys
sys.stdin = open('input.txt')


def issafe(y,x):
    if 0<=y<n and 0<=x<n:
        return True
    else:
        return False


def lego(y,x):
    global ans, result
    visited[y][x] = 1
    if y==n-1 and x==n-1 and ans > result:
        ans = result
        return
    for delta in range(4):
        new_y = y + dy[delta]
        new_x = x + dx[delta]
        if issafe(new_y,new_x) and visited[new_y][new_x]==0 and result + datas[new_y][new_x] < ans and distance[new_y][new_x] > result + datas[new_y][new_x]:
            now_y = new_y
            now_x = new_x
            result += datas[now_y][now_x]
            distance[now_y][now_x] = distance[y][x]+datas[now_y][now_x]
            lego(now_y,now_x)
            result -= datas[now_y][now_x]
            visited[now_y][now_x] = 0
    return


test = int(input())
for tc in range(test):
    n = int(input())
    datas = [[0]*n for _ in range(n)]
    for case in range(n):
        datas[case] = list(map(int,input()))
    # print(datas)

    dy = [0,1,0,-1] #우하좌상
    dx = [1,0,-1,0] #하우상좌
    visited = [[0]*n for _ in range(n)]
    distance = [[99999]*n for _ in range(n)]
    result = 0
    ans = 99999


    lego(0,0)
    print('#{} {}'.format(tc+1,ans))


