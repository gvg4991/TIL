# 문제
# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 n(1≤n≤100,000)이 주어진다. 다음 줄에는 인오더를 나타내는 n개의 자연수가 주어지고, 그 다음 줄에는 같은 식으로 포스트오더가 주어진다.
#
# 출력
# 첫째 줄에 프리오더를 출력한다.


import sys
sys.stdin = open('input.txt')


inorder = []
postorder = []

def order(in_l, in_r, post_l, post_r):
    if post_l <= post_r:
        head = postorder[post_r]
        print('{}'.format(head))
        idx = inorder.index(head)
        order(in_l, idx-1, post_l, idx-1)
        order(idx+1, in_r, idx+1, post_r)



        # print('{}'.format(head))
        # idx = inorder.index(head)
        # order(in_l, idx-1, post_l, post_l+idx-in_l-1)
        # order(idx+1, in_r, post_r+idx-in_r, post_r-1)

        # left = idx - in_l
        # right = in_r - idx
        # order(in_l, in_l + left - 1, post_l, post_l + left - 1)
        # order(in_r - right + 1, in_r, post_r - right, post_r - 1)


n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
order(0, n-1, 0, n-1)