# 문제
# 재현이는 주변을 살펴보던 중 체스판과 말을 이용해서 새로운 게임을 만들기로 했다.
# 새로운 게임은 크기가 N×N인 체스판에서 진행되고, 사용하는 말의 개수는 K개이다. 말은 원판모양이고, 하나의 말 위에 다른 말을 올릴 수 있다.
# 체스판의 각 칸은 흰색, 빨간색, 파란색 중 하나로 색칠되어있다.
#
# 게임은 체스판 위에 말 K개를 놓고 시작한다. 말은 1번부터 K번까지 번호가 매겨져 있고, 이동 방향도 미리 정해져 있다.
# 이동 방향은 위, 아래, 왼쪽, 오른쪽 4가지 중 하나이다.
#
# 턴 한 번은 1번 말부터 K번 말까지 순서대로 이동시키는 것이다. 한 말이 이동할 때 위에 올려져 있는 말도 함께 이동한다.
# 말의 이동 방향에 있는 칸에 따라서 말의 이동이 다르며 아래와 같다. 턴이 진행되던 중에 말이 4개 이상 쌓이는 순간 게임이 종료된다.
#
# A번 말이 이동하려는 칸이
# 흰색인 경우에는 그 칸으로 이동한다. 이동하려는 칸에 말이 이미 있는 경우에는 가장 위에 A번 말을 올려놓는다.
# A번 말의 위에 다른 말이 있는 경우에는 A번 말과 위에 있는 모든 말이 이동한다.
# 예를 들어, A, B, C로 쌓여있고, 이동하려는 칸에 D, E가 있는 경우에는 A번 말이 이동한 후에는 D, E, A, B, C가 된다.
# 빨간색인 경우에는 이동한 후에 A번 말과 그 위에 있는 모든 말의 쌓여있는 순서를 반대로 바꾼다.
# A, B, C가 이동하고, 이동하려는 칸에 말이 없는 경우에는 C, B, A가 된다.
# A, D, F, G가 이동하고, 이동하려는 칸에 말이 E, C, B로 있는 경우에는 E, C, B, G, F, D, A가 된다.
# 파란색인 경우에는 A번 말의 이동 방향을 반대로 하고 한 칸 이동한다. 방향을 반대로 바꾼 후에 이동하려는 칸이 파란색인 경우에는 이동하지 않고 가만히 있는다.
# 체스판을 벗어나는 경우에는 파란색과 같은 경우이다.
# 다음은 크기가 4×4인 체스판 위에 말이 4개 있는 경우이다.
#
#
#
# 첫 번째 턴은 다음과 같이 진행된다.
#
#
# 두 번째 턴은 다음과 같이 진행된다.
#
#
# 체스판의 크기와 말의 위치, 이동 방향이 모두 주어졌을 때, 게임이 종료되는 턴의 번호를 구해보자.
#
# 입력
# 첫째 줄에 체스판의 크기 N, 말의 개수 K가 주어진다. 둘째 줄부터 N개의 줄에 체스판의 정보가 주어진다.
# 체스판의 정보는 정수로 이루어져 있고, 각 정수는 칸의 색을 의미한다. 0은 흰색, 1은 빨간색, 2는 파란색이다.
#
# 다음 K개의 줄에 말의 정보가 1번 말부터 순서대로 주어진다. 말의 정보는 세 개의 정수로 이루어져 있고, 순서대로 행, 열의 번호, 이동 방향이다.
# 행과 열의 번호는 1부터 시작하고, 이동 방향은 4보다 작거나 같은 자연수이고 1부터 순서대로 →, ←, ↑, ↓의 의미를 갖는다.
#
# 같은 칸에 말이 두 개 이상 있는 경우는 입력으로 주어지지 않는다.
#
# 출력
# 게임이 종료되는 턴의 번호를 출력한다. 그 값이 1,000보다 크거나 절대로 게임이 종료되지 않는 경우에는 -1을 출력한다.
#
# 제한
# 4 ≤ N ≤ 12
# 4 ≤ K ≤ 10




import sys
sys.stdin = open('input.txt')


def issafe(y,x):
    return 0<=y<size and 0<=x<size


def target(n,y,x,dt):
    global horse_map, horse
    #WHO?
    horse_idx = horse_map[y][x].index(n)
    horse_list = horse_map[y][x][horse_idx:]
    #HOW?
    now_y, now_x = y,x
    next_y, next_x = y+dy[dt], x+dx[dt]
    next_dt = dt
    if not issafe(next_y,next_x) or game_map[next_y][next_x] == 2: #파란칸
        if dt == 0:
            next_dt = 1
        elif dt == 1:
            next_dt = 0
        elif dt == 2:
            next_dt = 3
        elif dt == 3:
            next_dt = 2
        horse[n][2] = next_dt
        # next_y, next_x = y+dy[next_dt], x+dx[next_dt]
        next_y, next_x = y+dy[next_dt], x+dx[next_dt]
        if issafe(next_y, next_x) and game_map[next_y][next_x] == 1: #빨간칸
            horse_list = horse_list[::-1]
    elif game_map[next_y][next_x] == 1: #빨간칸
        horse_list = horse_list[::-1]
    elif game_map[next_y][next_x] == 0: #흰칸
        pass
    return horse_list, now_y, now_x, next_dt


def move(l,y,x,dt):
    global horse_map, horse
    next_y, next_x = y+dy[dt], x+dx[dt]
    if issafe(next_y, next_x) and game_map[next_y][next_x] != 2:
        for horse_target in l:
            horse_map[horse[horse_target][0]][horse[horse_target][1]].remove(horse_target)
            horse_map[next_y][next_x] += [horse_target]
            horse[horse_target][0], horse[horse_target][1] = next_y,next_x
    else:
        next_y, next_x = y, x
    return next_y,next_x


def check(y,x):
    global stack
    if stack < len(horse_map[y][x]):
        stack = len(horse_map[y][x])


#데이터 준비
size, num = map(int,input().split())
game_map = list([0]*size for _ in range(size))
for row in range(size):
    game_map[row] = list(map(int,input().split()))
horse = []
horse_map = list(list([] for _ in range(size)) for __ in range(size))
for n in range(num):
    horse_y, horse_x, horse_dt = map(int,input().split())
    horse.append([horse_y-1, horse_x-1, horse_dt-1])
    horse_map[horse_y-1][horse_x-1] += [n]
# print('game_map : {}'.format(game_map))
# print('horse_map : {}'.format(horse_map))
# print('horse : {}'.format(horse))

#조건
dy = [0,0,-1,1]
dx = [1,-1,0,0]

#결과
stack = 0
turn = 0
result = -1

while stack < 4 and turn < 1000:
    for horse_num in range(num):
        horse_y, horse_x, horse_dt = horse[horse_num][0], horse[horse_num][1], horse[horse_num][2]
        horse_list, now_y, now_x, next_dt = target(horse_num, horse_y, horse_x, horse_dt)
        horse_y, horse_x = move(horse_list, now_y, now_x, next_dt)
        check(horse_y,horse_x)
    turn += 1

if turn >= 1000:
    print(result)
else:
    print(turn)


