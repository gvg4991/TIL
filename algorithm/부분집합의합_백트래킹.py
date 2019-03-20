import sys
sys.stdin = open("input.txt")


# def getsome(depth,k):
#     if depth == k:
#         ans.append(result)
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             result.append(datas[i])
#             getsome(depth+1,k)
#             visited[i] = False



def getsome(depth,r):
    if depth == r:
        if sum(result) == 0:
            print(result)
            ans.append(result)

        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            result[depth] = datas[i]
            getsome(depth+1,r)
            visited[i] = False

datas = [-1,3,-9,6,7,-6,1,5,4,-2]
n = len(datas)
visited = [False]*n
ans = []

for r in range(1,n):
    result = [0]*(r+1)
    getsome(0,r)
# print(ans)
#     result = []
# print(ans)