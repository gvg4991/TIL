# 그래프에서 사이클을 제거하고 모든 노드를 포함하는 트리를 구성할 때, 가중치의 합이 최소가 되도록 만든 경우를 최소신장트리라고 한다.
# 0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 이 그래프로부터 최소신장트리를 구성하는 간선의 가중치를 모두 더해 출력하는 프로그램을 만드시오.
# [입력]
# 첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
# 다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 
# 1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


import sys
sys.stdin = open("input.txt")


def find(x):
    if x != parent[x]: #조상 찾기
        return find(parent[x])
    else: #자신이랑 엄마가 같으면 즉, 자신이 엄마면
        return parent[x]

def union(x,y,z):
    global ans, cnt
    x = find(x) #x엄마 찾기
    y = find(y)
    if x!=y: #엄마가 다르면
        parent[y]=x #y의 엄마가 x가 됨
        ans += z
        cnt += 1

for tc in range(int(input())):
    n,p = map(int,input().split())
    node = [0]*(n+1)
    datas = [[0]*p for _ in range(p)]
    for i in range(n+1):
        node[i] = i #노드 만들기

    parent = [0]*(n+1) #엄마 지정해주기
    for make in range(n+1): #우선 엄마는 자기 자신
        parent[make] = make
    # print(parent)

    for i in range(p):
        datas[i] = list(map(int,input().split()))
    # print(datas)
    datas.sort(key=lambda x: x[2]) #2차원 리스트의 인덱스2의 값으로 오름차순
    # print(datas)

    ans = 0
    cnt = 0
    for path in datas:
        union(path[0],path[1],path[2])
        if cnt == n:
            break
    print('#{} {}'.format(tc+1,ans))







# n,k = map(int,input().split()) #노드 수, 경로 수
# datas = [[987654321]*n for _ in range(n)]
# for case in range(k):
#     start,end,dist = map(str,input().split())
#     datas[start][end] = int(dist)
# # print(datas)
#
#
# begin = 0
# distance = datas[begin] #처음 거리리스트는 idx=0을 출발지로 하는 거리
# # print(distance)
# # for now in range(n):
# #     if not distance[now]:
# #         distance[now] = 987654321
# # print(distance)
#
#
# # node = [0]*n
# # for i in range(n):
# #     node[i] = i
# # # print(node)
# node = [1,2,3,4,5]
#
#
# path = []
# while node:
#     result = 987654321
#     # print(distance)
#     for now in node: #남아있는 노드를 순서대로 불러옴
#         # print(now)
#         if distance[now] < result: #불러온 노드의 distance가 지금까지 결과값보다 작으면
#             result = distance[now] #distance를 result에 넣음 (3
#     idx = distance.index(result) #결과값의 인덱스 추출
#     path.append(idx) #경로에 추가
#     # print(idx)
#     node.remove(idx) #인덱스값의 노드를 제거
#     for next in node: #다음 순서를 정하기 위해 제거 후 남은 노드를 순서대로 불러옴
#         # print('#{} {} {}'.format(distance[next],distance[idx],datas[idx][next])) #원래 갈수있는 거리, 지금위치까지 거리, 지금위치에서 갈수있는 거리
#         if distance[next] > distance[idx] + datas[idx][next]: #기존의 위치에서 디스턴스보다 지금 위치에서가는 거리가 더 작으면
#             distance[next] = distance[idx] + datas[idx][next]
# print(distance[-1])
# print(path)