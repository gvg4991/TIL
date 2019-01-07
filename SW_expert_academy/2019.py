# 1부터 주어진 횟수까지 2를 곱한 값(들)을 출력하시오.
# 주어질 숫자는 30을 넘지 않는다. 

a=int(input())
for n in range(a+1):
    print(2**n,end=' ')

# a=int(input())
# b=0
# while b<=a:
#     print(2**b,end=' ')
#     b += 1