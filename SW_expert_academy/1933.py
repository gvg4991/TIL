# 입력으로 1개의 정수 N 이 주어진다.
# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
# [제약사항]
# N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
# [입력]
# 입력으로 정수 N 이 주어진다.
# [출력]
# 정수 N 의 모든 약수를 오름차순으로 출력한다.

# a=int(input())
# b=1
# for i in range(a):
#     if a%b==0:
#         print(b,end=' ')
#         b+=1
#     else:
#         b+=1

a=int(input())
b=1
while b<=a:
    if a%b==0:
        print(b,end=' ')
        b+=1
    else:
        b+=1