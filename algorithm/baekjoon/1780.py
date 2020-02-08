# 문제
# N×N크기의 행렬로 표현되는 종이가 있다. 종이의 각 칸에는 -1, 0, 1의 세 값 중 하나가 저장되어 있다. 우리는 이 행렬을 적절한 크기로 자르려고 하는데, 이때 다음의 규칙에 따라 자르려고 한다.
#
# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.
# 이와 같이 종이를 잘랐을 때, -1로만 채워진 종이의 개수, 0으로만 채워진 종이의 개수, 1로만 채워진 종이의 개수를 구해내는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 N(1≤N≤3^7, N은 3^k 꼴)이 주어진다. 다음 N개의 줄에는 N개의 정수로 행렬이 주어진다.
#
# 출력
# 첫째 줄에 -1로만 채워진 종이의 개수를, 둘째 줄에 0으로만 채워진 종이의 개수를, 셋째 줄에 1로만 채워진 종이의 개수를 출력한다.


import sys
sys.stdin = open('input.txt')


# def same_cnt(y,x,s):
#     global ans_1, ans0, ans1
#     check_1 = [[-1]*s for _ in range(s)]
#     check0 = [[0]*s for _ in range(s)]
#     check1 = [[1]*s for _ in range(s)]
#     change = [['']*s for _ in range(s)]
#         if datas[] == -1:
#             ans_1 += 1
#         elif check[0] == 0:
#             ans0 += 1
#         elif check[0] == 1:
#             ans1 += 1
#         return
#     else:
#         scale = s**(1//2)
#         for i in range(scale):
#             for j in range(scale):
#                 same_cnt(y+i*scale,x+j*scale,scale)
#
#
# case = int(input())
# datas = [[0]*case for _ in range(case)]
# for i in range(case):
#     datas[i] = list(map(int,input().split()))
# # print(datas)
#
# scale = case
# ans0 = ans_1 = ans1 = 0
# # check = list(set(datas))
# target = []
# tl = []
#
# same_cnt(0,0,scale)
# print(ans_1)
# print(ans0)
# print(ans1)









def same_cnt(y,x,s):
    global ans_1, ans0, ans1, check
    target = []
    for row in range(s):
        target.extend(list(set(datas[y+row][x:x+s])))
    check = list(set(target))
    if len(check) == 1:
        if check[0] == -1:
            ans_1 += 1
        elif check[0] == 0:
            ans0 += 1
        elif check[0] == 1:
            ans1 += 1
        return
    else:
        scale = int(s**(1/2))
        for i in range(scale):
            for j in range(scale):
                same_cnt(y+i*scale,x+j*scale,scale) #시작점들, scale==0일땐?


case = int(input())
datas = [[0]*case for _ in range(case)]
for i in range(case):
    datas[i] = list(map(int,input().split()))
# print(datas)

scale = case
ans0 = ans_1 = ans1 = 0
# check = list(set(datas))
target = []
tl = []

same_cnt(0,0,scale)
# print(check)
print(ans_1)
print(ans0)
print(ans1)





# def same_cnt(t):
#     global check, ans_1, ans0, ans1, scale
#     for row in t:
#         for data in row:
#             tl.append(data)
#     check = list(set(tl))
#     if len(check) == 1:
#         if check[0] == -1:
#             ans_1 += 1
#         elif check[0] == 0:
#             ans0 += 1
#         elif check[0] == 1:
#             ans1 += 1
#         return
#     else:
#         # scale = scale**(1/2)
#         # for i in range(scale):
#         #     for j in range(scale):
#         #         pass #함수에 넣어서 확인 def(y+i*next,x+j*next,next)
#         scale = scale**(1//2)
#         for point in range(scale):
#             target = datas[point*scale:point*scale+scale-1][point*scale:point*scale+scale-1]
#             # check = list(set(target))
#             same_cnt(target)

