# 다음 100X100의 2차원 배열이 주어질 때, 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 구하는 프로그램을 작성하여라.
# 다음과 같은 5X5 배열에서 최댓값은 29이다.
# [제약 사항]
# 총 10개의 테스트 케이스가 주어진다.
# 배열의 크기는 100X100으로 동일하다.
# 각 행의 합은 integer 범위를 넘어가지 않는다.
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다.
# [입력]
# 각 테스트 케이스의 첫 줄에는 테스트 케이스 번호가 주어지고 그 다음 줄부터는 2차원 배열의 각 행 값이 주어진다.
# [출력]
#  #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스의 답을 출력한다. 

for tc in range(10):
    case = input()
    datas = []
    for data_i in range(100):
        datas += [list(map(int,input().split()))]
    
    max_x = max_y = max_cross = 0
    for y in range(100):
        sum_x = 0
        for x in range(100):
            sum_x += datas[y][x]
            if max_x < sum_x:
                max_x = sum_x

    for x in range(100):
        sum_y = 0
        for y in range(100):
            sum_y += datas[y][x]
            if max_y < sum_y:
                max_y = sum_y

    sum_cross = 0
    for y in range(100):
        x=y
        sum_cross += datas[y][x]
        if max_cross < sum_cross:
            max_cross = sum_cross

    result = max(max_x,max_y,max_cross)
    print(f'#{case} {result}')

    
                


