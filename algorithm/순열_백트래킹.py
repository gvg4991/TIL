import sys
sys.stdin = open("input.txt")


# 순열
def getsome(depth):
    if depth == r:
        print(result)
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result[depth] = datas[i]
            getsome(depth+1)
            visited[i] = False

n = 5
r = 3
datas = [1,2,3,4,5]
visited = [False]*n
result = [0]*r

getsome(0)