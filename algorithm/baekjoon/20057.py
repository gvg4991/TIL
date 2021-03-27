# 문제
# 마법사 상어가 토네이도를 배웠고, 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다.
# 위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.
#
# 토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다.
# 다음은 N = 7인 경우 토네이도의 이동이다.
#
#
#
# 토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
#
#
#
# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다.
# 비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다.
# α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다. 모래가 이미 있는 칸으로 모래가 이동하면,모래의 양은 더해진다.
# 위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.
#
# 토네이도는 (1, 1)까지 이동한 뒤 소멸한다.
# 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.
#
# 입력
# 첫째 줄에 격자의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다.
# r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.
#
# 출력
# 격자의 밖으로 나간 모래의 양을 출력한다.
#
# 제한
# 3 ≤ N ≤ 499
# N은 홀수
# 0 ≤ A[r][c] ≤ 1,000
# 가운데 칸에 있는 모래의 양은 0




import sys
sys.stdin = open('input.txt')

def issafe(y,x):
    return 0<=y<case and 0<=x<case

def plus(y,x,dn):
    global datas, result
    target = 0
    if dn == 0:
        for p in left:
            plus_y, plus_x, plus_v = p[0], p[1], p[2]
            if issafe(y+plus_y,x+plus_x):
                datas[y+plus_y][x+plus_x] += int(datas[y][x]*plus_v)
            else:
                result += int(datas[y][x]*plus_v)
            target += int(datas[y][x]*plus_v)
        if issafe(y,x-1):
            datas[y][x-1] += (datas[y][x]-target)
        else:
            result += (datas[y][x]-target)
    elif dn == 1:
        for p in down:
            plus_y, plus_x, plus_v = p[0], p[1], p[2]
            if issafe(y+plus_y,x+plus_x):
                datas[y+plus_y][x+plus_x] += int(datas[y][x]*plus_v)
            else:
                result += int(datas[y][x]*plus_v)
            target += int(datas[y][x]*plus_v)
        if issafe(y+1,x):
            datas[y+1][x] += (datas[y][x]-target)
        else:
            result += (datas[y][x]-target)
    elif dn == 2:
        for p in right:
            plus_y, plus_x, plus_v = p[0], p[1], p[2]
            if issafe(y+plus_y,x+plus_x):
                datas[y+plus_y][x+plus_x] += int(datas[y][x]*plus_v)
            else:
                result += int(datas[y][x]*plus_v)
            target += int(datas[y][x]*plus_v)
        if issafe(y,x+1):
            datas[y][x+1] += (datas[y][x]-target)
        else:
            result += (datas[y][x]-target)
    elif dn == 3:
        for p in up:
            plus_y, plus_x, plus_v = p[0], p[1], p[2]
            if issafe(y+plus_y,x+plus_x):
                datas[y+plus_y][x+plus_x] += int(datas[y][x]*plus_v)
            else:
                result += int(datas[y][x]*plus_v)
            target += int(datas[y][x]*plus_v)
        if issafe(y-1,x):
            datas[y-1][x] += (datas[y][x]-target)
        else:
            result += (datas[y][x]-target)
    datas[y][x] = 0


case = int(input())
datas = [0] * case
for c in range(case):
    datas[c] = list(map(int,input().split()))
# print(datas)

now_y = now_x = next_y = next_x = case//2
dt = [[0,-1],[1,0],[0,1],[-1,0]]
dn = 0

left = [[0,-2,0.05],[-1,-1,0.1],[1,-1,0.1],[-1,0,0.07],[1,0,0.07],[-2,0,0.02],[2,0,0.02],[-1,1,0.01],[1,1,0.01]]
right = [[0,2,0.05],[-1,1,0.1],[1,1,0.1],[-1,0,0.07],[1,0,0.07,],[-2,0,0.02],[2,0,0.02],[-1,-1,0.01],[1,-1,0.01]]
up = [[-2,0,0.05],[-1,-1,0.1],[-1,1,0.1],[0,-1,0.07],[0,1,0.07],[0,-2,0.02],[0,2,0.02],[1,1,0.01],[1,-1,0.01]]
down = [[2,0,0.05],[1,-1,0.1],[1,1,0.1],[0,-1,0.07],[0,1,0.07],[0,-2,0.02],[0,2,0.02],[-1,1,0.01],[-1,-1,0.01]]

result = 0
move = [[0]*case for _ in range(case)]
move[now_y][now_x] = 1

while next_y != 0 or next_x != 0:
    #이동
    next_y, next_x = now_y + dt[dn][0], now_x + dt[dn][1]
    #더하기
    plus(next_y,next_x,dn)
    #위치 남기기
    now_y, now_x = next_y, next_x
    move[now_y][now_x] = 1
    #방향확인
    temp_dn = (dn+1)%4
    if move[now_y + dt[temp_dn][0]][now_x + dt[temp_dn][1]] == 0: #다음 경로가 0이면
        dn = temp_dn

print(result)


