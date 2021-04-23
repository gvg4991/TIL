# 민기는 핀볼 게임을 개발 중에 있다.
# 핀볼게임은 N x N 크기의 핀볼 게임판에 정사각형 블록과 4가지 형태의 삼각형 블록들이 섞여 있고,
# 여기에 추가적으로 웜홀과 블랙홀이 존재한다. 핀볼게임의 게임판의 하나의 예는 아래 [그림1]과 같다.
#
#
#                                                        [그림1]
#
# 각 블록들은 일정한 번호로 주어지는데, 블록들의 번호와 모양은 아래 [그림2]와 같다.
#
#
#
#                                                        [그림2]
#
#
# 웜홀과 블랙홀은 각각 아래 [그림3]의 번호로 주어진다.
#
#
#                         [그림3]
#
#
#
# 게임판 위에서는 작은 핀볼 하나가 상, 하, 좌, 우 중 한 방향으로 움직인다.
#
#
#
#
#
# 핀볼은 블록이나 웜홀 또는 블랙홀을 만나지 않는 한 현재 방향을 유지하면서 계속 직진하며,
#
# 블록의 수평면이나 수직면을 만날 경우 방향을 바꿔 반대 방향으로 돌아오고, 경사면을 만날 경우에는 직각으로 진행 방향이 꺾이게 된다.
#
#
#
#
#
# 또한 핀볼은 벽을 만날 경우에도 반대 방향으로 돌아온다.
# 아래의 그림과 같이 핀볼이 왼쪽으로 움직이다 벽을 만나면 반대 방향으로 다시 돌아오게 된다.
#
#
#
#
#
# 핀볼이 웜홀에 빠지면 동일한 숫자를 가진 다른 반대편 웜홀로 빠져 나오게 되며 진행방향은 그대로 유지된다.
# (웜홀은 반드시 쌍으로 주어지며, 입력에서는 6 이상 10 이하의 숫자로 표시된다.)
#
#
#
#
#
# 핀볼이 블랙홀을 만나면, 핀볼이 사라지게 되어 게임은 끝나게 된다.
#
#
#
#
#
# 게임은 핀볼이 출발 위치로 돌아오거나, 블랙홀에 빠질 때 끝나게 되며, 점수는 벽이나 블록에 부딪힌 횟수가 된다. (웜홀을 통과하는 것은 점수에 포함되지 않는다.)
#
# 블랙홀에 빠져서 게임이 끝나더라도, 벽이나 블록에 부딪혀 획득한 점수는 남아있게 된다.
#
# 게임판 위에서 출발 위치와 진행 방향을 임의로 선정가능 할 때,
#
# ▶ 게임에서 얻을 수 있는 점수의 최댓값을 구하여라!
#
# 단, 블록, 웜홀 또는 블랙홀이 있는 위치에서는 출발할 수 없다.
#
#
#
# [제약 사항]
#
# 게임판의 크기는 정사각형으로 주어지며, 한 변의 길이 N 은 5 이상 100 이하이다. (5 ≤ N ≤ 100)
# 웜홀은 게임판 내에서 숫자 6 ~ 10으로 주어진다.
# 블랙홀은 게임판 내에서 숫자 -1 로 주어진다.
# 게임판에서 웜홀 또는 블랙홀이 존재하지 않는 경우도 있다.
# 웜홀이 있는 경우 반드시 쌍(pair)으로 존재하며, 웜홀이 주어지는 경우 최대 5쌍 존재한다.
# 웜홀을 통과한 핀볼은 동일한 숫자를 가진 반대편 웜홀로 이동하게 되며, 이때 진행방향은 그대로 유지된다.
# 블랙홀은 최대 5개가 주어진다.
#
#
# [입력]
#
# 입력의 가장 첫 줄에는 총 테스트 케이스의 개수 T가 주어지며, 그 다음 줄부터 각 테스트 케이스가 주어진다.
#
# 각 테스트 케이스의 첫째 줄에는 N이 주어지고, 다음 N줄에 걸쳐서 핀볼 게임판의 모양이 주어진다.
#
# 게임판의 모양은 -1 이상 10 이하의 정수로 주어지며, 각 숫자는 한 칸씩 띄어져서 주어진다.
# 숫자에 따른 의미는 다음과 같다
#
#
#
# -1
#
# 0
#
# 1 ~ 5
#
# 6 ~ 10
#
# 블랙홀
#
# 빈공간
#
# 블록
#
# 웜홀
#
#
#
# [출력]
#
# 테스트 케이스 t에 대한 결과는 "#t"를 찍고, 한 칸 띄고 정답을 출력한다.
#
# (단, t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)



import sys
sys.stdin = open('input.txt')


def issafe(y,x):
    return 0<=y<case and 0<=x<case


