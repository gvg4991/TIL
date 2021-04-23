# 청소년 상어는 더욱 자라 어른 상어가 되었다. 상어가 사는 공간에 더 이상 물고기는 오지 않고 다른 상어들만이 남아있다.
# 상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다.
# 상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데,
# 1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.
#
# N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다.
# 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
# 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
# 자신의 냄새를 그 칸에 뿌린다. 냄새는 상어가 k번 이동하고 나면 사라진다.
#
# 각 상어가 이동 방향을 결정할 때는, 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
# 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
# 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
# 우선순위는 상어마다 다를 수 있고, 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
# 상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고, 그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.
#
# 모든 상어가 이동한 후 한 칸에 여러 마리의 상어가 남아 있으면,
# 가장 작은 번호를 가진 상어를 제외하고 모두 격자 밖으로 쫓겨난다.
#
#
#
# <그림 1>
#
# 우선 순위
# 상어 1	상어 2	상어 3	상어 4
# ↑	↓ ← ↑ →	↑	↓ → ← ↑	↑	→ ← ↓ ↑	↑	← → ↑ ↓
# ↓	→ ↑ ↓ ←	↓	↓ ↑ ← →	↓	↑ → ← ↓	↓	← ↓ → ↑
# ←	← → ↓ ↑	←	← → ↑ ↓	←	↑ ← ↓ →	←	↑ → ↓ ←
# →	→ ← ↑ ↓	→	→ ↑ ↓ ←	→	← ↓ ↑ →	→	↑ → ↓ ←
# <표 1>
#
# <그림 1>은 맨 처음에 모든 상어가 자신의 냄새를 뿌린 상태를 나타내며,
# <표 1>에는 각 상어 및 현재 방향에 따른 우선순위가 표시되어 있다.
# 이 예제에서는 k = 4이다. 왼쪽 하단에 적힌 정수는 냄새를 의미하고, 그 값은 사라지기까지 남은 시간이다.
# 좌측 상단에 적힌 정수는 상어의 번호 또는 냄새를 뿌린 상어의 번호를 의미한다.
#
#
#
# <그림 2>
#
#
#
# <그림 3>
#
# <그림 2>는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태이고, <그림 3>은 <그림 2>의 상태에서 한 칸 더 이동한 것이다.
# (2, 4)에는 상어 2과 4가 같이 도달했기 때문에, 상어 4는 격자 밖으로 쫓겨났다.
#
#
#
# <그림 4>
#
#
#
# <그림 5>
#
# <그림 4>은 격자에 남아있는 모든 상어가 한 칸 이동하고 자신의 냄새를 뿌린 상태,
# <그림 5>는 <그림 4>에서 한 칸 더 이동한 상태를 나타낸다.
# 상어 2는 인접한 칸 중에 아무 냄새도 없는 칸이 없으므로 자신의 냄새가 들어있는 (2, 4)으로 이동했다.
# 상어가 이동한 후에, 맨 처음에 각 상어가 뿌린 냄새는 사라졌다.
#
# 이 과정을 반복할 때, 1번 상어만 격자에 남게 되기까지 몇 초가 걸리는지를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫 줄에는 N, M, k가 주어진다. (2 ≤ N ≤ 20, 2 ≤ M ≤ N2, 1 ≤ k ≤ 1,000)
#
# 그 다음 줄부터 N개의 줄에 걸쳐 격자의 모습이 주어진다. 0은 빈칸이고, 0이 아닌 수 x는 x번 상어가 들어있는 칸을 의미한다.
#
# 그 다음 줄에는 각 상어의 방향이 차례대로 주어진다. 1, 2, 3, 4는 각각 위, 아래, 왼쪽, 오른쪽을 의미한다.
#
# 그 다음 줄부터 각 상어의 방향 우선순위가 상어 당 4줄씩 차례대로 주어진다. 각 줄은 4개의 수로 이루어져 있다.
# 하나의 상어를 나타내는 네 줄 중 첫 번째 줄은 해당 상어가 위를 향할 때의 방향 우선순위,
# 두 번째 줄은 아래를 향할 때의 우선순위,
# 세 번째 줄은 왼쪽을 향할 때의 우선순위,
# 네 번째 줄은 오른쪽을 향할 때의 우선순위이다.
# 각 우선순위에는 1부터 4까지의 자연수가 한 번씩 나타난다.
# 가장 먼저 나오는 방향이 최우선이다. 예를 들어, 우선순위가 1 3 2 4라면, 방향의 순서는 위, 왼쪽, 아래, 오른쪽이다.
#
# 맨 처음에는 각 상어마다 인접한 빈 칸이 존재한다. 따라서 처음부터 이동을 못 하는 경우는 없다.
#
# 출력
# 1번 상어만 격자에 남게 되기까지 걸리는 시간을 출력한다. 단, 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력한다.


