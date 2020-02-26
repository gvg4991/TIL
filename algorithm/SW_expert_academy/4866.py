# 주어진 입력에서 괄호 {}, ()가 제대로 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

# test = int(input())
# for tc in range(test):
#     data = list(map(str,input()))
#     stack = []
#     top = -1
#     result = 1

#     for i in range(len(data)):
#         if data[i] == '(' or data[i] == '{' or data[i] == '[' or data[i] == '<':
#             stack.append(data[i])
#             top += 1

#         elif data[i] == ')' and top > -1:
#             item = stack.pop(top)
#             top -= 1
#             if item != '(' :
#                 result = 0
#                 break
#         elif data[i] == '}' and top > -1:
#             item = stack.pop(top)
#             top -= 1
#             if item != '{':
#                 result = 0
#                 break
#         elif data[i] == ']' and top > -1:
#             item = stack.pop(top)
#             top -= 1
#             if item != '[':
#                 result = 0
#                 break
#         elif data[i] == '>' and top > -1:
#             item = stack.pop(top)
#             top -= 1
#             if item != '<':
#                 result = 0
#                 break

#     if top == -1 and result == 1:
#         print(f'#{tc+1} 1')
#     else:
#         print(f'#{tc+1} 0')


test = int(input())
for tc in range(test):
    data = list(map(str,input()))
    stack = []
    top = -1
    
    info = [0] *128
    info[ord(')')] = '('
    info[ord('}')] = '{'
    info[ord(']')] = '['
    info[ord('>')] = '<'

    d_in = ['(','[','<','{']
    d_out = [')','}',']','>']

    howmany = len(data)
    result = 1
    for i in range(howmany):
        if data[i] in d_in:
            stack.append(data[i])
            top += 1
        elif data[i] in d_out:
            if info[ord(data[i])] == stack[top] and top > -1:
                item = stack.pop(top)
                top -= 1
            else:
                result = 0
                break

    if top == -1 and result == 1:
        print(f'#{tc+1} 1')
    else:
        print(f'#{tc+1} 0')