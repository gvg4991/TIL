import sys
sys.stdin = open('input.txt')


n,k = map(int,input().split()) #노드 수, 경로 수
datas = [[987654321]*n for _ in range(n)]
for case in range(k):
    start,end,dist = map(str,input().split())
    if start == 'a': start = 0
    elif start == 'b': start = 1
    elif start == 'c': start = 2
    elif start == 'd': start = 3
    elif start == 'e': start = 4
    elif start == 'f': start = 5
    if end == 'a': end = 0
    elif end == 'b': end = 1
    elif end == 'c': end = 2
    elif end == 'd': end = 3
    elif end == 'e': end = 4
    elif end == 'f': end = 5
    datas[start][end] = int(dist)
# print(datas)


begin = 0
distance = datas[begin] #처음 거리리스트는 idx=0을 출발지로 하는 거리
# print(distance)
# for now in range(n):
#     if not distance[now]:
#         distance[now] = 987654321
# print(distance)


# node = [0]*n
# for i in range(n):
#     node[i] = i
# # print(node)
node = [1,2,3,4,5]


path = []
while node:
    result = 987654321
    # print(distance)
    for now in node: #남아있는 노드를 순서대로 불러옴
        # print(now)
        if distance[now] < result: #불러온 노드의 distance가 지금까지 결과값보다 작으면
            result = distance[now] #distance를 result에 넣음 (3
    idx = distance.index(result) #결과값의 인덱스 추출
    path.append(idx) #경로에 추가
    # print(idx)
    node.remove(idx) #인덱스값의 노드를 제거
    for next in node: #다음 순서를 정하기 위해 제거 후 남은 노드를 순서대로 불러옴
        # print('#{} {} {}'.format(distance[next],distance[idx],datas[idx][next])) #원래 갈수있는 거리, 지금위치까지 거리, 지금위치에서 갈수있는 거리
        if distance[next] > distance[idx] + datas[idx][next]: #기존의 위치에서 디스턴스보다 지금 위치에서가는 거리가 더 작으면
            distance[next] = distance[idx] + datas[idx][next]
print(distance[-1])
print(path)


# while node:
#     result = 987654321
#     for next in range(n):
#         if not next in visited and distance[next] < result:
#             result = distance[next]
#     now = distance.index(result)
#     visited.append(now)
#     # for target in range(n):
#     #     if not target in visited and distance[target] > datas[now][target]:
#     #         distance[target] = datas[now][target]
#     print(distance)
#     print(visited)







# begin = 0
# distance = datas[begin]
# visited = []
# while len(visited) < n:
#     result = 987654321
#     for next in range(n):
#         if not next in visited and distance[next] < result:
#             result = distance[next]
#     now = distance.index(result)
#     visited.append(now)
#     # for target in range(n):
#     #     if not target in visited and distance[target] > datas[now][target]:
#     #         distance[target] = datas[now][target]
#     print(distance)
#     print(visited)


    # if result > distance[next]:
    #     result = distance[next] #3
    #     now = next #b



# def dijkstra(s,e,d):
#     # if 종료
#
#     distance = datas[s]
#     result = 987654321
#     for next in range(n):
#         if result > distance[next]:
#             result = distance[next]  # 3
#             now = next  # b