import sys
sys.stdin = open('input.txt')


def issafe(y,x):
    return 0<=y<size and 0<=x<size


def ready():
    for row in range(size):
        for col in range(size):
            if shark_map[row][col]:
                shark_num = shark_map[row][col] - 1
                shark_smell[shark_num][0] = [row,col]


def search():
    global next_y,next_x,next_dt
    for shark_num in living_shark:
        if shark_num:
            shark_idx = shark_num-1
            now_y,now_x = shark_smell[shark_idx][0]
            now_dt = shark_dt[shark_idx]-1
            next_dt_list = shark_next_dt[shark_idx][now_dt]
            next_dt_flag = 0
            for dt in next_dt_list:
                target_dt = dt-1
                target_y = now_y + dy[target_dt]
                target_x = now_x + dx[target_dt]
                if issafe(target_y,target_x):
                    if not shark_map[target_y][target_x]: # 우선순위 방향에 흔적이 없으면
                        next_y,next_x,next_dt = target_y,target_x,target_dt
                        next_dt_flag = 1
                        break
                    if not next_dt_flag and shark_map[target_y][target_x] == shark_idx: # 우선순위 방향에 흔적이 자신이면
                        next_y,next_x,next_dt = target_y,target_x,target_dt
                        next_dt_flag = 2
            shark_move[shark_idx] = [next_y,next_x,next_dt]


def move():
    global shark_dt, result
    result += 1
    for shark_idx in range(mari):
        # shark_map에서 냄새가 없어지는 좌표에 있는 상어 == 냄새가 없어지는 상어라면 제거
        if shark_smell[shark_idx][smell-1]:
            remove_y,remove_x = shark_smell[shark_idx][smell-1]
            if shark_map[remove_y][remove_x] == shark_idx+1: #shark_map의 상어번호는 1부터라서 1더해줌
                shark_map[remove_y][remove_x] = 0
        # shark_smell에서 냄새를 한컬럼씩 이동
        for smell_num in range(smell-1,0,-1):
            shark_smell[shark_idx][smell_num] = shark_smell[shark_idx][smell_num-1]

        # 새로 이동한 상어 입력 및 상어냄새 생성
    for shark_num in living_shark:
        if shark_num:
            shark_idx = shark_num-1
            new_shark_y, new_shark_x, new_shark_dt = shark_move[shark_idx][0], shark_move[shark_idx][1], shark_move[shark_idx][2]
            if not shark_map[new_shark_y][new_shark_x] or shark_map[new_shark_y][new_shark_x] == shark_idx+1:
                shark_map[new_shark_y][new_shark_x] = shark_idx+1
                shark_smell[shark_idx][0] = [new_shark_y,new_shark_x]
                shark_dt[shark_idx] = new_shark_dt+1
            else:
                living_shark[shark_idx] = 0
                shark_smell[shark_idx][0] = 0
                shark_dt[shark_idx] = 0



size,mari,smell = map(int,input().split())
shark_map = [list(map(int,input().split())) for shark in range(size)] # 상어 위치 지도
shark_dt = list(map(int,input().split())) # 상어 현재 방향
shark_next_dt = [[list(map(int,input().split())) for dt in range(4)] for shark in range(mari)] # 방향 1,2,3,4 = 위,아래,왼쪽,오른쪽
dy = [-1,1,0,0]
dx = [0,0,-1,1]
living_shark = [shark+1 for shark in range(mari)] # 살이있는 상어
shark_smell = [[0]*smell for shark in range(mari)] # 상어 별 냄새 좌표
shark_move = [[0,0,0] for shark in range(mari)] # 상어 별 움직이는 좌표 및 방향
flag = 1
result = 0
ans = -1


ready()
while flag:
    if sum(living_shark) == 1 and result > 1000:
        flag = 0
    search()
    move()

if result <= 1000:
    ans = result
print(ans)
