def combO(i):
    global m,n, result
    result.append(i)
    if len(result) == n: #1
        return
    if i < m:
        new_i = i + 1 #2
        combO(new_i)
        ans.append(result)
        result = []
        combX(new_i)
        ans.append(result)
        result = []
    return

def combX(i):
    global m,n, result
    if len(result) == n:
        return
    else:
        if i < m:
            new_i = i + 1
            combO(new_i)
            ans.append(result)
            result = []
            combX(new_i)
            ans.append(result)
            result = []
        return

result = []
ans = []
o = []
x = []
m,n = 3,2

# for i in range(1,m-n+2):
#     result = []
#     combO(i)
#     print(o)
#     print(x)
#     # combX(i)
#     # print(o)
#     # print(x)

combO(1)
# print(result)
print(ans)
combX(1)
# print(result)
print(ans)