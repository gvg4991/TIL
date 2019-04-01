# import sys
# sys.stdin = open("input.txt")


# 중복순열
def getsome(depth):
    if depth == r:
        print(result)
        return
    for i in range(n):
        result[depth] = datas[i]
        getsome(depth+1)

n = 5
r = 3
datas = [1,2,3,4,5]
result = [0]*r

getsome(0)