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

