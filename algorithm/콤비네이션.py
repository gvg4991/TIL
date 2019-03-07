# def combO(i):
#     global m,n, result
#     result.append(i)
#     if len(result) == n: #1
#         ans.append(result)
#         return
#     if i < m:
#         new_i = i + 1 #2
#         combO(new_i)
#         # ans.append(result)
#         result = []
#         combX(new_i)
#         # ans.append(result)
#         result = []
#     return
#
# def combX(i):
#     global m,n, result
#     if len(result) == n:
#         ans.append(result)
#         return
#     else:
#         if i < m:
#             new_i = i + 1
#             combO(new_i)
#             # ans.append(result)
#             result = []
#             combX(new_i)
#             # ans.append(result)
#             result = []
#         return
#
# result = []
# ans = []
# o = []
# x = []
# m,n = 5,3
#
# # for i in range(1,m-n+2):
# #     result = []
# #     combO(i)
# #     print(o)
# #     print(x)
# #     combX(i)
# #     print(o)
# #     print(x)
#
# combO(1)
# # print(result)
# print(ans)
# ans=[]
# combX(1)
# # print(result)
# print(ans)


visited = [0] * 6
def Get(k,s):
    if len(s)==3:
        print(s)
        return
    if k > 5:
        return
    visited[k] = 1
    Get(k+1,s+str(k))
    visited[k] = 0
    Get(k+1,s)
Get(1,'')