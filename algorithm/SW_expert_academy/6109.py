# 2048이라는 추억의 게임을 아는가? 2048은 한 때 유명했던 1인용 게임으로, 격자 위에서 숫자가 적힌
# 타일들을 밀어서 합치고 최종적으로 2048을 만들어 내는 것이 목표인 게임이다.
# 한번 타일을 밀 때는 상하좌우를 정해서 밀어야 한다.
# 방향을 정하면 격자 위에 있는 모든 타일이 그 방향으로 밀린다.
# 만약 어떤 타일이 밀리는 방향에 다른 타일이 있고, 두 타일에 적힌 숫자가 같다면 두 타일은 합쳐져
# 새로운 하나의 타일이 되고 이 타일에 적힌 숫자는 합쳐진 숫자들의 합이 된다.
# 이렇게 합쳐져서 만들어진 새로운 타일은 숫자가 같은 다른 타일이 밀려와도 합쳐져서는 안 된다.
# 만약 같은 숫자가 적힌 타일이 세 개 이상 있을 때는 헷갈리는 경우를 없애기 위해 빨리 벽에 닿게 될 타일을 먼저 민다고
# 생각한다.
# 예를 들어 “2 2 4 2 2 2”가 적힌 타일들이 있을 때, 이 타일들을 왼쪽으로 밀면 결과는 “4 4 4 2 0 0”이 된다.
# 0은 타일이 없는 빈 칸을 나타낸다.
# 위의 그림은 4×4 크기의 격자(일반적인 2048 게임)에서 모든 타일을 오른쪽으로 이동시킨 예이다.
# 우리는 2048게임을 N×N 크기의 격자에서 하려고 한다.
# 현재 격자에 어떤 식으로 타일이 있는지 주어지고, 타일들을 이동시킬 방향이 주어질 때,
# 타일을 모두 이동시키고 나면 격자가 어떻게 변할 지 계산하는 프로그램을 작성하라.
# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 하나의 정수 N(1≤N≤20)과 하나의 문자열 S가 공백 하나로 구분되어 주어진다.
# S는 “left”, “right”, “up”, “down”의 넷 중 하나이며 각각 타일들을 왼쪽, 오른쪽, 위쪽, 아래쪽으로 이동시키겠다는 뜻이다.
# 다음 N개의 줄의 i번째 줄에는 N개의 정수가 공백 하나로 구분되어 주어진다.
# 이 정수들은 0이거나 2이상 1024이하의 2의 제곱수들이다.
# i번째 줄의 j번째 정수는 격자의 위에서 i번째 줄의 왼쪽에서 j번째에 있는 칸에 있는 타일에 어떤 정수가 적혀 있는지 나타내며,
# 0이면 이 칸에 타일이 없음을 의미한다.
# [출력]
# 각 테스트 케이스마다 ‘#t’(t는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고 한 줄을 띄운 후,
# N줄에 걸쳐 격자의 어떤 위치에 어떤 숫자가 적힌 타일이 있는지 입력 형식과 같은 형식으로 출력한다.


import sys
sys.stdin = open("input.txt")


# def check(s):
#     global count
#     value = datas[s].pop(0)
#     count += 1
#     if value == 0:
#         check(s)
#     return value

# def left(n):
#     global count, datas
#     for y in range(n):
#         for front0 in range(n - count):
#             front = datas[y].pop(0)
#             count += 1
#             if front != 0:
#                 break
#         for back0 in range(n - count):
#             back = datas[y].pop(0)
#             count += 1
#             if back != 0:
#                 break
#         while count < n:
#             if front == back:
#                 front = front + back
#                 datas[y].append(front)
#                 front = back = 0
#                 for front0 in range(n - count):
#                     front = datas[y].pop(0)
#                     count += 1
#                     if front != 0:
#                         break
#                 for back0 in range(n - count):
#                     back = datas[y].pop(0)
#                     count += 1
#                     if back != 0:
#                         break
#             else:
#                 datas[y].append(front)
#                 front = back
#                 back = datas[y].pop(0)
#                 count += 1
#         datas[y].append(front)
#         datas[y].append(back)
#
#             # front = check(y)
#             # back = check(y)
#             # if front == back:
#             #     front = front + back
#             #     datas[y].append(front)
#             # else:
#             #     datas[y].append(front)
#             #     datas[y].append(back)
#             # front = back = 0
#
#
# test = int(input())
# for tc in range(test):
#     n,s = map(str,input().split())
#     n = int(n)
#     datas = []
#     for case in range(n):
#         datas.append(list(map(int,input().split())))
#
#     count = 0
#
#     if s == 'up':
#         up(n)
#     elif s == 'down':
#         down(n)
#     elif s == 'left':
#         left(n)
#     elif s == 'right':
#         right(n)




