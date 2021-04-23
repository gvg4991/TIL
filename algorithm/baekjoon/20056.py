# 어른 상어가 마법사가 되었고, 파이어볼을 배웠다.
#
# 마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다. 가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
# i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.
#
# 격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
#
# 파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.
#
# 7	0	1
# 6	 	2
# 5	4	3
# 마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.
#
# 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
# 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
# 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
# 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
# 파이어볼은 4개의 파이어볼로 나누어진다.
# 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
# 질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
# 속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
# 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
# 질량이 0인 파이어볼은 소멸되어 없어진다.
# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.
#
# 입력
# 첫째 줄에 N, M, K가 주어진다.
#
# 둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다.
# .파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
#
# 서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.
#
# 출력
# 마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.
#
# 제한
# 4 ≤ N ≤ 50
# 0 ≤ M ≤ N2
# 1 ≤ K ≤ 1,000
# 1 ≤ ri, ci ≤ N
# 1 ≤ mi ≤ 1,000
# 1 ≤ si ≤ 1,000
# 0 ≤ di ≤ 7


import sys
sys.stdin = open('input.txt')


# def issafe(y,x):
#     return 0<=y<size and 0<=x<size


def move():
    for tc in range(case):
        if datas[tc]:
            y,x,m,s,d = datas[tc][0],datas[tc][1],datas[tc][2],datas[tc][3],datas[tc][4]
            if datas[tc][0]+s*dy[d] >= size:
                datas[tc][0] = (datas[tc][0]+s*dy[d])%size
            elif datas[tc][0]+s*dy[d] < 0:
                datas[tc][0] = size - (-1*(datas[tc][0]+s*dy[d]))%size
            else:
                datas[tc][0] += s*dy[d]
            if datas[tc][1]+s*dx[d] >= size:
                datas[tc][1] = (datas[tc][1]+s*dx[d])%size
            elif datas[tc][1]+s*dx[d] < 0:
                datas[tc][1] = size - (-1*(datas[tc][1]+s*dx[d]))%size
            else:
                datas[tc][1] += s*dx[d]
            fire[datas[tc][0]][datas[tc][1]] += [tc] #list(idx) map
            mass[datas[tc][0]][datas[tc][1]] += m #sum(mass) map
            speed[datas[tc][0]][datas[tc][1]] += s #sum(speed) map
            if len(fire[datas[tc][0]][datas[tc][1]]) == 2:
                target.append([datas[tc][0],datas[tc][1]]) #2개 이상 있는 좌표

def check():
    global case, datas
    for t in target:
        ty,tx = t[0],t[1]
        # 방향 설정
        # target_dy = [-1,0,1,0]
        # target_dx = [0,1,0,-1]
        d_nmg = []
        d_flag = 0
        for f in fire[ty][tx]: #2개 이상 좌표에 있는 파이어볼 인덱스 불러오기
            if datas[f] and not d_flag:
                if not datas[f][4]%2 in d_nmg:
                    d_nmg += [datas[f][4]%2]
                if len(d_nmg) == 2: #홀,짝 모두 있으면
                    # target_dy = [-1,1,1,-1]
                    # target_dx = [1,1,-1,-1]
                    d_flag = 1
                #같은 칸에 있는 파이어볼 제거
                # case-=1
            datas[f] = 0
        # datas=list(datas.set())
        # datas.remove(0)
        # 질량 설정
        target_m = mass[ty][tx]//5
        # if target_m == 0:
        #     continue
        # 속력 설정
        target_s = speed[ty][tx]//len(fire[ty][tx])
        # # 나눠진 4개의 파이어볼 추가
        # for dt in range(4):
        #     next_y,next_x = ty+target_s*target_dy[dt],tx+target_s*target_dx[dt]
        #     if next_y >= size:
        #         now_y = next_y%size
        #     elif next_y < 0:
        #         now_y = size - ((-1*next_y)%size)
        #     else:
        #         now_y = next_y
        #     if next_x >= size:
        #         now_x = next_x%size
        #     elif next_x < 0:
        #         now_x = size - ((-1*next_x)%size)
        #     else:
        #         now_x = next_x
        #     datas.append([now_y, now_x, target_m, target_s, 2*dt+d_flag])
        #     case+=1
        for dt in range(4):
            datas.append([ty, tx, target_m, target_s, 2*dt+d_flag])
            case+=1



size,case,test = map(int,input().split())
datas = list([0] for _ in range(case))
for tc in range(case):
    y,x,m,speed,dt = map(int,input().split())
    datas[tc] = [y-1,x-1,m,speed,dt] #[y,x,m,speed,dt]

dy = [-1,-1,0,1,1,1,0,-1]
dx = [0,1,1,1,0,-1,-1,-1]
# fire = list([[] for __ in range(size)] for _ in range(size))
# mass = list([0]*size for _ in range(size))
# speed = list([0]*size for _ in range(size))
# target = []


while test:
    fire = list([[] for __ in range(size)] for _ in range(size))
    mass = list([0]*size for _ in range(size))
    speed = list([0]*size for _ in range(size))
    target = []
    move()
    if target:
        check()
    test -= 1

ans = 0
for d in datas:
    if d:
        ans += d[2]
print(ans)

