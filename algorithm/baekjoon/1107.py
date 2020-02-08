# 문제
# 수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.
# 리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. +를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고,
# -를 누르면 -1된 채널로 이동한다. 채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.
# 수빈이가 지금 이동하려고 하는 채널은 N이다. 어떤 버튼이 고장났는지 주어졌을 때,
# 채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오.
# 수빈이가 지금 보고 있는 채널은 100번이다.
# 입력
# 첫째 줄에 수빈이가 이동하려고 하는 채널 N (0 ≤ N ≤ 500,000)이 주어진다.  둘째 줄에는 고장난 버튼의 개수 M (0 ≤ M ≤ 10)이 주어진다. 고장난 버튼이 있는 경우에는 셋째 줄에는 고장난 버튼이 주어지며, 같은 버튼이 여러번 주어지는 경우는 없다.
# 출력
# 첫째 줄에 채널 N으로 이동하기 위해 버튼을 최소 몇 번 눌러야 하는지를 출력한다.


import sys
sys.stdin = open("input.txt")



def getsome(depth): #중복순열
    if depth == r: #r개 다 뽑으면
        data = ''.join(map(str,result))
        datas.append(int(data)) #result에 숫자값으로 넣어줌
        return
    for i in range(nn):
        result[depth] = can[i]
        getsome(depth+1)


start = 100
target = []
end = int(input()) #5457
goal = list(map(int,str(end))) #[5,4,5,7]
n = int(input())
if n>0:
    err = list(map(int,input().split()))
    can = []
    for i in range(10):
        if not i in err:
            can.append(i)
else:
    can = [0,1,2,3,4,5,6,7,8,9]
ans = abs(end-start)
datas = []

nn=len(can)
rr=len(goal)
for r in range(1,rr):
    result = [0]*r
    getsome(0)
datas.append(1*10**(len(goal)))

if start == end:
    ans = 0
elif can == []:
    ans = abs(end-start)
elif len(goal) >= abs(end-start):
    ans = abs(end-start)
else:
    for d in datas:
        if ans > len(str(d))+abs(end-d):
            ans = len(str(d))+abs(end-d)
print(ans)

# if ans > abs(end-start):
#     print(abs(end-start))
# else:
#     print(ans)
















#
# def combination(n, r, i, d): #n개 데이터 중 r개를 뽑을 때, i값이 d에 들어갈까?
#     global cnt
#     if r == 0: #r개 다 뽑았으면
#         # print(d)
#         data = ''.join(map(str,d))
#         datas.append(int(data)) #result에 숫자값으로 넣어줌
#         # print(result)
#         return
#     if i==n:
#         return
#     combination(n, r-1, i, d+[can[i]]) #들어갔을때 (똑같은 수 한번 더 들어갈 수 있음)
#     combination(n, r, i+1, d) #안들어갔을때
#
#
# start = 100
# target = []
# end = int(input()) #5457
# goal = list(map(int,str(end))) #[5,4,5,7]
# n = int(input())
# err = list(map(int,input().split()))
# can = []
# for i in range(10):
#     if not i in err:
#         can.append(i)
# ans = abs(end-start)
# datas = []
#
# nn=len(can)
# rr=len(goal)
# combination(nn, rr, 0, [])
# datas.append(1*10**(len(goal)))
# # print(result)
#
# if start == end:
#     ans = 0
# elif len(goal) >= abs(end-start):
#     ans = abs(end-start)
# else:
#     for d in datas:
#         if ans > len(str(d))+abs(end-d):
#             ans = len(str(d))+abs(end-d)
# print(ans)
#







# if start == end:
#     pass
# elif len(goal) >= abs(end-start):
#     ans += abs(end-start)
# else:
#     while len(target) != len(goal):
#         for g in goal:
#             ans += 1
#             if not g in err:
#                 target.append(g)
#             else:
#                 data = 987654321
#                 for c in can:
#                     if abs(data-g) > abs(g-c): #차이가 가장 작은 숫자 선택
#                         data = c
#                 target.append(data)
#
#     result = []
#     for i in range(len(goal)):
#         x = len(goal)-(1+i)
#         result.append((goal[i]-target[i])*(10**x))
#     # print(result)
#     ans += abs(sum(result))
#
# if ans > abs(end-start):
#     print(abs(end-start))
# else:
#     print(ans)

















# if start == end:
#     pass
# elif len(goal) >= abs(end-start):
#     ans += abs(end-start)
# else:
#     while len(target) != len(goal):
#         for g in goal:
#             ans += 1
#             if not g in err:
#                 target.append(g)
#             else:
#                 data = 987654321
#                 for c in can:
#                     if abs(data-g) > abs(g-c): #차이가 가장 작은 숫자 선택
#                         data = c
#                 target.append(data)
#
#     result = []
#     for i in range(len(goal)):
#         x = len(goal)-(1+i)
#         result.append((goal[i]-target[i])*(10**x))
#     # print(result)
#     ans += abs(sum(result))
#
# if ans > abs(end-start):
#     print(abs(end-start))
# else:
#     print(ans)