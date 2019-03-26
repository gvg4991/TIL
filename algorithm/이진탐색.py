import sys
sys.stdin = open('input.txt')


# def find(l,r,v):
#     global m, ans, left, right
#     if v > a[r] or v < a[l] or l == r:
#         return
#     if left == False and right == False:
#         if v==a[r] or v==a[l] or v==a[m]:
#             ans += 1
#             return
#     else:
#         if v==a[m]:
#             ans += 1
#             return
#     if v < a[m]:
#         if left == False:
#             left = True
#             right = False
#             r = m-1
#         elif left == True:
#             return
#     elif v > a[m]:
#         if right == False:
#             right = True
#             left = False
#             l = m+1
#         elif right == True:
#             return
#     m = (l+r)//2
#     find(l,r,v)





def find(l,r,v):
    global m, ans, left, right
    if v > a[r] or v < a[l]:
        return

    if left == False and right == False:
        if v==a[r] or v==a[l] or v==a[m]:
            ans += 1
            return

    if v==a[m]:
        ans += 1
        return
    elif v < a[m]:
        if left == False:
            left = True
            right = False
            r = m-1
        elif left == True:
            return
    elif v > a[m]:
        if right == False:
            right = True
            left = False
            l = m+1
        elif right == True:
            return
    m = (l+r)//2
    find(l,r,v)


for tc in range(int(input())):
    n,m = map(int,input().split())
    a = sorted(list(map(int,input().split())))
    b = list(map(int,input().split()))

    # l = 0
    # r = len(a)-1
    # m = (l+r)//2
    ans = 0
    # left = False
    # right = False

    for value in b:
        l = 0
        r = len(a) - 1
        m = (l + r) // 2
        left = False
        right = False
        find(l,r,value)
    print('#{} {}'.format(tc+1,ans))



    # while m!=l and m!=r:
