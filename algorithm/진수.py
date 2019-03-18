import sys
sys.stdin = open("input.txt")



sixteen = input()
data = int(sixteen,16)
target = data

result = [0]*4*len(sixteen)
i = 0
while target >= 1:
    i += 1
    result[-i] = target%2
    target = target // 2
# print(result)

ans = []
for start in range(0,len(result),7):
    if len(result)-start >= 7:
        two = ''.join(map(str,result[start:start+7]))
        ans.append(int(two,2))
    else:
        two = ''.join(map(str,result[start:]))
        ans.append(int(two,2))
print(ans)

















# result = []
# for i in sixteen:
#     if i.isdigit() and int(i) <= 1:
#         result.append(int(i))
#     elif ord(i) >= 65 and ord(i) <= 70:
#         i = int(chr(ord(i) - 16)) + 10
#         while int(i) > 1:
#             result.append(int(i) % 2)
#             i = int(i) // 2
#     else:
#         while int(i) > 1:
#             result.append(int(i) % 2)
#             i = int(i) // 2
#
# print(result)



# for start in range(0,len(sixteen)-7,7):
#     data = sixteen[start:start+7]
