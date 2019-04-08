# 5C3
# 12,13,23
# 5H3
# 11,12,13,22,23,33

# nn = 5
# rr = 3
# IsUsed= [0]*(rr+1)
# def GetSome(n , r):
#     if r > rr :
#         for i in range(1, rr+1):
#               print(IsUsed[i], end=' ')
#         print()
#         return
#     if n > nn : return
#     IsUsed[r] = n
#     GetSome(n+1, r+1)
#     GetSome(n+1, r)
#
# GetSome(1,1)
#



cnt = 0
def combination(n, r, i, d):

    global cnt
    if r == 0:
        print(d)
        cnt+=1
        return
    if i==n:
        return

    combination(n, r-1, i, d+[data[i]]) #들어갔을때 (똑같은 수 한번 더 들어갈 수 있음)
    combination(n, r, i+1, d) #안들어갔을때 다음숫자를 봄

nn=5
rr=3
data = [1,2,3,4,5]
combination(nn, rr, 0, [])
print(cnt)
