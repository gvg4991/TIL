import sys
sys.stdin = open('input.txt')


def production(c):
    global cnt, result, ans
    if c == n:
        if result < ans:
            ans = result
        return

    if result > ans:
        return

    for i in range(n):
        if choice[i]:
            choice[i] = 0
            result += datas[cnt][i]
            cnt += 1
            production(cnt)
            cnt -= 1
            result -= datas[cnt][i]
            choice[i] = 1


for tc in range(int(input())):
    n = int(input())
    datas = [[0]*n for _ in range(n)]
    for case in range(n):
        datas[case] = list(map(int,input().split()))

    choice = [1]*n
    cnt = 0
    result = 0
    ans = 987654321
    production(0)
    print('#{} {}'.format(tc+1,ans))





