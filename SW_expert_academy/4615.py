# 오셀로라는 게임은 흑돌과 백돌을 가진 사람이 번갈아가며 보드에 돌을 놓아서 최종적으로 보드에 자신의 돌이 많은 사람이 이기는 게임이다.
# 보드는 4x4, 6x6, 8x8(가로, 세로 길이) 크기를 사용한다. 6x6 보드에서 게임을 할 때, 처음에 플레이어는 다음과 같이 돌을 놓고 시작한다(B : 흑돌, W : 백돌).
# 4x4, 8x8 보드에서도 동일하게 정가운데에 아래와 같이 배치하고 시작한다.
# 그리고 흑, 백이 번갈아가며 돌을 놓는다.
# 처음엔 흑부터 시작하는데 이 때 흑이 돌을 놓을 수 있는 곳은 다음과 같이 4군데이다.
# 플레이어는 빈공간에 돌을 놓을 수 있다.
# 단, 자신이 놓을 돌과 자신의 돌 사이에 상대편의 돌이 있을 경우에만 그 곳에 돌을 놓을 수 있고, 그 때의 상대편의 돌은 자신의 돌로 만들 수 있다.
#  (여기에서 "사이"란 가로/세로/대각선을 의미한다.)
#  (2, 3) 위치에 흑돌을 놓은 후의 보드는 다음과 같다.
# 이런 식으로 번갈아가며 흑, 백 플레이어가 돌을 놓는다.
# 만약 돌을 놓을 곳이 없다면 상대편 플레이어가 다시 돌을 놓는다.
# 보드에 빈 곳이 없거나 양 플레이어 모두 돌을 놓을 곳이 없으면 게임이 끝나고 그 때 보드에 있는 돌의 개수가 많은 플레이어가 승리하게 된다.
#  [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 보드의 한 변의 길이 N과 플레이어가 돌을 놓는 횟수 M이 주어진다. N은 4, 6, 8 중 하나이다.
# 그 다음 M줄에는 돌을 놓을 위치와 돌의 색이 주어진다.
# 돌의 색이 1이면 흑돌, 2이면 백돌이다.
# 만약 3 2 1이 입력된다면 (3, 2) 위치에 흑돌을 놓는 것을 의미한다.
# 돌을 놓을 수 없는 곳은 입력으로 주어지지 않는다.
#  [출력]
# 각 테스트 케이스마다 게임이 끝난 후 보드 위의 흑돌, 백돌의 개수를 출력한다.
# 흑돌이 30개, 백돌이 34인 경우 30 34를 출력한다.


import sys
sys.stdin = open("input.txt")


def issafe(y,x):
    global n
    if x >= 0 and x < n and y >= 0 and y < n:
        return True
    else:
        return False

def u(y,x,bw):
    new_y = y-1
    new_x = x
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def ur(y,x,bw):
    new_y = y-1
    new_x = x+1
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def r(y,x,bw):
    new_y = y
    new_x = x+1
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def dr(y,x,bw):
    new_y = y+1
    new_x = x+1
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def d(y,x,bw):
    new_y = y+1
    new_x = x
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def dl(y,x,bw):
    new_y = y+1
    new_x = x-1
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def l(y,x,bw):
    new_y = y
    new_x = x-1
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def ul(y,x,bw):
    new_y = y-1
    new_x = x-1
    change = False
    if bw == 1:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 1
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            change = True
        return
    elif bw == 2:
        if issafe(new_y, new_x) and mygame[new_y][new_x] == 1:
            u(new_y,new_x)
            if change == True:
                mygame[new_y][new_x] = 2
        elif issafe(new_y, new_x) and mygame[new_y][new_x] == 2:
            change = True
        return

def othello(y,x,bw):
    if issafe(new_y, new_x) and bw == 1:
        if mygame[new_y][new_x] == 2:
            now_y = new_y
            now_x = new_x

# def othello(y,x,bw):
#     for delta in range(8):
#         new_y = y + dy[delta]
#         new_x = x + dx[delta]
#         if issafe(new_y, new_x) and bw == 1:
#             if mygame[new_y][new_x] == 2:
#                 now_y = new_y
#                 now_x = new_x


                othello(now_y,now_x,)

            path_q.append((y, x))
            distance[y][x] = distance[now_y][now_x] + 1


test = int(input())
for tc in range(test):
    n,m = map(int,input().split())
    mygame = [[0]*n for i in range(n)]
    mygame[n//2][n//2] = mygame[n//2+1][n//2+1] = 2
    mygame[n//2][n//2+1] = mygame[n//2+1][n//2] = 1
    datas = []
    for case in range(m):
        datas.append(list(map(int,input().split())))
    dy = [-1,-1,0,1,1,1,0,-1]
    dx = [0,1,1,1,0,-1,-1,-1]
    for data in datas:
        mygame[data[0]-1,data[1]-1] = data[2]
        othello(data[0]-1,data[1]-1,data[2])
