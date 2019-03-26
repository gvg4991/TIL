# 알고 교수는 학생들에게 병합 정렬을 이용해 오름차순으로 정렬하는 과제를 내려고 한다. 정렬 된 결과만으로는 실제로 병합 정렬을 적용했는지 알 수 없기 때문에 다음과 같은 제약을 주었다. 
# N개의 정렬 대상을 가진 리스트 L을 분할할 때 L[0:N//2], L[N//2:N]으로 분할 한다. 
# 병합 과정에서 다음처럼 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력한다. 
# 2 4 7 8  1 3 5 6                    1 2 3 4 5 6 7 8 
 
# 정렬이 끝난 리스트 L에서 L[N//2] 원소를 출력한다. 
# 알고 교수의 조건에 따라 병합 정렬을 수행하는 프로그램을 만드시오. 
 
# 입력 
# 첫 줄에 테스트케이스의 수 T가 주어진다. 1<=T<=50 
# 다음 줄부터 테스트 케이스의 별로 정수의 개수 N이 주어지고, 다음 줄에 N개의 정수 ai가 주어 진다. 
# 5<=N<=1,000,000, 0 <= ai <= 1,000,000 
 
# 출력 
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 오른쪽 원소가 먼저 복사되는 경우의 수, N//2번 원소를 출력한다.


import sys
sys.stdin = open('input.txt')


def merge_sort(n):
    global result, cnt, ans
    if len(n) <= 1:
        return n
    mid = len(n)//2
    left = n[:mid]
    right = n[mid:]

    left = merge_sort(left) #7
    right = merge_sort(right) #2
    if left[-1] > right[-1]:
        cnt+=1


    return merge(left,right) #7,2

def merge(left,right):
    global result
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

    return result


for tc in range(int(input())):
    case = int(input())
    datas = list(map(int,input().split()))
# result = [0]*len(datas)

    cnt = 0
    merge_sort(datas)
    ans = result[len(datas)//2]
    # print(result)
    print('#{} {} {}'.format(tc+1,ans,cnt))