def move(y,x,d):
    global count, ans
    next_y, next_x = y+dy[d], x+dx[d]

    while issafe(next_y,next_x) and datas[next_y][next_x] == 0 and [next_y,next_x] != [start_y,start_x]:
            next_y, next_x = next_y+dy[d], next_x+dx[d]

    if game or (count > 1 and [next_y,next_x] == [start_y,start_x]) or (issafe(next_y,next_x) and datas[next_y][next_x] == -1):
        if ans < result and result != 0:
            ans = result
        return

    if d == 0:
        next_y, next_x, next_d = up(next_y,next_x,d)
    elif d == 1:
        next_y, next_x, next_d = right(next_y,next_x,d)
    elif d == 2:
        next_y, next_x, next_d = down(next_y,next_x,d)
    elif d == 3:
        next_y, next_x, next_d = left(next_y,next_x,d)
    count += 1
    move(next_y, next_x, next_d)


def left(y,x,d):
    global result, game
    if not issafe(y,x) or datas[y][x] in [3,4,5]:
        result *= 2
        result += 1
        game = 1
        d = 1
    elif datas[y][x] == 1:
        result += 1
        d = 0
    elif datas[y][x] == 2:
        result += 1
        d = 2
    elif datas[y][x] in [6,7,8,9,10]:
        y,x = warmhole(y,x)
    return y,x,d #바뀐 위치,방향


def right(y,x,d):
    global result, game
    if not issafe(y,x) or datas[y][x] in [1,2,5]:
        result *= 2
        result += 1
        game = 1
        d = 3
    elif datas[y][x] == 3:
        result += 1
        d = 2
    elif datas[y][x] == 4:
        result += 1
        d = 0
    elif datas[y][x] in [6,7,8,9,10]:
        y,x = warmhole(y,x)
    return y,x,d #바뀐 위치,방향


def up(y,x,d):
    global result, game
    if not issafe(y,x) or datas[y][x] in [1,4,5]:
        result *= 2
        result += 1
        game = 1
        d = 2
    elif datas[y][x] == 2:
        result += 1
        d = 1
    elif datas[y][x] == 3:
        result += 1
        d = 3
    elif datas[y][x] in [6,7,8,9,10]:
        y,x = warmhole(y,x)
    return y,x,d #바뀐 위치,방향


def down(y,x,d):
    global result, game
    if not issafe(y,x) or datas[y][x] in [2,3,5]:
        result *= 2
        result += 1
        game = 1
        d = 0
    elif datas[y][x] == 1:
        result += 1
        d = 1
    elif datas[y][x] == 4:
        result += 1
        d = 3
    elif datas[y][x] in [6,7,8,9,10]:
        y,x = warmhole(y,x)
    return y,x,d #바뀐 위치,방향


def warmhole(y,x):
    if datas[y][x] == 6:
        if [y,x] == warm[6][0]:
            y,x = warm[6][1][0],warm[6][1][1]
        elif [y,x] == warm[6][1]:
            y,x = warm[6][0][0],warm[6][0][1]
    elif datas[y][x] == 7:
        if [y,x] == warm[7][0]:
            y,x = warm[7][1][0],warm[7][1][1]
        elif [y,x] == warm[7][1]:
            y,x = warm[7][0][0],warm[7][0][1]
    elif datas[y][x] == 8:
        if [y,x] == warm[8][0]:
            y,x = warm[8][1][0],warm[8][1][1]
        elif [y,x] == warm[8][1]:
            y,x = warm[8][0][0],warm[8][0][1]
    elif datas[y][x] == 9:
        if [y,x] == warm[9][0]:
            y,x = warm[9][1][0],warm[9][1][1]
        elif [y,x] == warm[9][1]:
            y,x = warm[9][0][0],warm[9][0][1]
    elif datas[y][x] == 10:
        if [y,x] == warm[10][0]:
            y,x = warm[10][1][0],warm[10][1][1]
        elif [y,x] == warm[10][1]:
            y,x = warm[10][0][0],warm[10][0][1]
    return y,x #다음 위치


test = int(input())
for tc in range(1,test+1):
    case = int(input())
    datas = list([0] for _ in range(case))
    warm = [0,0,0,0,0,0,[],[],[],[],[]]
    for row in range(case):
        datas[row] = list(map(int,input().split()))
        for cal in range(case):
            if datas[row][cal] == 6:
                warm[6].append([row,cal])
            elif datas[row][cal] == 7:
                warm[7].append([row,cal])
            elif datas[row][cal] == 8:
                warm[8].append([row,cal])
            elif datas[row][cal] == 9:
                warm[9].append([row,cal])
            elif datas[row][cal] == 10:
                warm[10].append([row,cal])

    dy = [-1,0,1,0] #up, right, down, left
    dx = [0,1,0,-1]
    ans = 0
    for row in range(case):
        for cal in range(case):
            if datas[row][cal] == 0:
                start_y,start_x = row,cal
                for dt in range(4):
                    game = 0
                    result = 0
                    count = 0
                    move(row,cal,dt)

    print('#{} {}'.format(tc,ans))
