# ※ SW Expert 아카데미의 문제를 무단 복제하는 것을 금지합니다.
# 비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때, 가장 나중에 연락을 받게 되는 사람 중 번호가 가장 큰 사람을 구하는 함수를 작성하시오.
# [예시]
# 아래는 비상연락망을 나타낸 그림이다.
# 각 원은 개개인을 의미하며, 원 안의 숫자는 그사람의 번호를 나타내고 빨간원은 연락을 시작하는 당번을 의미한다.
# 화살표는 연락이 가능한 방향을 의미한다.
# 위의 예시에서는 7번과 1번은 서로 연락이 가능하다,
# 하지만 2번과 7번의 경우 2번은 7번에게 연락할 수 있지만 7번은 2번에게 연락할 수 없다.
# 비상연락망이 가동되면 아래 그림과 같이 연락을 시작하는 당번인 2번은 연락 가능한 7번과 15번에 동시에 연락을 취한다 (다자 간 통화를 사용한다고 가정).
# 그 다음 아래와 같이 7번은 1번에게, 15번은 4번에게 연락을 취한다 (이 과정은 동시에 일어난다고 가정한다).
# 그 다음 아래와 같이 1번은 8번과 17번에게 동시에 연락하며, 이와 동시에 4번은 10번에게 연락한다.
# 7번과 2번의 경우는 이미 연락을 받은 상태이기 때문에 다시 연락하지 않는다.
# 위의 모습이 연락이 끝난 마지막 모습이 되며, 마지막에 동시에 연락 받은 사람은 8번, 10번, 17번의 세 명이다.
# 이 중에서 가장 숫자가 큰 사람은 17번이므로 17을 반환하면 된다.
# ※ 3, 6, 11, 22번은 시간이 지나도 연락을 받지 못한다.
# [제약 사항]
# 연락 인원은 최대 100명이며, 부여될 수 있는 번호는 1이상, 100이하이다.
# 단, 예시에서 5번이 존재하지 않듯이 중간 중간에 비어있는 번호가 있을 수 있다.
# 한 명의 사람이 다수의 사람에게 연락이 가능한 경우 항상 다자 간 통화를 통해 동시에 전달한다.
# 연락이 퍼지는 속도는 항상 일정하다 (전화를 받은 사람이 다음사람에게 전화를 거는 속도는 동일).
# 비상연락망 정보는 사전에 공유되며 한 번 연락을 받은 사람에게 다시 연락을 하는 일은 없다.
# 예시에서의 3, 6, 11, 22번과 같이 연락을 받을 수 없는 사람도 존재할 수 있다.
# [입력]
# 입력의 첫 번째 줄에는 입력 받는 데이터의 길이와 시작점이 주어진다.
# 그 다음 줄에 입력받는 데이터는 {from, to, from, to, …} 의 순서로 해석되며 예시의 경우는 {2, 7, 11, 6, 6, 2, 2, 15, 15, 4, 4, 2, 4, 10, 7, 1, 1, 7, 1, 8, 1, 17, 3, 22}와 같다.
# 그런데 순서에는 상관이 없으므로 다음과 같이 주어진 인풋도 동일한 비상연락망을 나타낸다 (같은 비상연락망을 표현하는 다양한 인풋이 존재 가능하다).
#  {1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 4, 2}
# 다음과 같이 동일한 {from, to}쌍이 여러 번 반복되는 경우도 있으며, 한 번 기록된 경우와 여러 번 기록된 경우의 차이는 없다.
#  {1, 17, 1, 17, 1, 17, 3, 22, 1, 8, 1, 7, 7, 1, 2, 7, 2, 15, 15, 4, 6, 2, 11, 6, 4, 10, 11, 6, 4, 2}
# [출력]
#  #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다. 



for tc in range(10):
    case, begin = map(int,input().split())
    datas = list(map(int,input().split()))
    mycontact = [[0]*(max(datas)+1) for i in range(max(datas)+1)]
    for num in range(case//2):
        mycontact[datas[2*num]][datas[2*num+1]] = 1

    queue = []
    queue.append(begin)
    distance = [0] * (max(datas)+1)
    visited = [0] * (max(datas)+1)

    while queue != []:
        start = queue.pop(0)
        # visited[start] = 1

        for end in range(1,max(datas)+1):
            if visited[end] == 0 and mycontact[start][end] == 1:
                queue.append(end)
                visited[end] = 1
                distance[end] = distance[start] + 1

    result = []
    max_d = max(distance)
    for index_d in range(len(distance)):
        if distance[index_d] == max_d:
            result.append(index_d)

    print(f'#{tc+1} {max(result)}')
    # print(distance)

# 300 55
# 55 12 42 76 60 26 22 71 27 35 6 84 51 99 80 2 94 35 38 35 57 94 77 6 63 49 82 1 14 42 56 56 43 63 12 78 25 79 53 44 97 74 41 14 76 73 19 11 18 33 13 96 70 32 41 89 86 91 98 90 91 46 54 15 52 41 45 59 36 60 93 6 65 82 4 30 76 9 93 98 50 57 62 28 68 42 30 41 14 75 2 78 16 84 14 93 25 2 93 60 71 29 28 85 76 87 99 71 88 48 5 4 22 64 7 64 11 72 90 41 65 43 20 14 92 5 19 33 51 6 76 40 4 23 99 48 85 49 72 65 14 76 46 13 47 79 70 63 20 86 90 45 66 41 46 9 19 71 2 24 33 73 53 88 71 64 2 4 24 28 1 70 16 66 29 44 48 89 44 38 10 64 50 82 89 43 9 61 22 59 55 89 47 91 50 44 31 21 49 68 37 84 36 27 86 39 54 30 25 49 24 60 58 67 45 56 19 27 12 26 56 2 50 97 85 16 65 43 76 14 43 97 49 73 27 7 74 30 5 6 27 13 76 94 66 37 37 42 15 95 57 53 37 39 83 56 16 32 31 42 26 12 38 87 91 51 63 35 94 54 17 53 9 63 34 55 4 35 4 57 49 25 18 14 10 29 1 81 19 59 51 56 62 65 4 77 44 10 3 62 