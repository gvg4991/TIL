'''
문제 1.
문자열을 입력받아 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
'''

str = input('문자를 입력하세요: ')
# 아래에 코드를 작성해 주세요.

total = len(str)
first = str[0]
last = str[total-1]
# [a,b,c,d,e] = 0,1,2,3,4 = -5,-4,-3,-2,-1

print(first)
print(last)