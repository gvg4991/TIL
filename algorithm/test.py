
a = [1,4,6,5,5]
for aa in a:
    if aa==4:
        a.remove(4)
    print(aa)
print(a)


# for i in range(0):
#     print(i)
#
# a = [0,1,2,3,4,5]
# print(a[9])

#
# a=[[1,2,3,4],[6,7,8,9],[3,3,3,3]]
# print(a)
# b=a[0:2][0:2]
# print(b)
# b=list(zip(*b))
# print(b)

# for i in range(3):
#     a[0+3-1-i][1] = a[0][1+i]
# print(a)
# print(list(zip(*a)))
# print(a[::-1])
# print(list(zip(*a[::-1])))

# a[0][0],a[0][1],a[1][0],a[1][1] = a[1][0], a[0][0], a[1][1], a[0][1]
# print(a)

#
# a = (-1)//5
# b = (-1)%5
# print(a,b)
# c = 1%5
# print(c)

# a= [[0],1,1,1,1,2,3]
# b = list(set(a))
# print(b)


#
# a = [0,0,[1,2],0]
# a[3] = a[2].copy()
# a[3] += [3]
# print(a)


# a = [1,2,3]
# if [1,5] in a:
#     print('yo')
# else:
#     print('f')

# a = [1,2,3,3,3,4,5]
# b = a.count(3)
# c = a.index(6)
# print(b)
# print(c)

#
# import collections
# a = collections.deque()
# a.appendleft([1,2,3])
# a.append(5)
# print(a)
# a.popleft()
# print(a)
#
# import itertools
# a = itertools.combinations([1,2,3,4],2)
# print(list(a))
# b = itertools.permutations([1,2,3,4],2)
# print(list(b))
#
#
# import copy
# a = list([1,2,3,4,[5,5]])
# b = a.copy()
# c = copy.deepcopy(a)
# a[0] = 9
# print(a,b,c)
# a[4][1] = 6
# print(a,b,c)




# def test():
#     a = [1,2,3,4]
#     b = 9999
#     return a,b
#
# test_a, test_b = test()
# print(test_a,test_b)


# horse = [[[1,2,3],[]],[[],[6,5,4]]]
# target = horse[1][1][1:]
# print(target)
# target = target[::-1]
# print(target)


# a = [1,2,3]
# a += [4]
# print(a)
# a.pop(1)
# print(a)



# a = int(12.9999)
# print(a)



# V개의 노드 개수와 방향성이 없는 E개의 간선 정보가 주어진다.
# 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있는지 알아내는 프로그램을 만드시오.
# 예를 들어 다음과 같은 그래프에서 1에서 6으로 가는 경우, 두 개의 간선을 지나면 되므로 2를 출력한다.
# 노드 번호는 1번부터 존재하며, 노드 중에는 간선으로 연결되지 않은 경우도 있을 수 있다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄부터 테스트 케이스의 첫 줄에 V와 E가 주어진다. 5<=V=50, 4<=E<=1000
# 테스트케이스의 둘째 줄부터 E개의 줄에 걸쳐, 간선의 양쪽 노드 번호가 주어진다.
# E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.
#
# test = int(input())
# for tc in range(test):
#     v, e = map(int, input().split())
#     mymap = [[0] * (v + 1) for i in range(v + 1)]
#     for case in range(e):
#         start, end = map(int, input().split())
#         mymap[start][end] = 1
#         mymap[end][start] = 1
#     s, g = map(int, input().split())
#
#     queue = []
#     queue.append(s)# [1]
#     distance = [0] * (v + 1)  # [-1,-1,-1,...]
#     visited = [0] * (v + 1)
#
#     if s == g:  # 1 == 6
#         result = distance[s]  # 0
#     else:
#         while s != g and queue != []:
#             s = queue.pop(0)  # 1 -> 3
#             visited[s] = 1
#
#             if s == g:  # 1 == 6
#                 result = distance[s]  # 0
#                 break
#
#             else:
#                 for path in range(1, v + 1):  # 3
#                     if visited[path] == 0 and distance[path] == 0 and mymap[s][path] > 0:  # 3,4
#                         visited[path] = 1
#                         queue.append(path)  # [3,4]
#                         distance[path] = distance[s] + 1
#
#     print(result)

# test = int(input())
# for tc in range(test):
#     v,e = map(int,input().split())
#     mymap = [[0]*(v+1) for i in range(v+1)]
#     for case in range(e):
#         start, end = map(int,input().split())
#         mymap[start][end] = 1
#         mymap[end][start] = 1
#     s, g = map(int,input().split())

#     queue = []
#     queue.append(s) # [1]
#     distance = [0] * (v+1) # [-1,-1,-1,...]
#     visited = [0] * (v+1)

#     while s != g and queue != []:
#         s = queue.pop(0) # 1 -> 3
#         visited[s] = 1

#         if s == g: # 1 == 6
#             result = distance[s] # 0
#             break

#         else:
#             for path in range(1,v+1): # 3
#                 # if distance[path] == 0 and mymap[s][path] > 0: # 3,4
#                 if visited[path] == 0 and mymap[s][path] > 0: # 3,4
#                     queue.append(path) # [3,4]
#                     distance[path] = distance[s] + 1

#     print(f'#{tc+1} {result}')
