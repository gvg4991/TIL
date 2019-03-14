# 문제
# 어떤 N개의 수가 주어져 있다. 그런데 중간에 수의 변경이 빈번히 일어나고 그 중간에 어떤 부분의 합을 구하려 한다. 만약에 1,2,3,4,5 라는 수가 있고, 3번째 수를 6으로 바꾸고 2번째부터 5번째까지 합을 구하라고 한다면 17을 출력하면 되는 것이다. 그리고 그 상태에서 다섯 번째 수를 2로 바꾸고 3번째부터 5번째까지 합을 구하라고 한다면 12가 될 것이다.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)과 M(1 ≤ M ≤ 10,000), K(1 ≤ K ≤ 10,000) 가 주어진다. M은 수의 변경이 일어나는 회수이고, K는 구간의 합을 구하는 회수이다. 그리고 둘째 줄부터 N+1번째 줄까지 N개의 수가 주어진다. 그리고 N+2번째 줄부터 N+M+K+1번째 줄까지 세 개의 정수 a, b, c가 주어지는데, a가 1인 경우 b번째 수를 c로 바꾸고 a가 2인 경우에는 b번째 수부터 c번째 수까지의 합을 구하여 출력하면 된다.
#
# a가 1인 경우 c는 long long 범위를 넘지 않는다.
#
# 출력
# 첫째 줄부터 K줄에 걸쳐 구한 구간의 합을 출력한다. 단, 정답은 long long 범위를 넘지 않는다.

import sys
sys.stdin = open("input.txt")


n,m,k = map(int,input().split())
begin = 1
while begin < n:
    begin *= 2
datas = [0]*(begin*2)
for i in range(n):
    datas[begin+i] = int(input())
# print(datas)
for parent in range(begin-1,-1,-1):
    datas[parent] = datas[parent*2] + datas[parent*2+1] #부모의 값은 자식의 두수 합

for i in range(m+k):
    case,start,end = map(int,input().split())
    if case == 1:
        change = begin + start - 1
        datas[change] = end
        change = change//2
        while change:
            datas[change] = datas[change * 2] + datas[change * 2 + 1]
            change = change//2
    else:
        start = start + begin - 1  # 8
        end = end + begin - 1  # 11
        sum = 0
        while start < end:
            if start & 1:  # 홀수이면 (start%2==1)
                sum += datas[start]  # 값을 sum에 더해주고
                start += 1
            if end % 2 == 0:
                sum += datas[end]
                end -= 1
            start >>= 1  # 부모한테 찾아감
            end >>= 1
        if start == end:
            sum += datas[start]
            print(sum)

