import sys
sys.stdin = open("input.txt")

for tc in range(10):
    case = int(input())
    datas = []
    for number in range(case):
        datas.append(list(input().split()))

    sem = []
    num = []
    result = 1
    for i in range(case):
        if datas[i][1] == ['+','-','*','/']:
            sem.append(datas[i])
        elif datas[i][1].isdigit():
            num.append(datas[i])

    if len(sem)+1 != len(num):
        result = 0

    print('#{} {}'.format(tc+1, result))
