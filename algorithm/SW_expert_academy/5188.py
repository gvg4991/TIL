# 그림처럼 NxN 칸에 숫자가 적힌 판이 주어지고, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되도록 움직였다면 이때의 합계가 얼마인지 출력하는 프로그램을 만드시오.
# 그림의 경우 1, 2, 3, 4, 5순으로 움직이고 최소합계는 15가 된다. 가능한 모든 경로에 대해 합을 계산한 다음 최소값을 찾아도 된다.
# [입력]
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 첫 줄에 가로 세로 칸 수 N이 주어지고, 다음 줄부터 N개씩 N개의 줄에 걸쳐 10이하의 자연수가 주어진다. 3<=N<=13
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



import sys
sys.stdin = open('input.txt')



def issafe(y,x):
    if x<0 or x>n-1 or y<0 or y>n-1:
        return False
    else:
        return True

def min_sum(y,x):
    global result, ans
    result += datas[y][x]
    if y == n-1 and x == n-1:
        if ans > result:
            ans = result
        return
    for delta in range(2):
        new_y = y + dy[delta]
        new_x = x + dx[delta]
        if issafe(new_y,new_x):
            now_y = new_y
            now_x = new_x
            min_sum(now_y,now_x)
            result -= datas[now_y][now_x]


test = int(input())
for tc in range(test):
    n = int(input())
    datas=[]
    for case in range(n):
        datas.append(list(map(int,input().split())))

    dy = [0,1]
    dx = [1,0]
    result = 0
    ans = 99999

    min_sum(0,0)
    print('#{} {}'.format(tc+1,ans))