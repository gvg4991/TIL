import sys
sys.stdin = open('input.txt')


def test(l,r,t):
    global cnt
    cnt = 0
    for i in range(k):
        target = datas[i]
        cnt += t//target #시간동안 통과할 수 있는 총 사람 수
    if cnt == n:
        result.append(t)
        return
    elif cnt > n:
        r = t
        t = (l+r)//2
        test(l,r,t)
    elif cnt < n:
        l = t
        t = (l+r)//2
        test(l,r,t)


k,n = map(int,input().split())
datas = [0]*k
for i in range(k):
    datas[i] = int(input())
# print(datas)

r = max(datas)*n
l = min(datas)
t = max(datas)*n
cnt = 0
result = []

test(l,r,t)
print(result)