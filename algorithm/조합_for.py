import sys
sys.stdin = open("input.txt")



#조합
n = 5
r = 3
datas = [1,2,3,4,5]
result = []
for a in range(n-2):
    for b in range(a+1,n-1):
        for c in range(b+1,n):
            result.append([datas[a],datas[b],datas[c]])
print(result)



# # 중복조합
# n = 5
# r = 3
# datas = [1,2,3,4,5]
# result = []
# for a in range(n):
#     for b in range(a,n):
#         for c in range(b,n):
#             result.append([datas[a],datas[b],datas[c]])
# print(result)