# 점심 시간에 산책을 다니는 사원들은 최근 날씨가 더워져, 사다리 게임을 통하여 누가 아이스크림을 구입할지 결정하기로 한다.
# 김 대리는 사다리타기에 참여하지 않는 대신 사다리를 그리기로 하였다.
# 사다리를 다 그리고 보니 김 대리는 어느 사다리를 고르면 X표시에 도착하게 되는지 궁금해졌다. 이를 구해보자.
# 아래 <그림 1>의 예를 살펴보면, 출발점 x=0 및 x=9인 세로 방향의 두 막대 사이에 임의의 개수의 막대들이 랜덤 간격으로 추가되고(이 예에서는 2개가 추가됨) 이 막대들 사이에 가로 방향의 선들이 또한 랜덤하게 연결된다.
# X=0인 출발점에서 출발하는 사례에 대해서 화살표로 표시한 바와 같이, 아래 방향으로 진행하면서 좌우 방향으로 이동 가능한 통로가 나타나면 방향 전환을 하게 된다.
# 방향 전환 이후엔 다시 아래 방향으로만 이동하게 되며, 바닥에 도착하면 멈추게 된다.
# 문제의 X표시에 도착하려면 X=4인 출발점에서 출발해야 하므로 답은 4가 된다. 해당 경로는 별도로 표시하였다.
# <그림 1> 사다리 게임에 대한 설명 (미니맵)
# 아래 <그림 2>와 같은 100 x 100 크기의 2차원 배열로 주어진 사다리에 대해서, 지정된 도착점에 대응되는 출발점 X를 반환하는 코드를 작성하라 (‘0’으로 채워진 평면상에 사다리는 연속된 ‘1’로 표현된다. 도착 지점은 '2'로 표현된다).
# <그림 2> 테스트 케이스에 의해 생성되는 실제 사다리의 모습
# [제약 사항]
# 한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속하여 이어지는 경우는 없다.
# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 번호가 주어지며, 바로 다음 줄에 테스트 케이스가 주어진다.
# 총 10개의 테스트 케이스가 주어진다.
# [출력]
#  #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 도착하게 되는 출발점의 x좌표를 출력한다. 


# def IsSafe(y,x): #데이터가 틀에서 벗어나지 않으면
#     if x>=0 and x<100 and y>=0 and y<100:
#         return True
#     else:
#         return False

# def sadari(y,x):
#     change = True
#     for di in range(3):
#         new_y = y + dy[di] # 99, 99, 98
#         new_x = x + dx[di] # start-1, start+1, start
#         if change and IsSafe(new_y, new_x) and  datas[new_y][new_x] == 1 : #지나간 자리 못가게하기! 왼쪽으로확정되면 위로가는건 확인안해도됨! 추가
#             # now = datas[new_y][new_x] # 현재위치의 값
#             now_y = new_y # 현재 위치의 y
#             now_x = new_x # 현재 위치의 x
#             change = False
#             datas[new_y][new_x] = 2
#     if now_y == 0:
#         print(f'#{case} {now_x}')
#         return
#     sadari(now_y,now_x)

# for i in range(10):
#     case = input()
#     datas = []
#     for row in range(100):
#         datas += [list(map(int,input().split()))]

#     finish_y = 99
#     for x in range(100):
#         if datas[finish_y][x] == 2:
#             finish_x = x
#     # datas[finish][start]는 도착지

#     dy = [0,0,-1]
#     dx = [-1, 1, 0]

#     sadari(finish_y, finish_x)


#------------------------------------------------------------------------------------------------------------------------------------------

for i in range(10):
    case = input()
    datas = []
    for row in range(100):
        datas += [list(map(int,input().split()))]

    finish_y = 99
    for x in range(100):
        if datas[finish_y][x] == 2:
            finish_x = x
    # datas[finish][start]는 도착지

    dy = [0,0,-1]
    dx = [-1, 1, 0]
    now_y = 99

    while now_y != 0:
        change = True
        for di in range(3):
            new_y = finish_y + dy[di] # 99, 99, 98
            new_x = finish_x + dx[di] # start-1, start+1, start
            if change and new_x>=0 and new_x<100 and new_y>=0 and new_y<100 and  datas[new_y][new_x] == 1 : 
                now_y = new_y # 현재 위치의 y
                now_x = new_x # 현재 위치의 x
                change = False
                datas[new_y][new_x] = 2
    
    print(f'#{case} {now_x}')
