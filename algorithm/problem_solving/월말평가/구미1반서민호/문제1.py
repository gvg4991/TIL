import sys
sys.stdin = open('input.txt')


def issafe(y,x):
    return 0<=y<n and 0<=x<n

for tc in range(int(input())):
    n = int(input())
    mymap = [[0]*n for _ in range(n)]
    start_x,start_y,end_x,end_y = map(int,input().split())

    dy = [2,3,2,3,-2,-3,-2,-3]
    dx = [3,2,-3,-2,3,2,-3,-2]
    q = [(start_y,start_x)]
    distance = [[987654321]*n for _ in range(n)]
    distance[start_y][start_x] = 0
    cnt = 0
    while q != []:
        target = q.pop(0)
        target_y, target_x = target[0], target[1]
        if target_y == end_y and target_x == end_x:
            ans = distance[target_y][target_x]
        for delta in range(8):
            new_y = target_y + dy[delta]
            new_x = target_x + dx[delta]
            if issafe(new_y,new_x) and distance[new_y][new_x] > distance[target_y][target_x]+1:
                distance[new_y][new_x] = distance[target_y][target_x]+1
                q.append((new_y,new_x))

    print('#{} {}'.format(tc+1,ans))
