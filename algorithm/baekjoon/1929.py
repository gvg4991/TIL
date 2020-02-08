# 문제
# M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
#
# 출력
# 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.

import sys
sys.stdin = open("input.txt")

a,b = map(int,input().split())
idx = 0
l = []
result = []
datas = [0]*(b-a+1)

for data in range(a,b+1):
    datas[idx] = data
    idx += 1
# print(datas)

for i in range(2,11): #최대값 내 소수 아닌 값
    t = i
    t += i
    while t <= b:
        l.append(t)
        t += i
l = set(l)
# print(l)

for target in l:
    if target in l:
        datas.remove(target)
# print(*datas)
for yo in datas:
    print(yo)