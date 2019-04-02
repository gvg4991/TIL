import sys, time
sys.stdin = open('input.txt')
stime = time.time()


def eating(used):
    global dist, ans
    if used == n and ans>dist:
        # result.append(dist)
        ans = dist
        return
    for i in range(n):
        if not eat[i] and dist+abs(s[used][0]-r[i][0])+abs(s[used][1]-r[i][1])<ans:
            dist += abs(s[used][0]-r[i][0])+abs(s[used][1]-r[i][1])
            eat[i] = 1
            eating(used+1)
            eat[i] = 0
            dist -= abs(s[used][0]-r[i][0])+abs(s[used][1]-r[i][1])


for tc in range(int(input())):
    n = int(input())
    snack = list(map(int,input().split()))
    robot = list(map(int,input().split()))

    s=[(0,0)]*n
    r=[(0,0)]*n
    for case in range(n):
        s[case] = (snack[2*case],snack[2*case+1])
        r[case] = (robot[2*case],robot[2*case+1])
    # print(s)
    # print(r)

    used = 0
    dist = 0
    eat = [0]*n
    # result = []
    ans = 987654321
    eating(used)
    # ans = min(result)
    print('#{} {}'.format(tc+1,ans))
    print(time.time()-stime)