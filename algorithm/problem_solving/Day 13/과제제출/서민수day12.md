1. 문자열비교 KMP (4864)

```python
for tc in range(1, int(input())+1):
    pattern = str1 = input()
    str2 = input()

    pi = [0 for _ in range(len(pattern))]
    pi[0] = -1;
    i = 0; j = 1
    while j != len(pattern)-1 :
        if pattern[i] != pattern[j]:
            if i:
                i = 0
            else:
                j+=1
                pi[j]=0
        else:
            if i:
                pi[j+1] = pi[j] + 1
            else:
                pi[j+1] = 1
            i += 1; j += 1
    #print(pi)
    p=0; i = 0; k = 0; result = 0
    while i != len(str2):
        if str2[i] == str1[k]:
            i+=1
            k+=1
        else:
            p = k - pi[k] + p
            i = p
            k = 0

        if k == len(pattern):
            result = 1
            break
    print('#{0} {1}'.format(tc, result))

```



2. 문자열비교  BruteForce (4864)

```python
for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    result = 0
    for i in range(len(str2)-len(str1)+1):
        cnt = 0
        for j in range(len(str1)):
            if str2[i+j] == str1[j]:
                cnt += 1
        if cnt == len(str1):
            result = 1
            break
    print('#{0} {1}'.format(tc, result))

```



3. 회문 (4861)

```python
for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    Data = [input() for _ in range(N)]
    #print(Data)
    palind = []
    Is_done = False
    for y in range(N):
        if Is_done: break
        for x in range(N):
            if x+M-1 < N:
                if Data[y][x:x+M] == ''.join(reversed(Data[y][x:x+M])):
                    palind = Data[y][x:x+M]
                    Is_done = True
                    break
            if y+M-1 < N:
                cnt = 0
                for k in range(M//2):
                    if Data[y+k][x] == Data[y+M-1-k][x]:
                        cnt += 1
                    else: break
                if cnt == M//2:
                    for i in range(M):
                        palind.append(Data[y+i][x])
                    Is_done = True
                    break
    print('#{0} {1}'.format(tc, ''.join(palind)))
```



4. 회문2 (1216)

```python
for _ in range(1, 11):
    tc = int(input())
    string = [input() for _ in range(100)]
    result = 0
    Is_done = False
    for m in range(100,0,-1):
        if Is_done: break
        for y in range(100):
            if Is_done: break
            for x in range(100):
                # x 범위 제한
                if x+m <= 100:
                    if string[y][x:x + m] == ''.join(reversed(string[y][x:x + m])):
                        result = m
                        Is_done = True
                        break

                # y 범위 제한
                if y+m <= 100:
                    cnt = 0
                    for k in range(m // 2):
                        if string[y + k][x] == string[y + m - 1 - k][x]:
                            cnt += 1
                        else:
                            break
                    if cnt == m // 2:
                        result = m
                        Is_done = True
                        break
    print('#{0} {1}'.format(tc, result))
# 실행속도 느립니다..
```



5. 글자수 (4865)

```python
for tc in range(1, int(input())+1):
    str1 = input()
    str2 = input()
    MAX = 0
    for c1 in set(str1):
        cnt = 0
        for c2 in str2:
            if c1 == c2:
                cnt += 1
        if cnt > MAX:
            MAX = cnt
    print('#{0} {1}'.format(tc, MAX))
```



6. GNS(1221)

```python
string = {0: 'ZRO', 1: 'ONE', 2: 'TWO', 3: 'THR',
              4: 'FOR', 5: 'FIV', 6: 'SIX', 7: 'SVN',
              8: 'EGT', 9: 'NIN',}

decimal = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3,
          'FOR': 4, 'FIV': 5, 'SIX': 6, 'SVN': 7,
          'EGT': 8, 'NIN': 9}

for tc in range(1,int(input())+1):
    T, length = input().split()
    numbers = list(input().split())

    for i in range(int(length)):
        numbers[i] = decimal[numbers[i]]
    numbers.sort()

    for j in range(int(length)):
        numbers[j] = string[numbers[j]]

    print('#{} {}'.format(tc, ' '.join(numbers)))

```



7. 민석이의과제체크하기(5431)

```python
for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    submit = list(map(int, input().split()))
    result = []

    for i in range(1, N+1):
        for j in range(K):
            if i == submit[j]:
                break
        else:
            result.append(str(i))
    result = ' '.join(result)
    print('#{} {}'.format(tc, result))
```



