# 어떤 문자열 A를 타이핑하려고 한다.
# 그냥 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 할 것이다.
# 여기에 속도를 조금 더 높이기 위해 어떤 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
# 이미 타이핑 한 문자를 지우는 것은 불가능하다.
# 예를 들어 A=”asakusa”, B=”sa”일 때, 다음 그림과 같이 B를 두 번 사용하면 5번 만에 A를 타이핑 할 수 있다.
# A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하여라.
# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스마다 첫 번째 줄에 두 문자열 A, B가 주어진다. A의 길이는 1이상 10,000이하, B의 길이는 1이상 100이하이다.
# [출력]
# 각 테스트 케이스마다 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 출력한다.


import sys
sys.stdin = open("input.txt")

#창언이형
casesize = int(input())
for case in range(casesize):
    a, b = input().split()
    a = a.replace(b, '-')
    print('#', case + 1, ' ', len(a), sep="")


#
# test = int(input())
# for tc in range(test):
#     a,b = map(str,input().split())
#     voca = list(a)
#     find = list(b)
#
#     queue = []
#     count = 0
#
#     if len(voca) >= len(find):
#         for i in range(len(find)):
#             queue.append(voca.pop(0))
#             count += 1
#         if len(voca) == 0 and queue == find:
#             count = 1
#     else:
#         for i in range(len(voca)):
#             voca.pop(0)
#             count += 1
#
#     while voca != []:
#         if queue != find:
#             queue.pop(0)
#             queue.append(voca.pop(0))
#             count += 1
#
#         if queue == find:
#             count = count - len(find) + 1
#             queue = []
#             if len(voca) >= len(find):
#                 for i in range(len(find)):
#                     queue.append(voca.pop(0))
#                     count += 1
#                 if len(voca) == 0 and queue == find:
#                     count = count - len(find) + 1
#             elif len(voca) == 0:
#                 break
#             else:
#                 for i in range(len(voca)):
#                     voca.pop(0)
#                     count += 1
#
#     print('#{} {}'.format(tc+1,count))



#-----------------
    # while result == False:
    #     if len(voca) < len(find) or voca[point+len(find)-1] == 0:
    #         result = True
    #         break
    #     elif voca[point:point+len(find)] == find:
    #         for delete in range(len(find)):
    #             voca.pop(point)
    #         voca.append(0)
    #     else:
    #         point += 1
    # print('#{} {}'.format(tc+1,len(voca)-1))

#----------------
    # for point in range(len(voca)-len(find)+1):
    #     if voca[point:point+len(find)] == find:
    #         for delete in range(len(find)):
    #             voca.pop(point)
    #         voca.append(0)
    #     elif voca[point] == 0:
    #         break
    # print('#{} {}'.format(tc+1,len(voca)))
    # # print(voca)
#----------------

    # for point in range(len(voca) - len(find) + 1):
    #     if b in a:
    #         c = a.find(b)
    #
    #         # a+='0'
    # # print(c)
# ----------------


    # queue = []
    # for point in range(len(voca)):
    #     target = voca.pop(0)
    #     queue.append(target)
    #     if len(queue) == len(find):
    #         if queue == find:
    #
    #
    #     if voca[point:point+len(find)] == find:
    #         for delete in range(len(find)):
    #             voca.pop(point)
    #         voca.append(0)
    # print('#{} {}'.format(tc+1,len(voca)))