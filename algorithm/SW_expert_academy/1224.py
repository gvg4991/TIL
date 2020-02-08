# 문자열로 이루어진 계산식이 주어질 때, 이 계산식을 후위 표기식으로 바꾸어 계산하는 프로그램을 작성하시오.
# 예를 들어
# “3+(4+5)*6+7”
# 라는 문자열로 된 계산식을 후위 표기식으로 바꾸면 다음과 같다.
#  "345+6*+7+"
# 변환된 식을 계산하면 64를 얻을 수 있다.
# 문자열 계산식을 구성하는 연산자는 +, * 두 종류이며 문자열 중간에 괄호가 들어갈 수 있다.
#  때 괄호의 유효성 여부는 항상 옳은 경우만 주어진다.
# 피연산자인 숫자는 0 ~ 9의 정수만 주어진다.
# [입력]
# 각 테스트 케이스의 첫 번째 줄에는 테스트 케이스의 길이가 주어진다. 그 다음 줄에 바로 테스트 케이스가 주어진다.
# 총 10개의 테스트 케이스가 주어진다.
# [출력]
#  #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 답을 출력한다. 

for tc in range(10):
    case = int(input())
    datas = list(input())

    push = 0
    sem = []
    result = []

    for data in datas:
        if data == '(':
            sem.append(data)
        elif data == ')':
            while push == 0:
                sem_i = sem.pop()
                if sem_i != '(':
                    result.append(sem_i)
                else:
                    push = 1
            push = 0
        elif data == '*' or data == '/':
            sem.append(data)
        elif data == '+' or data == '-':
            while push == 0:
                if sem == []:
                    sem.append(data)
                    push = 1
                else:
                    sem_i = sem.pop()
                    if sem_i == '*' or sem_i == '/':
                        result.append(sem_i)
                    else:
                        sem.append(sem_i)
                        sem.append(data)
                        push = 1
            push = 0
        else:
            result.append(int(data))

    for sem_v in sem[::-1]:
        result.append(sem_v)

    calculation = []
    buho = ['+','-','*','/']

    for value in result:
        if not value in buho:
            calculation.append(value)
        else:
            back = calculation.pop()
            front = calculation.pop()
            if value == '+':
                cal = front + back
            elif value == '*':
                cal = front * back
            elif value == '-':
                cal = front - back
            elif value == '/':
                cal = front / back
            calculation.append(cal)

    c = calculation.pop()    
    print(f'#{tc+1} {c}')

# #------------------------------------------------------------------------------------------------
# # 후위 표기법
# case = int(input())
# datas = list(input())

# push = pull = 0
# sem = []
# result = []

# for data in datas:
#     if data == '(':
#         sem.append(data)
#     elif data == ')':
#         while push == 0:
#             sem_i = sem.pop()
#             if sem_i != '(':
#                 result.append(sem_i)
#             else:
#                 push = 1
#         push = 0
#     elif data == '*' or data == '/':
#         sem.append(data)
#     elif data == '+' or data == '-':
#         while push == 0:
#             if sem == []:
#                 sem.append(data)
#                 push = 1
#             else:
#                 sem_i = sem.pop()
#                 if sem_i == '*' or sem_i == '/':
#                     result.append(sem_i)
#                 else:
#                     sem.append(sem_i)
#                     sem.append(data)
#                     push = 1
#         push = 0
#     else:
#         result.append(int(data))

# for sem_v in sem[::-1]:
#     result.append(sem_v)

# print(result)

# #-------------------------------------------------------------------------------------------------
# # 후위표기법 계산

# calculation = []
# buho = ['+','-','*','/']

# for value in result:
#     if not value in buho:
#         calculation.append(value)
#     else:
#         back = calculation.pop()
#         front = calculation.pop()
#         if value == '+':
#             cal = front + back
#         elif value == '*':
#             cal = front * back
#         elif value == '-':
#             cal = front - back
#         elif value == '/':
#             cal = front / back
#         calculation.append(cal)

# c = calculation.pop()    
# print(f'#{1} {c}')