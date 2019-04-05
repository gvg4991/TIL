# 선표는 게임을 통해 사칙 연산을 공부하고 있다.
# N개의 숫자가 적혀 있는 게임 판이 있고, +, -, x, / 의 연산자 카드를 숫자 사이에 끼워 넣어 다양한 결과 값을 구해보기로 했다.
# 수식을 계산할 때 연산자의 우선 순위는 고려하지 않고 왼쪽에서 오른쪽으로 차례대로 계산한다.
# 예를 들어 1, 2, 3 이 적힌 게임 판에 +와 x를 넣어 1 + 2 * 3을 만들면 1 + 2를 먼저 계산하고 그 뒤에 * 를 계산한다.
# 즉 1+2*3의 결과는 9이다.
# 주어진 연산자 카드를 사용하여 수식을 계산했을 때 그 결과가 최대가 되는 수식과 최소가 되는 수식을 찾고, 두 값의 차이를 출력하시오.
# [예시]
# [Figure 1] 과 같이 [3,5,3,7,9]가 적힌 숫자판과 [‘+’ 2개, ‘-‘ 1개, ‘/’ 1개]의 연산자 카드가 주어진 경우를 생각해보자.
# [Figure 1]
# 아래 [Table 1]은 만들 수 있는 수식과 계산 결과이다.
# 수식
# 수식의 계산 결과
# 3 + 5 + 3 - 7 / 9
# 0
# 3 + 5 + 3 / 7 - 9
# -8
# 3 + 5 - 3 + 7 / 9
# 1
# 3 + 5 - 3 / 7 + 9
# 9
# 3 + 5 / 3 + 7 - 9
# 0
# 3 + 5 / 3 - 7 + 9
# 4
# 3 / 5 + 3 + 7 - 9
# 1
# 3 / 5 + 3 - 7 + 9
# 5
# 3 / 5 - 3 + 7 + 9
# 13
# 3 - 5 + 3 + 7 / 9
# 0
# 3 - 5 + 3 / 7 + 9
# 9
# 3 - 5 / 3 + 7 + 9
# 16
# 이 경우 최댓값은 3 - 5 / 3 + 7 + 9 = 16, 최솟값은 3 + 5 + 3 / 7 - 9 = -8 이다.
# 즉 결과는 최댓값과 최솟값의 차이 ( 16 - ( -8 ) ) 로 24 가 답이 된다.
# [제약사항]
# 1. 시간 제한 : 최대 50 개 테스트 케이스를 모두 통과하는 데 C / C++ / Java 모두 3 초
# 2. 게임 판에 적힌 숫자의 개수 N 은 3 이상 12 이하의 정수이다. ( 3 ≤ N ≤ 12 )
# 3. 연산자 카드 개수의 총 합은 항상 N - 1 이다.
# 4. 게임 판에 적힌 숫자는 1 이상 9 이하의 정수이다.
# 5. 수식을 완성할 때 각 연산자 카드를 모두 사용해야 한다..
# 6. 숫자와 숫자 사이에는 연산자가 1 개만 들어가야 한다.
# 7. 완성된 수식을 계산할 때 연산자의 우선 순위는 고려하지 않고, 왼쪽에서 오른쪽으로 차례대로 계산한다.
# 8. 나눗셈을 계산 할 때 소수점 이하는 버린다.
# 9. 입력으로 주어지는 숫자의 순서는 변경할 수 없다.
# 10. 연산 중의 값은 -100,000,000 이상 100,000,000 이하임이 보장된다.
# [입력]
# 입력의 맨 첫 줄에는 총 테스트 케이스의 개수 T 가 주어지고,
# 그 다음 줄부터 T 개의 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 숫자의 개수 N 이 주어진다.
# 다음 줄에는 '+', '-', '*', '/' 순서대로 연산자 카드의 개수가 공백을 사이에 두고 주어진다.
# 다음 줄에는 수식에 들어가는 N 개의 숫자가 순서대로 공백을 사이에 두고 주어진다.
# [출력]
# 테스트 케이스 개수만큼 T 개의 줄에 각각의 테스트 케이스에 대한 답을 출력한다.
# 각 줄은 "#t" 로 시작하고 공백을 하나 둔 다음 정답을 출력한다. ( t 는 1 부터 시작하는 테스트 케이스의 번호이다. )
# 정답은 연산자 카드를 사용하여 만들 수 있는 수식으로 얻은 결과값 중 최댓값과 최솟값의 차이이다.

import sys
sys.stdin = open('input.txt')
import collections


def getsome(depth):
    if depth == cnt-1:
        if not calculation in calculator:
            calculator.append(calculation[:])
        return
    for i in range(cnt-1):
        if not used[i]:
            used[i] = 1
            calculation[depth] = sem[i]
            getsome(depth+1)
            used[i] = 0


for tc in range(int(input())):
    cnt = int(input())
    calc = list(map(int,input().split()))
    sem = []
    # sem = [0]*(cnt-1)
    for c in range(4):
        if c == 0:
            sem.extend(['+']*calc[c])
        elif c == 1:
            sem.extend(['-']*calc[c])
        elif c == 2:
            sem.extend(['*']*calc[c])
        elif c == 3:
            sem.extend(['/']*calc[c])
    # print(sem)
    used = [0]*(cnt-1)
    calculation = ['']*(cnt-1)
    calculator = []
    num = list(map(int,input().split()))
    result = 0
    ans = []

    getsome(0)
    # print(calculator)
    for c in calculator:
        target = collections.deque(num[:])
        l = target.popleft()
        for solve in c:
            r = target.popleft()
            if solve == '+':
                result = l+r
            elif solve == '-':
                result = l-r
            elif solve == '*':
                result = l*r
            elif solve == '/':
                result = l//r
                # if l//r < 0:
                #     result = l//r+1
                # else:
                #     result = l//r
            l = result
        ans.append(result)
    print('#{} {}'.format(tc+1,max(ans)-min(ans)))











# def getsome(depth):
#     global result, l
#     if depth == cnt-1:
#         if not l in ans:
#             ans.append(l)
#         return
#     for i in range(cnt-1):
#         if not used[i]:
#             used[i] = 1
#             # calculation[depth] = sem[i]
#             if sem[i] == '+':
#                 result = l+num[i+1]
#             elif sem[i] == '-':
#                 result = l-num[i+1]
#             elif sem[i] == '*':
#                 result = l*num[i+1]
#             elif sem[i] == '/':
#                 result = l//num[i+1]
#             l = result
#             getsome(depth+1)
#             used[i] = 0
#
#
# for tc in range(int(input())):
#     cnt = int(input())
#     calc = list(map(int,input().split()))
#     sem = []
#     for c in range(4):
#         if c == 0:
#             sem.extend(['+']*calc[c])
#         elif c == 1:
#             sem.extend(['-']*calc[c])
#         elif c == 2:
#             sem.extend(['*']*calc[c])
#         elif c == 3:
#             sem.extend(['/']*calc[c])
#     used = [0]*(cnt-1)
#     num = list(map(int,input().split()))
#     l = num[0]
#     result = 0
#     ans = []
#
#     getsome(0)
#     print('#{} {}'.format(tc+1,max(ans)-min(ans)))














# def getsome(depth):
#     if depth == r:
#         print(result)
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             result[depth] = datas[i]
#             getsome(depth+1)
#             visited[i] = False
#
# n = 5
# r = 3
# datas = [1,2,3,4,5]
# visited = [False]*n
# result = [0]*r
#
# getsome(0)




