import sys
sys.stdin = open("input.txt")


datas = list(input())
eng = []
num = []
for d in datas:
    if d.isdigit():
        num.append(d)
    else:
        eng.append(d)

result = []
ei = 0
ni = 0

try:
    while ei<len(eng) and ni<len(num):
        now = eng[ei]
        if ei+1 < len(eng):
            next = eng[ei+1]
        if now.isupper():
            result.append(now)
        if next.islower():
            result.append(next)
            ei += 2
        else:
            ei += 1

        first = num[ni]
        if ni + 1 < len(num):
            second = num[ni+1]
        if first == '1':
            if second == '0':
                result.append(first)
                result.append(second)
                ni += 2
            else:
                ni += 1
        else:
            result.append(first)
            ni += 1

    print(''.join(result))

except:
    print('error')