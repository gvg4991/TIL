# 문제
# 상근이와 친구들은 오스트레일리아로 여행을 떠났다. 상근이와 친구들은 총 M명이고, 지금 공항에서 한 줄로 서서 입국심사를 기다리고 있다. 입국심사대는 총 N개가 있다. 각 입국심사관이 심사를 하는데 걸리는 시간은 사람마다 모두 다르다. k번 심사대에 앉아있는 심사관이 한 명을 심사를 하는데 드는 시간은 Tk이다.
# 가장 처음에 모든 심사대는 비어있고, 심사를 할 준비를 모두 끝냈다. 상근이와 친구들은 비행기 하나를 전세내고 놀러갔기 때문에, 지금 심사를 기다리고 있는 사람은 모두 상근이와 친구들이다. 한 심사대에서는 한 번에 한 사람만 심사를 할 수 있다. 가장 앞에 서 있는 사람은 비어있는 심사대가 보이면 거기로 가서 심사를 받을 수 있다. 하지만 항상 이동을 해야 하는 것은 아니다. 더 빠른 심사대의 심사가 끝나길 기다린 다음에 그 곳으로 가서 심사를 받아도 된다.
# 상근이와 친구들은 모두 컴퓨터 공학과 학생이기 때문에, 어떻게 심사를 받으면 모든 사람이 심사를 받는데 걸리는 시간이 최소가 될지 궁금해졌다.
# 예를 들어, 두 심사대가 있고, 심사를 하는데 걸리는 시간이 각각 7초와 10초라고 하자. 줄에 서 있는 사람이 6명이라면,
# 가장 첫 두 사람은 즉시 심사를 받으러 가게 된다. 7초가 되었을 때, 첫 번째 심사대는 비어있게 되고,
# 세 번째 사람이 그곳으로 이동해서 심사를 받으면 된다. 10초가 되는 순간, 네 번째 사람이 이곳으로 이동해서 심사를 받으면 되고,
# 14초가 되었을 때는 다섯 번째 사람이 첫 번째 심사대로 이동해서 심사를 받으면 된다. 20초가 되었을 때, 두 번째 심사대가 비어있게 된다.
# 하지만, 여섯 번째 사람이 그 곳으로 이동하지 않고, 1초를 더 기다린 다음에 첫 번째 심사대로 이동해서 심사를 받으면, 모든 사람이 심사를 받는데 걸리는 시간이 28초가 된다. 만약, 마지막 사람이 1초를 더 기다리지않고,
# 첫 번째 심사대로 이동하지 않았다면, 모든 사람이 심사를 받는데 걸리는 시간이 30초가 되게 된다.
# 상근이와 친구들이 심사를 받는데 걸리는 시간의 최솟값을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 N과 M이 주어진다. (1 ≤ N ≤ 100,000, 1 ≤ M ≤ 1,000,000,000)
# 다음 N개 줄에는 각 심사대에서 심사를 하는데 걸리는 시간인 Tk가 주어진다. (1 ≤ Tk ≤ 109)
# 출력
# 첫째 줄에 상근이와 친구들이 심사를 마치는데 걸리는 시간의 최솟값을 출력한다. 



import sys
sys.stdin = open('input.txt')


# def test(l,r,t):
#     global cnt
#     cnt = 0
#     for i in range(k):
#         target = datas[i]
#         cnt += t//target #시간동안 통과할 수 있는 총 사람 수
#     if cnt == n:
#         result.append(t)
#         return
#     elif cnt > n:
#         r = t
#         t = (l+r)//2
#         test(l,r,t)
#     elif cnt < n:
#         l = t
#         t = (l+r)//2
#         test(l,r,t)


# 느려느려!
# def test(l,r,t):
#     global cnt, result
#     cnt = 0
#     for i in range(k):
#         target = datas[i]
#         cnt += t//target #시간동안 통과할 수 있는 총 사람 수
#     if cnt == n:
#         while cnt == n:
#             if result>t:
#                 result = t
#             # result.append(t)
#             cnt = 0
#             t -= 1
#             for i in range(k):
#                 target = datas[i]
#                 cnt += t//target #시간동안 통과할 수 있는 총 사람 수
#         return
#     elif cnt > n:
#         r = t
#         t = (l+r)//2
#         test(l,r,t)
#     elif cnt < n:
#         l = t
#         t = (l+r)//2
#         test(l,r,t)
#
#
# k,n = map(int,input().split())
# datas = [0]*k
# for i in range(k):
#     datas[i] = int(input())
# # print(datas)
#
# r = max(datas)*n
# l = min(datas)
# t = max(datas)*n
# cnt = 0
# result = 987654321
#
# if n == 0:
#     result = 0
# elif n == 1:
#     result = l
# else:
#     test(l,r,t)
# print(result)





n,goal = map(int, input().split())
test = []
for i in range(n):
    test.append(int(input()))

r = max(test)*goal
l = min(test)

while l <= r:
    cnt = 0
    mid = (r+l)//2
    for i in range(n):
        target = test[i]
        cnt += mid//target #시간동안 통과할 수 있는 총 사람 수

    if cnt >= goal:
        r = mid-1
    elif cnt < goal:
        l = mid+1
print(l)
