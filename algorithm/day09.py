# queue = [0]*10
# front = -1
# rear = -1
#
# rear += 1; queue[rear] = 1
# rear += 1; queue[rear] = 2
# rear += 1; queue[rear] = 3
#
# while front != rear:
#     front += 1
#     print(queue[front])
#


#------------------------------------------------------------------------------------------------------
# 일본군 자결

# queue = [0]*1000
# front = rear = -1
#
# for i in range(1,42):
#     rear += 1
#     queue[rear] = i
#
# while rear - front > 2:
#     front += 1
#     rear += 1
#     queue[rear] = queue[front]
#     front += 1
#     rear += 1
#     queue[rear] =queue[front]
#     front += 1
#
# # print(queue[front]) 마지막 자결
# print(queue[front+1])
# print(queue[front+2])



#------------------------------------------------------------------------------------------------------
# BFS


datas = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]

start = []
end = []
harf = int(len(datas)/2)
for case in range(harf):
    start += [datas[2*case]] #[1,1,2,2,4,5,6,3]
    end += [datas[2*case+1]] #[2,3,4,5,6,6,7,7]

mymap = [[0] * (8) for i in range(8)]
for mapping in range(harf):
    mymap[start[mapping]][end[mapping]] = 1
    mymap[end[mapping]][start[mapping]] = 1
# print(mymap)

queue = []
front = rear = -1

now = 0
visited = [0] * 8
path = -1 # 이동하면 1씩 추가
mom = None
result = []

queue.append(1) # [1]

while queue != []: # and not 0 in visited[1:] 은?
    now = queue.pop(0) # 1 -> 2 -> 3 -> 4 -> 5 -> 7 -> 6
    visited[now] = 1
    result.append(now) # [1] -> [1,2] -> [1,2,3] -> [1,2,3,4] -> [1,2,3,4,5] -> [1,2,3,4,5,7] -> [1,2,3,4,5,7,6]
    for x in range(8):
        if mymap[now][x] == 1 and visited[x] == 0:
            queue.append(x) # [2,3] -> [3,4,5] -> [4,5,7] -> [5,7,6] -> [7,6] -> [6]
    path += 1

print(result)


#------------------------------------------------------------------------------------------------------
# # BFS 강사님
#
# queue = []
# front = rear = -1
#
# def bfs(here):
#     global front, rear
#     rear += 1
#     queue[rear] = here
#     visited[here] = True
#
#     while front != rear:
#         front += 1
#         here = queue[front]
#         print(here)
#
#         for next in range(8):
#             if mymap[here][next] and not visited[next]:
#                 visited[next] = True
#                 distance[next] = distance[here] + 1
#                 parent[next] = here
#                 rear += 1
#                 queue[rear] = next