# 교도소로 이송 중이던 흉악범이 탈출하는 사건이 발생하여 수색에 나섰다.
# 탈주범은 탈출한 지 한 시간 뒤, 맨홀 뚜껑을 통해 지하터널의 어느 한 지점으로 들어갔으며,
# 지하 터널 어딘가에서 은신 중인 것으로 추정된다.
# 터널끼리 연결이 되어 있는 경우 이동이 가능하므로 탈주범이 있을 수 있는 위치의 개수를 계산하여야 한다.
# 탈주범은 시간당 1의 거리를 움직일 수 있다.
# 지하 터널은 총 7 종류의 터널 구조물로 구성되어 있으며 각 구조물 별 설명은 [표 1]과 같다.
# [표 1]
# [그림 1-1] 은 지하 터널 지도의 한 예를 나타낸다.
# 이 경우 지도의 세로 크기는 5, 가로 크기는 6 이다.
# 맨홀 뚜껑의 위치가 ( 2, 1 ) 으로 주어질 경우, 이는 세로 위치 2, 가로 위치 1을 의미하며 [그림 1-2] 에서 붉은 색으로 표기된 구역이다.
# 탈주범이 탈출 한 시간 뒤 도달할 수 있는 지점은 한 곳이다.
# 탈주범이 2시간 후 도달할 수 있는 지점은, [그림 1-3] 과 같이 맨홀 뚜껑이 위치한 붉은 색으로 표시된 지하도 와 파란색으로 표기된 지하도까지 총 3개의 장소에 있을 수 있다.
# 3시간 후에는 [그림 1-4] 과 같이 총 5개의 지점에 있을 수 있다.
 
# [그림 2-1] 에서 맨홀뚜껑이 위치한 지점이 ( 2, 2 ) 이고 경과한 시간이 6 으로 주어질 경우,
# [그림 2-2] 에서 맨홀뚜껑이 위치한 지점은 붉은 색, 탈주범이 있을 수 있는 장소가 푸른색으로 표기되어 있다.
# 탈주범이 있을 수 있는 장소는, 맨홀뚜껑이 위치한 지점을 포함하여 총 15 개 이다.
#  지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소의 개수를 계산하는 프로그램을 작성하라.
# [제약 사항]
# 1. 시간 제한 : 최대 50개 테이트 케이스를 모두 통과하는데, C/C++/Java 모두 1초
# 2. 지하 터널 지도의 세로 크기 N, 가로 크기 M은 각각 5 이상 50 이하이다. (5 ≤ N, M ≤ 50)
# 3. 맨홀 뚜껑의 세로 위치 R 은 0 이상 N-1이하이고 가로 위치 C 는 0 이상 M-1이하이다. (0 ≤ R ≤ N-1, 0 ≤ C ≤ M-1)
# 4. 탈출 후 소요된 시간 L은 1 이상 20 이하이다. (1 ≤ L ≤ 20)
# 5. 지하 터널 지도에는 반드시 1개 이상의 터널이 있음이 보장된다.
# 6. 맨홀 뚜껑은 항상 터널이 있는 위치에 존재한다.
# [입력]
# 첫 줄에 총 테스트 케이스의 개수 T가 주어진다.
# 두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.
# 각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
# 그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.
# 숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0 은 터널이 없는 장소를 의미한다.
# [출력]
# 테스트 케이스의 개수만큼 T줄에 T개의 테스트 케이스 각각에 대한 답을 출력한다.
# 각 줄은 “#x”로 시작하고 공백을 하나 둔 다음 정답을 기록한다. (x는 1부터 시작하는 테스트 케이스의 번호이다)
# 출력해야 할 정답은 탈주범이 위치할 수 있는 장소의 개수이다.


import sys
sys.stdin = open('input.txt')


def issafe(row,col):
    return 0<=row<sero and 0<=col<garo

def up(row,col):
    if issafe(row-1,col) and not visited[row-1][col] and mymap[row-1][col] in u:
        q.append((row-1,col))
        visited[row-1][col] = 1
        time[row-1][col] = time[row][col]+1

def right(row,col):
    if issafe(row,col+1) and not visited[row][col+1] and mymap[row][col+1] in r:
        q.append((row,col+1))
        visited[row][col+1] = 1
        time[row][col+1] = time[row][col]+1

