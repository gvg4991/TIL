'''
문제 3.
숫자를 입력 받아 짝수/홀수를 구분하는 코드를 작성하시오.
'''

number = int(input('숫자를 입력하세요: '))
# 아래에 코드를 작성해 주세요.

# number=3
if number % 2 == 0:
    print("짝수")
else:
    print("홀수")

# %: 나머지를 구함, //: 몫을 구함

#비교 연산자 없으면 false, true로 구분
#if number % 2:
# prnt("홀수") - true
#else:
# print("짝수") - false