# import sys
# sys.stdin = open("input.txt")

# 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
# 출력: 454

# a = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

# a.pop(1)
# # print(a)

# c=[]
# for i in range(5):
#     c += [[0,1]]

# print(c)

# d=c.pop()
# print(c)
# print(d)

# p = [2,3]
# c[0] = p
# print(c)

# print(c[0][1])

# c[1][1]=c[1][1]*5
# print(c)

# a=[]
# b=[1,3]
# a.append([1,3])

# print(a)


# result = []
# i = [2,3,4,5,1,2,3,4,1,2,3,1,2,1]
# if not int(9) in i:
#     print('yo')

# w=[]
# w.append((1,2))
# print(w)
# wi=w.pop(0)
# q1=wi[0]
# q2=wi[1]
# print(q1)
# print(q2)


# w = ((1,2),(10,20),(100,200))
# a=w[2][1]
# print(a)

# a=5
# b=[1,3,5,7,9]
# print('#{y},{x}'.format(x=a+2,y=b))

# d={}
# a=[1,2,3,4,1,3,5]
# # a.zip() 안돼!!
# for i in a:
#     d[i]=0
# # print(d)

# k=[]
# for find in d.keys():
#     k.append(find)
#     d[find] += 1
# print(k)
# print(d)

# case, n = map(str,input().split())
# print(case)
# print(n)

# x=14054
# datas = list(map(int,str(x)))
# print(datas)

# data = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2]
# for i in range(10):
#     print(data[0:i])

# data = [[0,0,0],[1,1,1],[2,2,2]]
# print(data[2][1])
#
# # data=[0,1,2,3]
# # print(data[2])

# data=[[1,2,3],[4,5,6],[7,8,9]]
# list(map(list,zip(*data)))
# print(data)

data=[[1,2,3],[4,5,6],[7,8,9]]
data = list(map(list,zip(*data)))
print(data)

# #
# l = [0,1,2,3,4,5,6,7,8,9,5,5]
# m = 'abddddsssd'
# # # print(l[::-2])
# # m = [2,3,4,5]
#
# # l = 941217
# # m = 412
# # l=l.replace(m,'-')
# # print(l)
#
# # l.remove(5)
# i = set(l)
# print(i)
#
# n=m.replace('d','z')
# print(n)

#
# l = [0,0,0,0,0,0]
# r = [1,2,3,4,5]
#
# l[1:4] = r[0:2]
# print(l)

# j=0
# while j<=4:
#     j += 1
# print(j)

# #int(str,n)
# #문자열을 n진법으로 생각하고 10진수로 바꾸기
# input = '1110'
# print(int(input,2)) #14
# print(int(input,4)) #84


# result = [0,1,2,3,4,5,6,7,8,9]
# start = 0
# # print(''.join(map(str,result[start:start+7])))
# a=''.join(map(str,result[start:start+7]))
# print(a)
# print(type(a))

# a = 'asd'
# print(a[1])


# k = '000000001DB176C588D26EC000'
# print(int(k,16))

# input = 1256666
# yo = list(map(str,input))
# datas = list(map(int,yo))
# print(datas)

# result = [0,1,3,5,7,9]
# a=str(map(str, result))
# print(a)

# # datas = [[' ']*9 for _ in range(10)]
# datas = [0]*9
# for i in range(-4,5):
#     # datas[4+i][4-(4-abs(i)):4+(4-abs(i))]='*'
#     datas[4-(4-abs(i)):4+(4-abs(i))]='*'*(4-abs(i)+1)
#     print(datas)


# #안되는거임!!
# datas = [[0,0,0,0,5],[1,1,1,1,5],[2,2,2,2,5],[3,3,3,3,5]]
# data = datas[1][2:4]
# print(data)

# a=3
# print(int(a**(1/2)))


# for i in range(10,5,-1):
#     print(i)

# yo = [1,2,3,4,5,6,7,8,9]
# y = [2,3,4]
# if y[0:2] in yo:
#     print(1)
# else:
#     print(0)

#
# i=[1,2,3,4,5]
# print(i)


# #인트형 데이터 리스트화
# a = 15688
# b = list(map(int,str(a)))
# print(b)

# datas = '123456789'
# # target = datas[::-1].index(7)
# # print(target)
# # a= datas.count(1)
# # datas[0],datas[1] = datas[1],datas[0]
# print(datas[0])


# datas = [[1,1,1],[2,2,2],[3,3,3]]
# print(list(map(list,zip(*datas))))
#
# a,b = divmod(-2,3)
# print(a,b)

# datas = [2,1,1,3,5,10,88,88,89,77,50]
# d = list(set(datas))
# print(d)
# print(datas)
#
# datas = [[1,10],[3,2],[8,8],[9,8],[50,8],[15,8]]
# datas.sort(key=lambda t:t[1])
# print(datas)

# datas = [1,2,3,4,5]
# supply = [6]*3
# result = datas + supply
# print(result)

# datas = [[1,2,3],[5,5,5],[7,8,9]]
# # print(datas)
# datas=list(map(list,zip(*datas)))
# print(datas)
# datas = list(map(list,zip(*datas)))
# print(datas)

# def check(x,n):
#     if n == 10:
#         return
#     if x:
#         print('전반부{}'.format(result))
#         result[x] = 1
#         check(x+1,n+1)
#     print('후반부{}'.format(x))

import copy

# def check(x,n,result):
#     res = copy.copy(result)
#     if n == 10:
#         return
#     if x:
#         print('전반부{}'.format(result))
#         result[x] = 1
#         check(x+1,n+1,result)
#         # result[x] -= 1
#         result = copy.copy(res)
#     print('후반부{}'.format(result))
# def check(x,n):
#     global result
#     res = copy.copy(result)
#     if n == 10:
#         return
#     if x:
#         print('전반부{}'.format(result))
#         # result[x] = 1
#         result.append(1)
#         check(x+1,n+1)
#         # result[x] -= 1
#         result = copy.copy(res)
#     print('후반부{}'.format(result))
#
# # result = [0]*11
# result = []
# check(1,0)


# input = str(10101111)
# a = [input[0],input[1],input[2],input[3],input[4],input[5],input[6],input[7]]
# print(a)

# a = [[0,0,0],[1,1,1],[2,2,2]]
# b = len(a[2][0:2])
# c = sum(a[1][0:3])
# print(b)
# print(c)

a = [1,2,3,4,5,6,7]
a.remove(1)
a.remove(2)
print(a)

