# 보통의 정렬은 오름차순이나 내림차순으로 이루어지지만, 이번에는 특별한 정렬을 하려고 한다.
# N개의 정수가 주어지면 가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수 식으로 큰 수와 작은 수를 번갈아 정렬하는 방법이다.
# 예를 들어 1부터 10까지 10개의 숫자가 주어지면 다음과 같이 정렬한다.
# 10 1 9 2 8 3 7 4 6 5
# 주어진 숫자에 대해 특별한 정렬을 한 결과를 10개까지 출력하시오
# 입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 다음 줄에 정수의 개수 N이 주어지고 다음 줄에 N개의 정수 ai가 주어진다. 10<=N<=100, 1<=ai<=100
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 특별히 정렬된 숫자를 10개까지 출력한다.

# test = int(input())
# for tc in range(test):
#     case = int(input())
#     datas = list(map(int,input().split()))

    # large_result = None
    # small_result = None
    # result = []
    # count = 0

    # while count < (case/2+0.8):
    #     count += 1
    #     for i in datas:
    #         if large_result == None or large_result < i:
    #             large_result = i

    #         if small_result == None or small_result > i:
    #             small_result = i
            
    #     result.append(large_result)
    #     result.append(small_result)

# ----------------------------------------------------------------

    # datas=sorted(datas)
    # small = datas[0:int(case/2)]
    # large = datas[int(case/2):]

    # result = []
    # for i in range(5):
    #     result.append(large[-i-1])
    #     result.append(small[i])

    # print(f'#{tc+1} {" ".join(map(str,result))}')


# ---------------------------------------------------------------

test = int(input())
for tc in range(test):
    case = int(input())
    datas = list(map(int,input().split()))

    datas=sorted(datas)
    result = []
    for i in range(5):
        result += [datas[-i-1]]
        result += [datas[i]]

    print(f'#{tc+1} {" ".join(map(str,result))}')
