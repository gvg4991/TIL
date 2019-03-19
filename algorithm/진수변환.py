import sys
sys.stdin = open("input.txt")


data = int(input())
value = data
result = []

while value >= 6:
    result += [value%7]
    value = value//7
result.append(value)

ans = result[::-1]
ans = ' '.join(map(str,ans))
print(ans)

