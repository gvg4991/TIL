import sys
sys.stdin = open("day04_01.txt","r")

mymap = [[0]*8 for i in range(8)]
visited = [0]*8
stack = [0] * 10
top = -1

# 백트래킹
def push(x):
    global top
    top += 1
    stack[top] = x

def pop():
    global top
    if top == -1:
        return 0
    x = stack[top]
    top -= 1
    return x

def findnext(here):
    for next in range(8):
        if mymap[here][next] and not visited[next]:
            return next

def dfs(here):
    global top
    print(here)
    visited[here] = True
    while here: #here가 있는 동안
        next = findnext(here)
        if next:
            push(here)
        while next:
            here = next
            print(here)
            visited[here] = True
            next = findnext(here)
            push(here)
        here = pop()

