import sys
sys.stdin = open("input.txt")


n,m = map(int,input().split())

result = 0
if n == 1 or m == 1:
    result = 1
elif n == 2 and m < 3:
    result = 1
elif n == 2 and m < 5:
    result = 2
elif n == 2 and m < 7:
    result = 3
elif n == 2 and m >= 7:
    result = 4
elif n >= 3 and m < 3:
    result = 2
elif n >= 3 and m < 4:
    result = 3
elif n >= 3 and m <= 6:
    result = 4
elif n >= 3 and m > 6:
    result = m - 5 + 3

print(result)