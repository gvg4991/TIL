# 1부터 12까지의 숫자를 원소로 가진 집합 A가 있다. 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력하는 프로그램을 작성하시오.
# 해당하는 부분집합이 없는 경우 0을 출력한다. 모든 부분 집합을 만들어 답을 찾아도 된다.
# 예를 들어 N = 3, K = 6 경우, 부분집합은 { 1, 2, 3 } 경우 1가지가 존재한다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 테스트 케이스 별로 부분집합 원소의 수 N과 부분 집합의 합 K가 여백을 두고 주어진다. ( 1 ≤ N ≤ 12, 1 ≤ K ≤ 100 ) 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

test = int(input())
for tc in range(test):
    n,k = map(int,input().split())

    datas = range(1,12+1)
    subs = []
    for i in range(1<<len(datas)): # 부분집합 전체 갯수
        subset = []
        for j in range(len(datas)+1): # 데이터 수, 2진수로 한번 확인할 때 수[1 0 1 0]=4개
            if i & (1<<j):
                subset.append(datas[j])
        subs.append(subset)
    # print(subs)

    result = []
    count = 0
    for sub_i in subs:
        if len(sub_i) == n and sum(sub_i) == k:
            result += sub_i
            count += 1
    
    print(f'#{tc+1} {count}')