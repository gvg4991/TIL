# 상원이의 생일 파티가 곧 열린다!
# 그렇기에 상원이는 반 친구들에게 생일 파티 초대장을 주려고 한다.
# 그러나 파티가 어색하게 되는 것을 원치 않는 상원이는 모든 친구들에게 초대장을 줄 생각이 없다.
# 같은 반에 있지만, 서로 친한 친구가 아닐 수도 있기 때문이다.
# 상원이는 우선 자신과 친한 친구들에게는 모두 초대장을 주기로 했다.
# 여기에 더해서 친한 친구의 친한 친구인 경우에도 초대장을 주기로 했다.
# 총 몇 명의 친구들에게 초대장을 주어야 하는지 구하는 프로그램을 작성하라.
# 상원이의 반에는 N명이 있으며, 각 학생들은 1번에서 N번까지의 번호가 붙어 있다.
# 여기서 1번 학생이 상원이다.
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 두 정수 N, M ( 2 ≤ N ≤ 500, 1 ≤ M ≤ 104 ) 이 공백으로 구분되어 주어진다.
# M은 친한 친구 관계의 수 이다.
# 다음 M개의 줄의 각 줄에는 두 정수 a, b (1 ≤ a ＜ b ≤ N) 이 주어진다.
# 이는 a번 학생과 b번 학생이 서로 친한 친구 관계에 있다는 의미이다.
# [출력]
# 각 테스트 케이스마다 #T를 출력하고 한 칸을 띄운 후, 각 테스트 케이스마다 상원이의 생일 파티 초대장을 받는 친구의 수를 출력한다.
# *상원이의 친구가 없을 수도 있다는 점에 유의해야 한다. 그리고 상원이는 초대장을 받는 사람에 속하지 않는다.


import sys
sys.stdin = open('input.txt')



# def find(x):
#     global cnt
#     if x != friend[x]: #자신이랑 엄마가 같으면 즉, 자신이 엄마면
#         return find(friend[x])
#     else:
#         return friend[x]
#
# def union(x,y):
#     x = find(x) #x엄마 찾기
#     y = find(y)
#     if x!=y:
#         friend[y]=x #y의 엄마가 x가 됨


# for tc in range(int(input())):
#     n,m = map(int,input().split())
#
#     friend = [0]*(n+1)
#     for make in range(1,n+1):
#         friend[make] = make
#
#     cnt = 0
#     for bf in range(m):
#         fri1,fri2 = map(int,input().split())
#         friend[fri2] = fri1
#         # union(fri1,fri2)
#     # print(friend)
#
#     invite = 0
#     for d in range(2,n+1):
#         if friend[d] == 1:
#             invite += 1
#         elif friend[friend[d]] == 1:
#             invite += 1
#     print(invite)





# # 시간터짐
# result = [1]
# friend = []
# cnt = 0
# for tc in range(int(input())):
#     n,m = map(int,input().split())
#     friend = [(0,0)]*m
#     for bf in range(m):
#         fri = list(map(int,input().split()))
#         friend[bf] = fri
#         if 1 in fri:
#             result.extend(fri)
#     result = list(set(result))
#     # print(result)
#     # print(friend)
#     for i in result:
#         for fri in friend:
#             if i in fri:
#                 cnt += 1
#                 friend.remove(fri)
#     print('#{} {}'.format(tc+1,cnt))




#bfs 코딩
for tc in range(int(input())):
    n,m = map(int, input().split())
    friend = [[0]*(n+1) for _ in range(n+1)]
    invite = [0]*(n+1)
    best = [0]*(n+1)

    for relation in range(m):
        i, you = map(int,input().split())
        friend[i][you] = friend[you][i] = 1
    # print(friend)

    now = 1
    q = [now]
    invite[now] = 1
    cnt = -1
    while q and max(best)<3: #최대누적 bfs횟수가 3보다 작을때까지만
        now = q.pop(0)
        cnt += 1
        # print(best)
        for next in range(1,n+1):
            if friend[now][next] and not invite[next] and best[now]+1 <= 2:
                best[next] = best[now] + 1
                # if best[next] <= 2:
                q.append(next)
                invite[next] = 1

    print('#{} {}'.format(tc+1,cnt))



