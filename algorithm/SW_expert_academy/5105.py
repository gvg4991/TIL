# NxN 크기의 미로에서 출발지 목적지가 주어진다.
# 이때 최소 몇 개의 칸을 지나면 출발지에서 도착지에 다다를 수 있는지 알아내는 프로그램을 작성하시오.
# 경로가 있는 경우 출발에서 도착까지 가는데 지나야 하는 최소한의 칸 수를, 경로가 없는 경우 0을 출력한다.
# 다음은 5x5 미로의 예이다. 1은 벽, 0은 통로를 나타내며 미로 밖으로 벗어나서는 안된다.
# 13101
#  10101
#  10101
#  10101
#  10021
# 마지막 줄의 2에서 출발해서 0인 통로를 따라 이동하면 맨 윗줄의 3에 5개의 칸을 지나 도착할 수 있다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 별로 미로의 크기 N과 N개의 줄에 걸쳐 미로의 통로와 벽에 대한 정보가 주어진다. 5<=N<=100
#  0은 통로, 1은 벽, 2는 출발, 3은 도착이다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.



def issafe(y,x):
    if x < 0 or x > case-1 or y < 0 or y > case-1:
        return False
    else:
        return True

test = int(input())
for tc in range(test):
    datas = []
    case = int(input())
    for row in range(case):
        datas.append(list(map(int,input())))

    start_y = start_x = None
    for y in range(case):
        for x in range(case):
            if datas[y][x] == 2:
                now_y = y
                now_x = x
                break

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    visited = []
    path_q = []
    path_q.append((now_y,now_x))
    result = 0
    distance = [[0]*case for i in range(case)]

    while path_q != []:
        path = path_q.pop(0)
        now_y = path[0]
        now_x = path[1]
        visited.append((now_y,now_x))

        if datas[now_y][now_x] == 3:
            result = 1
            break

        else:
            for delta in range(4):
                new_y = now_y + dy[delta]
                new_x = now_x + dx[delta]

                if issafe(new_y,new_x) and not (new_y,new_x) in visited and datas[new_y][new_x] != 1:
                    y = new_y
                    x = new_x
                    path_q.append((y,x))
                    distance[y][x] = distance[now_y][now_x] + 1
    
    if result == 1: 
        print(f'#{tc+1} {distance[now_y][now_x]-1}')
    else:
        print(f'#{tc+1} {0}')








    # dy = [-1, 0, 1, 0]
    # dx = [0, 1, 0, -1]
    # path = []
    # visited = []
    # result = 0
    # now_d = -1
    # distance = []
    # # parent = []

    # path += [[now_y,now_x]] #[4,3]
    # visited += [[now_y,now_x]] #[4,3]
    # now_d += now_d # 0
    # distance += [now_d] # 0
    # # parent.append(0)

    # now = path.pop(0)
    # now_y = now[y]
    # now_x = now[x]

    # while datas[now_y][now_x] != 3:

    #     for delta in range(4): 
    #         new_y = now_y + dy[delta]
    #         new_x = now_x + dx[delta]
    #         if issafe(new_y,new_x) and not [new_y,new_x] in visited and datas[new_y,new_x] != 1:
    #             path += [[new_y,new_x]] #[4,2],[3,3] -> [3,3],[4,1]
            
    #     now = path.pop(0) #[4,2] -> [3,3]
    #     now_y = now[y] # 4 -> 3
    #     now_x = now[x] # 2 -> 3
    #     visited += [[now_y,now_x]] #[4,3],[4,2] -> [4,3],[4,2],[3,3]
    #     # now_d += 1 # 1
    #     # distance += [now_d] # [0,1]




