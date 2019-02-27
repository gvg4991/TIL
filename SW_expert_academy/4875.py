# NxN 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램을 작성하시오. 도착할 수 있으면 1, 아니면 0을 출력한다.
# 주어진 미로 밖으로는 나갈 수 없다.
# 다음은 5x5 미로의 예이다.
# 13101
# 10101
# 10101
# 10101
# 10021
# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 도착할 수 있는지 확인하면 된다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 0은 통로, 1은 벽, 2는 출발, 3은 도착이다. 5<=N<=100
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.


def issafe(y,x):
    if x < 0 or x > case-1 or y < 0 or y > case-1:
        return False
    else:
        return True

def miro(y,x):
    global result
    visited.append((y,x))
    
    if datas[y][x] == 3:
        result = 1
        return

    else:
        for delta in range(4):
            new_y = y+dy[delta]
            new_x = x+dx[delta]

            if issafe(new_y,new_x) and not (new_y,new_x) in visited and datas[new_y][new_x] != 1:
                now_y = new_y
                now_x = new_x

                miro(now_y,now_x)
                
    

test = int(input())
for tc in range(test):
    case = int(input())
    datas = []
    for row in range(case):
        datas += [list(map(int,input()))]

    start_y = start_x = None
    # end_y = end_x = None
    for row in range(case):
        for col in range(case):
            if datas[row][col] == 2:
                start_y = row
                start_x = col
                break

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    result = 0
    visited = []

    miro(start_y,start_x)

    if result == 1:
        print(f'#{tc+1} {1}')
    else:    
        print(f'#{tc+1} {0}')
    