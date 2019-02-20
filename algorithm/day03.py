import sys
sys.stdin = open("day03_01.txt","r")

# 스택
stack = [0]*10 #시험시 10000
top = -1 #탑 고정값

# 데이터 넣기(스택에 쌓기)
for i in range(1,4):
    # stack.append(i) [3,2,1,0,0,0,0,0,0,0,0,0,0]
    top += 1
    stack[top] = i #[3,2,1,0,0,0,0,0,0,0]

# 위에서부터 출력하기
while top != -1:
    print(stack[top])
    top -= 1

# while stack:
#     print(stack.pop())


#----------------------------------------------------------------------------------------------------
# 괄호 검사

sys.stdin = open("day03_02.txt","r")

# stack = [0] * 100
# top = -1
#
# data = list(map(str,input()))
#
# for i in range(len(data)):
#     if data[i] == '(' or data[i] == '{' or data[i] == '[' or data[i] == '<':
#         top += 1
#         stack[top] = data[i]
#
#     elif data[i] == ')':
#         item = stack.pop(top)
#         top -= 1
#         if item != '(':
#             print('조건3 error')
#             break
#     elif data[i] == '}':
#         item = stack.pop(top)
#         top -= 1
#         if item != '{':
#             print('조건3 error')
#             break
#     elif data[i] == ']':
#         item = stack.pop(top)
#         top -= 1
#         if item != '[':
#             print('조건3 error')
#             break
#     elif data[i] == '>':
#         item = stack.pop(top)
#         top -= 1
#         if item != '<':
#             print('조건3 error')
#             break
#
# if top != -1:
#     print('조건1 error')
# else:
#     print('YO!')


# 강사님
stack = [0]*100
top = -1

info = [0] *128
data = list(map(str,input()))

info[ord(')')] = '('
info[ord('}')] = '{'
info[ord(']')] = '['
info[ord('>')] = '<'

howmany = len(data)
for i in range(howmany):
    if data[i] == '(' or data[i] == '{' or data[i] == '[' or data[i] == '<':
        top += 1
        stack[top] = data[i]
    elif info[ord(data[i])] == stack[top]:
        item = stack.pop(top)
        top -= 1
    else:
        print('조건3 error')
        break

if top != -1:
    print('조건1 error')
else:
    print('YO!')



#----------------------------------------------------------------------------------------------------
# 하노이 탑

def hanoi(n, ffrom, to, spare):
    if n > 0:
        hanoi(n-1, ffrom, spare, to)
        hanoi(n-1, spare, to, ffrom)

    print('원반의 갯수 :')
    n = int(input())
    hanoi(n, 'from', 'to', 'spare')



#----------------------------------------------------------------------------------------------------
# 계단 오르기

sys.stdin = open("day03_01.txt","r")
ans = 0

def getsome(here):
    global ans
    if here == howmany: # 입력 위치에 도착했을 경우
        ans += 1
        return
    if here > howmany: # 입력 위치를 뛰어넘었을 경우
        return
    getsome(here+1) # 1칸씩 올라간 입력값(1) -> 1칸 후 올라간 입력값(2) and 2칸 후 올라간 입력값(3)
    getsome(here+2) # 2칸씩 올라간 입력값(2) -> 1칸 후 올라간 입력값(3) and 2칸 후 올라간 입력값(4)

# howmany = int(input()) # 도착 위치 입력

start = 0  #0번째 칸부터 시작하겠다!
getsome(start) # 시작값부터해서 입력 위치까지 몇가지 방법이 있는지 카운트
print(f'{ans}')


#----------------------------------------------------------------------------------------------------
# 그래프

sys.stdin = open("day03_04.txt","r")

mymap = [[0]*8 for i in range(8)]
# degree = [0]*8
visited = [0]*8

def dfs(here):
    print(here)
    visited[here] = True #들린곳은 True 바꿔줌
    for next in range(8):
        if mymap[here][next] and not visited[next]:
        # 시작위치에서 갈 수 있는 벨류이고 방문한 적이 없을 경우
            dfs(next)

data = list(map(int,input().split()))
for ind in range(int(len(data)/2)):
    start = data[ind*2]
    stop = data[ind*2+1]
    mymap[start][stop] = 1
    mymap[stop][start] = 1

# for i in data:
#     degree[i] += 1

print(mymap)
dfs(1)


