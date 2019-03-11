# 문제
# N개의 수로 이루어진 수열 A[1], A[2], …, A[N]이 있다. 이 수열에 대해서 버블 소트를 수행할 때, Swap이 총 몇 번 발생하는지 알아내는 프로그램을 작성하시오.
# 버블 소트는 서로 인접해 있는 두 수를 바꿔가며 정렬하는 방법이다. 예를 들어 수열이 3 2 1 이었다고 하자. 이 경우에는 인접해 있는 3, 2가 바뀌어야 하므로 2 3 1 이 된다. 다음으로는 3, 1이 바뀌어야 하므로 2 1 3 이 된다. 다음에는 2, 1이 바뀌어야 하므로 1 2 3 이 된다. 그러면 더 이상 바꿔야 할 경우가 없으므로 정렬이 완료된다.
# 입력
# 첫째 줄에 N(1≤N≤500,000)이 주어진다. 다음 줄에는 N개의 정수로 A[1], A[2], …, A[N]이 주어진다. 각각의 A[i]는 0≤|A[i]|≤1,000,000,000의 범위에 들어있다.
# 출력
# 첫째 줄에 Swap 횟수를 출력한다



import sys
sys.stdin = open("input.txt")


cnt = 0

def merge_sort(n):
    global result
    if len(n) <= 1:
        return n
    mid = len(n)//2
    left = n[:mid]
    right = n[mid:]

    left = merge_sort(left) #7
    right = merge_sort(right) #2

    return merge(left,right) #7,2

def merge(left,right):
    global result, cnt
    result = [0]*(len(left)+len(right)) #00
    i = l = r = 0

    while l<len(left) and r<len(right): # 둘다 0보다 클때 반복
        if left[l] < right[r]:
            result[i] = left[l]
            l += 1
        else:
            result[i] = right[r]
            r += 1
        i += 1

    if len(left)-l>0:
        result[i:] = left[l:]
    elif len(right)-r>0:
        result[i:] = right[r:]

    cnt += 1
    return result

case = int(input())
datas = list(map(int,input().split()))
merge_sort(datas)
print(cnt)