import sys
sys.stdin = open("input.txt")


pattern = {0:'001101', 1:'010011', 2:'111011', 3:'110001', 4:'100011', 5:'110111', 6:'001011', 7:'111101', 8:'011001', 9:'101111'}

sixteen = input()
result = [0]*4*len(sixteen)
# print(result)
i = 0

ten = int(sixteen,16)
# print(ten)
two = list(bin(ten))
# print(two)

for value in two[:1:-1]:
    i += 1
    result[-i] = int(value)
pw = ''.join(map(str,result))
# print(pw)

ans = []
for key,val in pattern.items():
    if val in pw:
        pw = pw.replace(val,'-')
        ans.append(key)
# print(pw)
print(ans)