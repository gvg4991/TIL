# 0에서 9까지 숫자가 적힌 N장의 카드가 주어진다.
# 가장 많은 카드에 적힌 숫자와 카드가 몇 장인지 출력하는 프로그램을 만드시오. 카드 장수가 같을 때는 적힌 숫자가 큰 쪽을 출력한다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 다음 줄부터 테스트케이스의 첫 줄에 카드 장수 N이 주어진다. ( 5 ≤ N ≤ 100 )
# 다음 줄에 N개의 숫자 ai가 여백없이 주어진다. (0으로 시작할 수도 있다.)  ( 0 ≤ ai ≤ 9 ) 
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 가장 많은 카드의 숫자와 장 수를 차례로 출력한다.

test = int(input())
for tc in range(test):
    case = int(input())
    datas = str(input())

    empty=[]
    for data in datas:
        empty+=[int(data)]

    cnt=[0]*(max(empty)+1)
    for item in empty:
        cnt[item]+=1

    result=0
    resulti=0
    for cnti in range(len(cnt)):
        if result<cnt[cnti]:
            result=cnt[cnti]
            resulti=cnti
        elif result==cnt[cnti]:
            if resulti<cnti:
                resulti=cnti

    print(f'#{tc+1} {resulti} {result}')
    
