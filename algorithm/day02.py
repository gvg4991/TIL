# 2차원 계산
import sys
sys.stdin = open("day02_01.txt","r")

def IsSafe(y,x): #데이터가 있는 값이면
    if x>=0 and x<5 and y>=0 and y<5:
        return True
    else:
        return False

def Mycalc(a,b):
    if a>b:
        return a-b
    else:
        return b-a


data01 = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    data01[i] = list(map(int,input().split()))
# print(data01)

dy = [-1,1,0,0]
dx = [0,0,-1,1]

sum = 0
for y in range(5):
    for x in range(5):
        for dir in range(4): # 4=len(dy)
            newY = y + dy[dir]
            newX = x + dx[dir]
            if IsSafe(newY, newX):
                sum += Mycalc(data01[y][x], data01[newY][newX])

print(sum)


#-----------------------------------------------------------------------------------------------------------------------
# 부분합
sys.stdin = open("day02_02.txt","r")
data02 = list(map(int,input().split()))

for i in range(1<<len(data02)): # 부분합 전체 갯수
    result = []
    for j in range(len(data02)+1): # 데이터 수, 2진수로 한번 확인할 때 수[1 0 1 0]=4개
        if i & (1<<j): #실제로 2진수로 바꿔서 검사하는 조건
            result.append(data02[j])
    # print(result)
            # if sum == 0:
            #     print(sum, end=",")
# bbotto='뽀또'
# print(f'{bbotto}:민호오빠 발냄새')


#-----------------------------------------------------------------------------------------------------------------------
# 이진검색

d = [1,2,3,4,5,6,7,8,9]
num = 10

start = 0 #d[start]=1
end= len(d)-1 #d[end]=9
mid = int((start + end)/2)
while d[mid] != num:
    mid = int((start + end)/2)
    if d[end] < num or d[start] > num:
        mid = False
        break
    else:
        if d[mid] > num:
           end = mid-1
        elif d[mid] < num:
            start = mid+1

if mid == False:
    print('error')
else:
    print(f'index는 {mid}, 결과값은 {d[mid]}.')


#-----------------------------------------------------------------------------------------------------------------------
#전체 검색

d = [1,2,3,4,5,6,7,8,9]
num = 3

result=None
for di in d:
    if di == num:
        result=di
        break
    else:
        result='error'
print(result)


#-----------------------------------------------------------------------------------------------------------------------
# 달팽이 배열

sys.stdin = open("day02_04.txt","r")
data04 = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    data04[i] = list(map(int,input().split()))
# print(data04)

# 오름차순 데이터 만들기
data = []
value = 0
while value <100:
    value = None
    for y in range(5):
        for x in range(5):
            if value == None or value > data04[y][x]: # 최소값 찾기
                value = data04[y][x]
    if value < 100:
        data += [value]
print(data)


# dy = [0,1,0,-1]
# dx = [1,0,-1,0]
# dir = 0
#
# location = data04[y+dy[dir]][x+dx[dir]]
#
# new_y = y + dy[dir]
# new_x = x + dx[dir]
# if IsSafe(new_y, new_x):
#     sum += Mycalc(data01[y][x], data01[new_y][new_x])


# for y in range(5):
#     for x in range(5):
#         for dir in range(4):  # 4=len(dy)
#                     newY = y + dy[dir]
#                     newX = x + dx[dir]
#                     if IsSafe(newY, newX):
#                         sum += Mycalc(data01[y][x], data01[newY][newX])