test = int(input())
for tc in range(test):
    n,s = map(str,input().split())
    n = int(n)
    datas = []
    for case in range(n):
        datas.append(list(map(int,input().split())))

    a = list(map(list,zip(*datas))) #위로
    # print(a)
    b = list(map(list,zip(*datas[::-1]))) #아래로
    # print(b)
    c = list(map(list,zip(*b[::-1])))[::-1] #오른쪽
    # print(c)
    if s == 'right':
        datas = c
    elif s == 'up':
        datas = a
    elif s == 'down':
        datas = b

    print('#{}'.format(tc+1))
    ans = []
    for line in range(n):
        i = 0
        check = []
        result = []

        while i < n:
            target = datas[line].pop(0)
            i += 1
            if target != 0:
                check.append(target)

            if len(check) == 2:
                if check[0] == check[1]:
                    result.append(check[0]+check[1])
                    check = []
                else:
                    value = check.pop(0)
                    result.append(value)

        for yo in check:
            result.append(yo)
        for yo in range(n-len(result)):
            result.append(0)

        ans.append(result)
        # print(ans)
        #4 8 2 4 0
        #8 2 8 0 0
        #8 2 8 0 0
        #4 4 8 0 0
        #4 0 0 0 0
        #16 2
        #2 0

    a = list(map(list,zip(*ans))) #위로
    # print(a)
    b = list(map(list,zip(*ans)))[::-1] #아래로
    # print(b)
    c = list(map(list,zip(*b))) #오른쪽
    # print(c)
    if s == 'right':
        ans = c
    elif s == 'up':
        ans = a
    elif s == 'down':
        ans = b

    for yo in ans:
        print(*yo)










## 지현이 코딩
# def Game():
#     for y in range(N):
#         arr=[]
#         lst=[]
#         for x in range(N):
#             if Data[y][x]!=0:
#                 lst.append(Data[y][x])
#
#
#         for i in range(len(lst)-1):
#             if lst[i]==lst[i+1]:
#                 lst[i]*=2
#                 lst[i+1]=0
#
#         for i in range(len(lst)):
#             if lst[i]!=0:
#                 arr.append(lst[i])
#
#
#         arr+=[0]*(N-len(arr))
#         Mymap.append(arr)
#
#
#
#
# TC=int(input())
# for tc in range(1,TC+1):
#     print("#%d"%tc)
#     N,S=input().split()
#     N=int(N)
#     Data=[0]*N
#     for n in range(N):
#         Data[n]=list(map(int,input().split()))
#
#     if N==1:
#         print(Data)
#         break
#
#     if S=='right':
#         for y in range(N):
#             Data[y]=Data[y][::-1]
#
#     if S=='up':
#         Data=list(map(list,zip(*Data)))
#
#     if S=='down':
#         Data=list(map(list,zip(*Data)))
#         for y in range(N):
#             Data[y]=Data[y][::-1]
#     Mymap = []
#     Game()
#     if S == 'right':
#         for y in range(N):
#             Mymap[y] = Mymap[y][::-1]
#
#     if S == 'up':
#         Mymap = list(map(list, zip(*Mymap)))
#
#     if S == 'down':
#         for y in range(N):
#             Mymap[y] = Mymap[y][::-1]
#         Mymap = list(map(list, zip(*Mymap)))
#
#     for y in range(N):
#         for x in range(N):
#             print(Mymap[y][x],end=' ')
#         print()
