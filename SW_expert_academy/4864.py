# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.
# 예를 들어 두 개의 문자열이 다음과 같이 주어질 때, 첫 문자열이 두번째에 존재하면 1, 존재하지 않으면 0을 출력한다.
# ABC
# ZZZZZABCZZZZZ
# 두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
# ABC
# ZZZZAZBCZZZZZ
# 문자열이 일치하지 않으므로 0을 출력.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  (1≤T≤50)
# 다음 줄부터 테스트 케이스 별로 길이가 N인 문자열 str1과 길이가 M인 str2가 각각 다른 줄에 주어집니다. (5≤N≤100, 10≤M≤1000, N≤M)
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

test = int(input())
for tc in range(test):
    n = list(input()) #작은거
    m = list(input()) #큰거

#pitable만들기
    pitable = [0] * len(n)
    i = 0
    j = 1
    pitable[0] = -1
    pitable[1] = 0

    while j < len(n)-1:
        if n[i] == n[j]:
            pitable[j+1] = pitable[j] + 1
            i += 1
            j += 1
        else:
            if i != 0:
                i = 0
            else:
                pitable[j+1] = 0
                j += 1
    # print(pitable)

    k = 0
    move = 0
    result = 0
    while k != len(n) and move+len(n) <= len(m):
        k = 0
        for n_index in range(len(n)):
            if n[n_index] == m[move + n_index]:
                k += 1
            else:
                move = move + (k - pitable[k])
                break

            if k == len(n):
                result = 1
    
    print('#{} {}'.format(tc+1,result))

    
        

