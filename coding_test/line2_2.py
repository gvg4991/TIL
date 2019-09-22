# k번째 순열 찾기
# # 예를 들어 숫자 1, 2, 3으로 만들 수 있는 순열 중 오름차순으로 정렬 했을 때 3번째 순열은 213이다.
# #
# # 조합된 순열	순서(오름차순)
# # 123	1
# # 132	2
# # 213	3
# # 231	4
# # 312	5
# # 321	6
# # 제한 사항
# # 순열을 조합할 때 주어진 숫자를 모두 한번씩 사용해야 한다
# # 입력 형식
# # 첫 번째 행에 공백(space)을 구분자로 숫자가 주어진다
# # 각 숫자는 한 자리 숫자로 주어진다 (0과 같거나 크고, 10보다 작은 숫자)
# # 같은 숫자가 중복되어 나타나지 않는다
# # 두 번째 행에 찾으려는 수열의 순서(k)가 주어진다
# # k는 조합된 순열의 개수보다 크거나 작지 않다
# # 출력 형식
# # 조합된 순열을 오름차순으로 정렬 했을 때 k번째 순열
# # 맨 앞자리가 0인 경우는 0을 그대로 유지한다
# # 입출력 예제
# # 입력
# #
# # 1 0 2
# # 5
# # 출력
# #
# # 201

import sys
sys.stdin = open('input.txt')

import itertools

datas = list(map(int,input().split()))
n = len(datas)
target = int(input())
ans = []

perm = list(itertools.permutations(datas))
# print(perm)

for p in perm:
    result = 0
    for jrs in range(len(p)):
        result += p[jrs]*(10**(n-1-jrs))
    ans.append(result)

ans = sorted(ans)
print(ans[target-1])



# def getsome(depth):
#     global ans, target
#     if depth == n:
#         target = ''
#         for i in result:
#             target += str(i)
#         target = int(target)
#         ans.append(target)
#         return
#     for i in range(n):
#         if not visited[i]:
#             visited[i] = True
#             result[depth] = datas[i]
#             getsome(depth+1)
#             visited[i] = False
#
# datas = list(map(int,input().split()))
# n = len(datas)
# idx = int(input())
# visited = [False]*n
# result = [0]*n
# ans = [0]*n
#
# getsome(0)
# # print(ans[idx])
# print(ans)
