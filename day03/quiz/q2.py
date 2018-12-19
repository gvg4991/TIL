'''
문제 2.
자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.
'''

n = int(input('숫자를 입력하세요: ')) 
#int는 숫자만 받겠다. 문자열 들어오면 에러!
#int:문자를 숫자로 바꿔줌, str: 숫자를 문자로 바꿔줌

# 아래에 코드를 작성해 주세요.

#while 문
#i = 0
#while i < 5:
#    print(i+1)
#    i += 1

#for 문(선호)
#n = 5
for i in range(n):
    print(i+1)

#for i in range(1,n+1):
#   print(i)