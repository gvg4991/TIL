# 그림과 같이 인덱스가 있는 10x10 격자에 빨간색과 파란색을 칠하려고 한다.
# 개의 영역에 대해 왼쪽 위와 오른쪽 아래 모서리 인덱스, 칠할 색상이 주어질 때, 칠이 끝난 후 색이 겹쳐 보라색이 된 칸 수를 구하는 프로그램을 만드시오.
# 주어진 정보에서 같은 색인 영역은 겹치지 않는다.
# 예를 들어 2개의 색칠 영역을 갖는 위 그림에 대한 색칠 정보이다.
# 2
# 2 2 4 4 1  ( [2,2] 부터 [4,4] 까지 color 1 (빨강) 으로 칠한다 )
# 3 3 6 6 2 ( [3,3] 부터 [6,6] 까지 color 2 (파랑) 으로 칠한다 )
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.   ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 칠할 영역의 개수 N이 주어진다. ( 2 ≤ N ≤ 30 )
# 다음 줄에 왼쪽 위 모서리 인덱스 r1, c1, 오른쪽 아래 모서리 r2, c2와 색상 정보 color가 주어진다. ( 0 ≤ r1, c1, r2, c2 ≤ 9 )
#  color = 1 (빨강), color = 2 (파랑)
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# test = int(input())
# for tc in range(test):
#     case = int(input())
#     datas = []
#     for case_num in range(case):
#         datas += [list(map(int,input().split()))]
#     # [[Ax1,Ay1,Ax2,Ay2,Acolor],[Bx1,By1,Bx2,By2,Bcolor],...]
#     # 가로 = datas[0][0] ~ datas[0][2]+1 
#     # 세로 = datas[0][1] ~ datas[0][3]+1

#     for row in range(case):
#         for y in range(datas[row][1],datas[row][3]+1):
#             for x in range(datas[row][0],datas[row][2]):

    
test = int(input())
for tc in range(test):
    case = int(input())
    red = []
    blue = []
    for case_num in range(case):
        datas = list(map(int,input().split()))
    # [[Ax1,Ay1,Ax2,Ay2,Acolor],[Bx1,By1,Bx2,By2,Bcolor],...]
    # 가로 = datas[0] ~ datas[2]+1 
    # 세로 = datas[1] ~ datas[3]+1
        garo = datas[2]+1-datas[0]
        sero = datas[3]+1-datas[1]
        for y in range(sero):
            for x in range(garo):
                if datas[4] == 1:
                    red += [[datas[0]+x,datas[1]+y]] #[[2,2],[2,3],[3,2],[3,3]]
                elif datas[4] == 2:
                    blue += [[datas[0]+x,datas[1]+y]]
    # print(red)
    # print(blue)

    # count = 0
    # for red_i in red:
    #     if red_i in blue:
    #         count += 1
    # print(f'#{tc+1} {count}')

    count = 0
    for red_i in red:
        for blue_i in blue:
            if red_i == blue_i:
                count += 1
    print(f'#{tc+1} {count}')

                    
