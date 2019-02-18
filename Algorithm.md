- 알고리즘 성능 분석

ex) sum() -- O(n)
ex) 1부터 n까지 합: n(n+1)/2 -- O(1)



- 용어

O(big o): upper bound
-신뢰성↑, 최악의 케이스

θ: tight bound

Ω: lower bound
-신뢰성↓, 최고의 케이스



- 리스트 범위 옮기기

k=5
list[start​:start+k]



- 데이터를 변수에 지정하기

l,m,n = map(int,input().split())



A << B = (A) * (2^B)
A >> B = (A) / (2^B)
(A+B) /2 = (A + B) >>1
 FIND ODDS
• if(N%2==1)
• if(N&1)

ex)
1 << 4 = 16
3 << 3 = 24 (3 * 2^3) 
5 << 10 = 5120 (5 * 2^10)



int = 4byte
char = 1byte



for i in range(1<<n):

for j in range(n):

if i & (1 << j):

print(arr[j], end=", ")