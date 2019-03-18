import sys
sys.stdin = open("input.txt")

case = int(input())
datas = [0]*case
for n in range(case):
    datas[n] = int(input())

target = 0
result = 0
ans = []
for i in range(len(datas)-1):
    if datas[i] > max(datas[i+1:]):
        target = 0
        ans.append(result)
        result = 0
        pass
    elif datas[i] >= target:
        target = datas[i]
        ans.append(result)
        result = 0
    else:
        result += 1

ans.append(result)
print(max(ans)+1)
