# 문제
#
#
# N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며,
# r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다.
# 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.
#
# 오늘부터 인구 이동이 시작되는 날이다.
#
# 인구 이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.
# •국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루동안 연다.
# •위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# •국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# •연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# •연합을 해체하고, 모든 국경선을 닫는다.
#
# 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성하시오.
#
#
#
#
# 입력
#
#
# 첫째 줄에 N, L, R이 주어진다. (1 ≤ N ≤ 50, 1 ≤ L ≤ R ≤ 100)
#
# 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다.
# r행 c열에 주어지는 정수는 A[r][c]의 값이다. (1 ≤ A[r][c] ≤ 100)
#
# 인구 이동이 발생하는 횟수가 2,000번 보다 작거나 같은 입력만 주어진다.
#
#
# 출력
#
# 인구 이동이 몇 번 발생하는지 첫째 줄에 출력한다.


import sys
sys.stdin = open('input.txt')
import collections
q = collections.deque()


def issafe(y,x):
    return 0<=y<size and 0<=x<size

def move(y,x):
    for delta in range(4):
        new_y = y+dy[delta]
        new_x = x+dx[delta]
        if issafe(new_y,new_x) and not visited[new_y][new_x] and so <= abs(datas[new_y][new_x]-datas[y][x]) <= dae:
            q.append((new_y,new_x))
            visited[new_y][new_x] = 1
    return


size,so,dae = map(int,input().split())
datas = list([0]*size)
for row in range(size):
    datas[row] = list(map(int,input().split()))
# print(datas)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
ans = 0
change = True
while ans<=2000 and change:
    visited = [[0]*size for _ in range(size)]
    change = False
    for y in range(size):
        for x in range(size):
            if not visited[y][x]:
                q.append((y,x))
                visited[y][x]=1
                target = []
                result = 0
                cnt = 0
                while q:
                    # print(q)
                    yy,xx = q.popleft()
                    result += datas[yy][xx]
                    cnt += 1
                    target.append((yy,xx))
                    move(yy,xx)
                for ty,tx in target:
                    datas[ty][tx] = result//cnt
                if cnt > 1:
                    change = True
    if change:
        ans += 1
        # print(ans)
    # print(ans)
# print(result)
# print(cnt)
# print(datas)
print(ans)