def down(row,col):
    if issafe(row+1,col) and not visited[row+1][col] and mymap[row+1][col] in d:
        q.append((row+1,col))
        visited[row+1][col] = 1
        time[row+1][col] = time[row][col]+1

def left(row,col):
    if issafe(row,col-1) and not visited[row][col-1] and mymap[row][col-1] in l:
        q.append((row,col-1))
        visited[row][col-1] = 1
        time[row][col-1] = time[row][col]+1


for tc in range(int(input())):
    sero,garo,row,col,t = map(int,input().split())
    mymap = [[0]*garo for _ in range(sero)]
    for r in range(sero):
        mymap[r] = list(map(int,input().split()))

    u = [1,2,5,6]
    r = [1,3,6,7]
    d = [1,2,4,7]
    l = [1,3,4,5]
    visited = [[0]*garo for _ in range(sero)]
    visited[row][col] = 1
    time = [[1]*garo for _ in range(sero)]

    q = []
    q.append((row,col))
    cnt = 0
    y = row
    x = col
    while q != []:
        # for i in time:
        #     print(i)
        # print('-'*20)
        # print(cnt)
        y,x = q.pop(0)
        if time[y][x] == t+1:
            break
        cnt += 1
        now = mymap[y][x]
        if now == 1:
            up(y,x)
            right(y, x)
            down(y, x)
            left(y, x)
        elif now == 2:
            up(y, x)
            down(y, x)
        elif now == 3:
            right(y, x)
            left(y, x)
        elif now == 4:
            up(y, x)
            right(y, x)
        elif now == 5:
            right(y, x)
            down(y, x)
        elif now == 6:
            down(y, x)
            left(y, x)
        elif now == 7:
            up(y, x)
            left(y, x)
    print('#{} {}'.format(tc+1,cnt))









# def issafe(row,col):
#     return 0<=row<sero and 0<=col<garo
#
# def up(row,col,t):
#     global cnt
#     # row -= 1
#     if issafe(row-1,col) and not visited[row-1][col] and mymap[row-1][col] in u:
#         cnt += 1
#         # visited[row - 1][col] = 1
#         find(row-1,col,t-1)
#
# def right(row,col,t):
#     global cnt
#     # col += 1
#     if issafe(row,col+1) and not visited[row][col+1] and mymap[row][col+1] in r:
#         cnt += 1
#         # visited[row][col + 1] = 1
#         find(row, col+1,t-1)
#
# def down(row,col,t):
#     global cnt
#     # row += 1
#     if issafe(row+1,col) and not visited[row+1][col] and mymap[row+1][col] in d:
#         cnt += 1
#         # visited[row + 1][col] = 1
#         find(row+1, col,t-1)
#
# def left(row,col,t):
#     global cnt
#     # col -= 1
#     if issafe(row,col-1) and not visited[row][col-1] and mymap[row][col-1] in l:
#         cnt += 1
#         # visited[row][col - 1] = 1
#         find(row, col-1,t-1)
#
# def find(row,col,t):
#     global cnt, ans
#     if t == 0:
#         ans = cnt
#         return
#     # t -= 1
#     visited[row][col] = 1
#     now = mymap[row][col]
#     if now == 1:
#         up(row, col,t)
#         right(row, col,t)
#         down(row, col,t)
#         left(row, col,t)
#     elif now == 2:
#         up(row, col,t)
#         down(row, col,t)
#     elif now == 3:
#         right(row, col,t)
#         left(row, col,t)
#     elif now == 4:
#         up(row, col,t)
#         right(row, col,t)
#     elif now == 5:
#         right(row, col,t)
#         down(row, col,t)
#     elif now == 6:
#         down(row, col,t)
#         left(row, col,t)
#     elif now == 7:
#         up(row, col,t)
#         left(row, col,t)
#
#
# for tc in range(int(input())):
#     sero,garo,row,col,t = map(int,input().split())
#     mymap = [[0]*garo for _ in range(sero)]
#     for r in range(sero):
#         mymap[r] = list(map(int,input().split()))
#
#     u = [1,2,5,6]
#     r = [1,3,6,7]
#     d = [1,2,4,7]
#     l = [1,3,4,5]
#     visited = [[0]*garo for _ in range(sero)]
#
#     cnt = 1
#     ans = 0
#     find(row,col,t-1)
#     print(ans)

