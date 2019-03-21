# 삼성전자의 서비스 기사인 김대리는 회사에서 출발하여 냉장고 배달을 위해 N명의 고객을 방문하고 자신의 집에 돌아가려한다.
# 회사와 집의 위치, 그리고 각 고객의 위치는 이차원 정수 좌표 (x, y)로 주어지고 (0 ≤ x ≤ 100, 0 ≤ y ≤ 100)
# 두 위치 (x1, y1)와 (x2, y2) 사이의 거리는 |x1-x2| + |y1-y2|으로 계산된다.
# 여기서 |x|는 x의 절대값을 의미하며 |3| = |-3| = 3이다. 회사의 좌표, 집의 좌표, 고객들의 좌표는 모두 다르다.
# 회사에서 출발하여 N명의 고객을 모두 방문하고 집으로 돌아오는 경로 중 가장 짧은 것을 찾으려 한다.
# 회사와 집의 좌표가 주어지고, 2명에서 10명 사이의 고객 좌표가 주어질 때,
# 회사에서 출발해서 이들을 모두 방문하고 집에 돌아가는 경로 중 총 이동거리가 가장 짧은 경로를 찾는 프로그램을 작성하라.
# 여러분의 프로그램은 가장 짧은 경로의 이동거리만 밝히면 된다.
# 이 문제는 가장 짧은 경로를 ‘효율적으로’ 찾는 것이 목적이 아니다.
# 여러분은 모든 가능한 경로를 살펴서 해를 찾아도 좋다.
# 모든 경우를 체계적으로 따질 수 있으면 정답을 맞출 수 있다.
# [제약사항]
# 고객의 수 N은 2≤N≤10 이다.
# 그리고 회사의 좌표, 집의 좌표를 포함한 모든 N+2개의 좌표는 서로 다른 위치에 있으며 좌표의 값은 0이상 100 이하의 정수로 이루어진다.
# [입력]
# 가장 첫줄은 전체 테스트케이스의 수이다.
# 이후, 두 줄에 테스트 케이스 하나씩이 차례로 주어진다.
# 각 테스트 케이스의 첫째 줄에는 고객의 수 N이 주어진다. 둘째 줄에는 회사의 좌표,집의 좌표, N명의 고객의 좌표가 차례로 나열된다.
# 좌표는 (x,y)쌍으로 구성되는데 입력에서는 x와 y가 공백으로 구분되어 제공된다.
# [출력]
# 총 10줄에 10개의 테스트 케이스 각각에 대한 답을 출력한다.
# 각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음 최단 경로의 이동거리를 기록한다. 여기서 x는 테스트 케이스의 번호다.



import sys
sys.stdin = open("input.txt")



def lego(now):
    global result, ans
    visited[now] = True
    if not False in visited[2:node]:
        result += abs(start[now]-start[1])+abs(end[now]-end[1])
        if ans > result:
            ans = result
        result -= abs(start[now] - start[1]) + abs(end[now] - end[1])
        return

    for next in range(2,node):
        if not visited[next]:
            result += abs(start[now]-start[next])+abs(end[now]-end[next])
            if result > ans:
                pass
            lego(next)
            result -= abs(start[now]-start[next])+abs(end[now]-end[next])
            visited[next] = False


test = int(input())
for tc in range(test):
    case = int(input())
    datas = list(map(int,input().split()))

    #좌표
    node = len(datas) // 2
    start = [0]*node
    end = [0]*node
    # mymap = [[0]*node for _ in range(node)]
    for way in range(node):
        start[way] = datas[2*way]
        end[way] = datas[2*way+1]

    total = 0
    visited = [False]*node
    result = 0
    ans = 99999

    lego(0)
    print('#{} {}'.format(tc+1,ans))










#
# def getsome(depth):
#     if depth == node-1:
#         # print(result)
#         ans = ''.join(map(str,result))
#         path.append(ans)
#         # print(path)
#         return
#     for i in range(2,node):
#         if not visited[i]:
#             visited[i] = True
#             result[depth] = i
#             getsome(depth+1)
#             visited[i] = False
#
#
# test = int(input())
# for tc in range(test):
#     case = int(input())
#     datas = list(map(int,input().split()))
#
#     #좌표
#     node = len(datas) // 2
#     start = [0]*node
#     end = [0]*node
#     # mymap = [[0]*node for _ in range(node)]
#     for way in range(node):
#         start[way] = datas[2*way]
#         end[way] = datas[2*way+1]
#
#     #경로 순열
#     visited = [False]*node
#     result = [0] * (node - 1) + [1]
#     path = []
#     getsome(1)
#     # print(path) #str형식
#
#     #거리계산
#     x1 = start[0]
#     y1 = end[0]
#     x2 = y2 = None
#     distance = 0
#     total = []
#     for way in path:
#         for d in way[1:]:
#             x2 = start[int(d)]
#             y2 = end[int(d)]
#             distance += abs(x1-x2)+abs(y1-y2)
#             x1 = x2
#             y1 = y2
#         total.append(distance)
#         distance = 0
#
#     print('#{} {}'.format(tc+1,min(total)))

