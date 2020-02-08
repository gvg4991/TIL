# 영준이는 학생들의 시험을 위해 N개의 문제를 만들었다.
# 각 문제의 배점은 문제마다 다를 수 있고, 틀리면 0점 맞으면 배점만큼의 점수를 받게 된다.
# 학생들이 받을 수 있는 점수로 가능한 경우의 수는 몇 가지가 있을까?
# 예를 들어, 첫 번쨰 Testcase의 경우, 총 문제의 개수는 3개이며 각각의 배점은 2, 3, 5점이다
# 가능한 시험 점수의 경우의 수를 살펴보면 0, 2, 3, 5, 7, 8, 10의 7가지가 있다.
# 두 번째 Testcase의 경우, 총 문제의 개수는 10개이며 각각의 배점은 모두 1점이다.
# 가능한 시험점수의 경우의 수를 살펴보면 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10으로 모두 11가지이다.
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 100)이 주어진다.
# 두 번째 줄에는 각 문제의 배점을 의미하는 N개의 자연수가 공백으로 구분되어 주어진다. 배점은 1이상 100이하의 자연수이다.
# [출력]
# 각 테스트 케이스마다 학생들이 받을 수 있는 점수의 경우의 수를 출력한다.


import sys
sys.stdin = open('input.txt')
















# import itertools
#
#
# for tc in range(int(input())):
#     n = int(input())
#     datas = list(map(int,input().split()))
#     # print(datas)
#
#     result = []
#     for ni in range(1,n+1):
#         result.append(list(set(itertools.combinations(datas,ni))))
#     # print(result)
#
#     ans = []
#     for idx in range(n):
#         for r in result[idx]:
#             ans.append(sum(r))
#     # print(ans)
#     ans=list(set(ans))
#     print('#{} {}'.format(tc+1,len(ans)+1))













# import itertools
#
#
# for tc in range(int(input())):
#     n = int(input())
#     datas = [0]*n + list(map(int,input().split()))
#     # print(datas)
#
#     result = []
#     result.append(list(set(itertools.combinations(datas,n))))
#     # print(result)
#     ans = []
#     for r in result[0]:
#         ans.append(sum(r))
#     # print(ans)
#     ans=list(set(ans))
#     print('#{} {}'.format(tc+1,len(ans)))










# def combination(n, r, i, d):
#     if r == 0:
#         ans.append(sum(d))
#         return
#     if i == n:
#         return
#
#     combination(n, r-1, i+1, d+[datas[i]]) #들어갔을때 (똑같은 수 한번 더 들어갈 수 있음)
#     combination(n, r, i+1, d) #안들어갔을때 다음숫자를 봄
#
# for tc in range(int(input())):
#     n = int(input())
#     datas = [0] * n + list(map(int, input().split()))
#     ans=[]
#
#     result = []
#     combination(len(datas), n, 0, result)
#     # print(ans)
#     ans = list(set(ans))
#     print('#{} {}'.format(tc+1,len(ans)))










# def combination(n, r, i, d):
#     if r == 0:
#         ans.append(sum(d))
#         return
#     if i == n:
#         return
#
#     combination(n, r-1, i+1, d+[datas[i]]) #들어갔을때 (똑같은 수 한번 더 들어갈 수 있음)
#     combination(n, r, i+1, d) #안들어갔을때 다음숫자를 봄
#
# for tc in range(int(input())):
#     n = int(input())
#     datas = list(map(int, input().split()))
#     ans=[]
#
#     result = []
#     for ni in range(1,n+1):
#         combination(len(datas), ni, 0, result)
#     # print(ans)
#     ans = list(set(ans))
#     print('#{} {}'.format(tc+1,len(ans)+1))
