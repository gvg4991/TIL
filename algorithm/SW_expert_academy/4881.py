# NxN 배열에 숫자가 들어있다. 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려고 한다. 단, 세로로 같은 줄에서 두 개 이상의 숫자를 고를 수 없다.
# 조건에 맞게 숫자를 골랐을 때의 최소 합을 출력하는 프로그램을 만드시오.
# 예를 들어 다음과 같이 배열이 주어진다.
# 212
# 585
# 722
# 이경우 1, 5, 2를 고르면 합이 8로 최소가 된다.
# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 첫 줄에 숫자 N이 주어지고, 이후 N개씩 N줄에 걸쳐 10보다 작은 자연수가 주어진다. 3≤N≤10
# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 합계를 출력한다.

# def min_sum(y):
#     global result, ing
#     if y >= case:
#         if result == None or result > ing:
#             result = ing
#         return

#     else:
#         for x in range(case):
#             if select_x[x] == 0:
#                 ing += datas[y][x]
#                 select_x[x] = 1
#                 new_y = y+1
#                 min_sum(new_y)
                
#                 ing -= datas[y][x]
#                 select_x[x] = 0

# test = int(input())
# datas = []
# for tc in range(test):
#     case = int(input())
#     datas += [list(map(int,input().split()))]

#     select_x = [0]*case
#     ing = 0
#     result = 0
#     y = 0

#     print(f'#{tc+1} {result}')



# 함수에 쓸 변수를 미리 언급해주기
datas = []
ing = 0
result = None

def min_sum(y):
    global result, ing
    if y < case:
        for x in range(case):
            if select_x[x] == 0 and (result == None or ing < result): 
            #간적이 없거나 중간에 합쳐진 ing값이 결과값보다 커진 경우
                ing += datas[y][x]
                select_x[x] = 1
                new_y = y+1
                min_sum(new_y) # 재귀
                
                ing -= datas[y][x] # 재귀가 끝나고 return된 후에 실행 (리턴된 만큼 ing 진행값을 빼줌)
                select_x[x] = 0 # 다시 갈 수 있도록 0으로 바꿔줌
                new_y = 0 # y에 새로운 값 줄수있도록 준비(없어도 됨)
    else:
        if result == None or result > ing:
            result = ing
        return

test = int(input())
for tc in range(test):
    case = int(input())
    datas = []
    select_x = [0]*case
    ing = 0
    result = None
    y = 0

    for row in range(case):
        datas += [list(map(int,input().split()))]

    min_sum(y)
    print(f'#{tc+1} {result}')

