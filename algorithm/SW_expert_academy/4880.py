# 사다리 게임이 지겨워진 알고리즘 반 학생들이 새로운 게임을 만들었다. 가위바위보가 그려진 카드를 이용해 토너먼트로 한 명을 뽑는 것이다. 게임 룰은 다음과 같다.
# 1번부터 N번까지 N명의 학생이 N장의 카드를 나눠 갖는다. 전체를 두 개의 그룹으로 나누고, 그룹의 승자끼리 카드를 비교해서 이긴 사람이 최종 승자가 된다. 
# 그룹의 승자는 그룹 내부를 다시 두 그룹으로 나눠 뽑는데, i번부터 j번까지 속한 그룹은 파이썬 연산으로 다음처럼 두개로 나눈다.
# 두 그룹이 각각 1명이 되면 양 쪽의 카드를 비교해 승자를 가리고, 다시 더 큰 그룹의 승자를 뽑는 방식이다. 
# 다음은 4명이 카드를 비교하는 경우로, 숫자 1은 가위, 2는 바위, 3은 보를 나타낸다. 만약 같은 카드인 경우 편의상 번호가 작은 쪽을 승자로 하고, 처음 선택한 카드는 바꾸지 않는다.
# N명이 학생들이 카드를 골랐을 때 1등을 찾는 프로그램을 만드시오.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 별로 인원수 N과 다음 줄에 N명이 고른 카드가 번호순으로 주어진다. 4≤N≤100
# 카드의 숫자는 각각 1은 가위, 2는 바위, 3은 보를 나타낸다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 1등의 번호를 출력한다.


import sys
sys.stdin = open("input.txt","r")

def team(s,e):
    mid = (s+e)//2
    if (e-s+1)//2 == 0:
        return mid
    left = team(s,mid)
    right = team(mid+1,e)
    battle(left,right)
    return result

def battle(l,r):
    global result
    if datas[l] == 1:
        if datas[r] == 1 or datas[r] == 3:
            result = l
        else:
            result = r
    elif datas[l] == 2:
        if datas[r] == 2 or datas[r] == 1:
            result = l
        else:
            result = r
    elif datas[l] == 3:
        if datas[r] == 3 or datas[r] == 2:
            result = l
        else:
            result = r
    return result


test = int(input())
for tc in range(test):
    case = int(input())
    datas = list(map(int,input().split()))

    team(0, case-1)
    print('#{} {}'.format(tc+1, result+1))











# member = []
# result = None
#
# def rsp(i,j):
#     global result
#     if datas[i] == 1:
#         if datas[j] == 1 or datas[j] == 3:
#             result = i
#         else:
#             result = j
#     elif datas[i] == 2:
#         if datas[j] == 2 or datas[j] == 1:
#             result = i
#         else:
#             result = j
#     elif datas[i] == 3:
#         if datas[j] == 3 or datas[j] == 2:
#             result = i
#         else:
#             result = j
#     return result
#
# def team(i,j):
#     global member, result
#     if (i+j)//2 >= 2:
#         member = (i+j)//2
#         team(i,member) #result
#         result_i = result #result
#         team(member+1, j) #result
#         result_j = result #result
#
#         rsp(result_i,result_j) #result
#         # return
#
#     elif (i+j)//2 == 1:
#         if (i+j)%2 > 0: #[0,1],[2,3]
#             member = (i+j)//2
#             rsp(i,member) #result
#             result_i = result
#             rsp(member+1, j) #result
#             result_j = result
#
#             rsp(result_i,result_j) #result
#             return
#
#         elif (i+j)%2 == 0: #[0,1],[2]
#             member = (i+j)//2
#             rsp(i,member)
#             result_i = result
#             # team(result_i, j)
#             # result_j = result
#
#             rsp(result_i,j)
#             return
#
#     # else:
#     #     rsp(i,j) #result = i
#     #     return
#
#
# test = int(input())
# datas = []
# for tc in range(test):
#     case = int(input())
#     datas = list(map(int,input().split()))
#
#     team(0,case-1)
#     print('#{} {}'.format(tc+1,result+1))












# member = []
# result = None

# def rsp(i,j):
#     global result
#     if datas[i] == 1:
#         if datas[j] == 1 or datas[j] == 3:
#             result = i
#         else:
#             result = j
#     elif datas[i] == 2:
#         if datas[j] == 2 or datas[j] == 1:
#             result = i
#         else:
#             result = j
#     else:
#         if datas[j] == 3 or datas[j] == 2:
#             result = i
#         else:
#             result = j
#     return

# def team(i,j):
#     global member, result
#     member = int((i+j)//2)
#     if member // 2 >= 2:
#         team(i,member)
#         result_i = result
#         team(member+1, j)
#         result_j = result

#         rsp(result_i,result_j)
#         return

#     else:
#         rsp(i,j) #result = i
#         return


# test = int(input())
# datas = []
# for tc in range(test):
#     case = int(input())
#     datas = list(map(int,input().split()))

#     team(0,case-1)
#     print(f'#{tc+1} {result}')