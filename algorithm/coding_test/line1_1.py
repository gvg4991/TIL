import sys
sys.stdin = open("input.txt")


# n = int(input())
# result = []
# if n == 1:
#     ans = 0
# else:
#     for w in range(1,n+1):
#         for h in range(1,n+1):
#             if w*h == n:
#                 result.append(abs(w-h))
#                 ans = min(result)
# print(ans)


n = int(input())
result = []
if n == 1:
    ans = 0
else:
    for w in range(1,int(n**(1/2))+1):
        for h in range(int(n**(1/2)),n+1):
            if w*h == n:
                result += abs(w-h)
ans = min(result)
print(ans)