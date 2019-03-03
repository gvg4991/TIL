# 원형 금속 막대를 가장 길게 연결하고자 한다. 원형 금속 막대는 한 쪽 면에 수나사와 다른 쪽에 암나사로 이루어져 있다.
# 수나사와 암나사는 굵기가 서로 다르다. 아래 그림에서 수나사의 굵기는 3을 암나사의 굵기는 4를 나타내고 있다.
# 이후 나사의 굵기를 수나사의 굵기 x 암나사의 굵기로 표현한다. 연결은 +로 표현한다.
# 이와 같은 원형 금속 막대를 연결하기 위해서는 수나사의 굵기와 암나사의 굵기가 서로 일치해야 한다.
# 예를 들어 두 개의 원형 금속 막대 3x4와 4x5가 있을 때 3x4+4x5로 연결해야 연결되며 4x5+3x4로 연결하면 연결되지 않는다.
# 수나사와 암나사의 크기가 서로 다른 여러 개의 원형 금속 막대를 가장 많이 연결하려고 한다.
# 어떤 순서로 연결해야 가장 많이 연결하는지를 찾는 프로그램을 작성하시오.
# [입력]
# 맨 첫 줄에는 테스트 케이스의 개수가 주어진다.
# 그리고 테스트 케이스가 각 라인에 주어진다. 각 테스트 케이스는 2줄로 구성되며, 첫 줄에는 원형 금속 막대의 개수 n이 주어지고, 다음 줄에는 2n개의 수가 주어진다. 
# 숫자는 공백으로 구분한다. 앞에서부터 2개씩 하나의 원형 금속 막대의 수나사 굵기와 암나사 굵기를 의미한다.
# [출력]
# 각 테스트 케이스 각각에 대한 답을 출력한다.
# 각 줄은 ‘#x’로 시작하고 공백을 하나 둔 다음, 각 테스트 케이스에 주어진 수열로부터 가장 많이 연결하기 위한 원형 금속 막대의 수나사 굵기와 암나사 굵기를 순서대로 출력한다. 


def screw(start):
    result.append(sunasa[start])

    if amnasa[start] in sunasa:
        result.append(amnasa[start])
        new = sunasa.index(amnasa[start])
        screw(new)
        return
    else:
        result.append(amnasa[start])
        return
    
    new = sunasa.index(amnasa[start])
    screw(new)
    
test = int(input())
for tc in range(test):
    case = int(input())
    datas = list(map(int,input().split()))

    sunasa = []
    amnasa = []
    for num in range(case):
        sunasa.append(datas[2*num])
        amnasa.append(datas[2*num+1])

    begin = 0
    for case_i in range(case):
        if not sunasa[case_i] in amnasa:
            begin = case_i

    result = []
    screw(begin)

    ans = ' '.join(map(str,result))
    print(f'#{tc+1} {ans}')


    # sunasa = []
    # amnasa = []
    # for num in range(len(datas)):
    #     if num % 2 == 0:
    #         sunasa += [datas[num]]
    #     else:
    #         amnasa += [datas[num]]

    # ind = []
    # for am_i in range(len(amnasa)):
    #     for su_i in range(len(sunasa)):
    #         if amnasa[am_i] == sunasa[su_i]:
    #             ind += [[am_i,su_i]]
    # print(ind)
    
#------------------------------------------------------------

    # nasa = []
    # for num in range(len(datas)):
    #     if num % 2 == 0:
    #         nasa += [[datas[num],datas[num+1]]]
    # print(nasa)

    # result = []
    # for am in nasa:
    #     for su in nasa:
    #         result += am[1]
    #         if am[1] == su[0]:
    #             result += su[0]

#-------------------------------------------------------------
    
# nut = [[0] * len(datas)/2+1 for i in range(len(datas)/2+1)]

        

