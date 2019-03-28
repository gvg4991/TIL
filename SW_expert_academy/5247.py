# 자연수 N에 몇 번의 연산을 통해 다른 자연수 M을 만들려고 한다.
# 사용할 수 있는 연산이 +1, -1, *2, -10 네 가지라고 할 때 최소 몇 번의 연산을 거쳐야 하는지 알아내는 프로그램을 만드시오.
# 단, 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다.
# 예를 들어 N=2, M=7인 경우, (2+1) *2 +1 = 7이므로 최소 3번의 연산이 필요한다.
# [입력]
# 첫 줄에 테스트 케이스의 개수가 주어지고, 다음 줄부터 테스트 케이스 별로 첫 줄에 N과 M이 주어진다. 1<=N, M<=1,000,000, N!=M
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.


# import sys
# sys.stdin = open("input.txt")
# import collections
# q=collections.deque([0])
# q.popleft()

for tc in range(int(input())):
    target,goal = map(int,input().split())
    #10000007
    # q = [target]*1000000
    q = [target]
    push = 1
    pull = 0
    # cnt = [0]*1000000
    cnt = [0]
    cnt_i = -1
    ans = 0

    while target != goal:
        calculation = [1, -1, target, -10]
        cnt_i += 1
        for calc in calculation:
            if target+calc == goal:
                # q[push] = target+calc
                # target = q[push]
                # cnt[push] = cnt[cnt_i] + 1
                # ans = cnt[push]
                target = target+calc
                ans = cnt[cnt_i]+1
                break
            if  (target+calc in q) or target+calc <= 0 or target+calc > 1000000:
                continue
            else:
                # q[push] = target+calc
                # cnt[push] = cnt[cnt_i] + 1
                # push += 1
                q.append(target+calc)
                cnt.append(cnt[cnt_i]+1)
        if ans == 0:
            pull += 1
            target = q[pull]

    print('#{} {}'.format(tc+1,ans))



