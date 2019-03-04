# 숫자 체계가 우리와 다른 어느 행성이 있다. 아래는 이 행성에서 사용하는 0 ~ 9의 값을 순서대로 나타낸 것이다.
# "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
#  0 ~ 9 의 값을 나타내는 단어가 섞여 있는 문자열을 받아 작은 수부터 차례로 정렬하여 출력하는 프로그램을 작성하라.
# 예를 들어 입력 문자열이 "TWO NIN TWO TWO FIV FOR" 일 경우 정렬한 문자열은 "TWO TWO TWO FOR FIV NIN" 이 된다.
# [입력]
# 입력 파일의 첫 번째 줄에는 테스트 케이스의 개수가 주어진다.
# 그 다음 줄에 #기호와 함께 테스트 케이스의 번호가 주어지고 공백문자 후 테스트 케이스의 길이가 주어진다.
# 그 다음 줄부터 바로 테스트 케이스가 주어진다. 단어와 단어 사이는 하나의 공백으로 구분하며, 문자열의 길이 N은 100≤N≤10000이다.
# [출력]
#  #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 정렬된 문자열을 출력한다. 

test = int(input())
for tc in range(test):
    case, n = map(str,input().split()) # #1, 7041
    n = int(n)
    datas = list(map(str,input().split()))
    # idx = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

    list0 = []
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    list5 = []
    list6 = []
    list7 = []
    list8 = []
    list9 = []
    for data in datas:
        if data == "ZRO":
            list0.append(data)
        elif data == "ONE":
            list1.append(data)
        elif data == "TWO":
            list2.append(data)
        elif data == "THR":
            list3.append(data)
        elif data == "FOR":
            list4.append(data)
        elif data == "FIV":
            list5.append(data)
        elif data == "SIX":
            list6.append(data)
        elif data == "SVN":
            list7.append(data)
        elif data == "EGT":
            list8.append(data)
        elif data == "NIN":
            list9.append(data)

    l0 = ' '.join(list0)
    l1 = ' '.join(list1)
    l2 = ' '.join(list2)
    l3 = ' '.join(list3)
    l4 = ' '.join(list4)
    l5 = ' '.join(list5)
    l6 = ' '.join(list6)
    l7 = ' '.join(list7)
    l8 = ' '.join(list8)
    l9 = ' '.join(list9)

    print(case)
    print('{} {} {} {} {} {} {} {} {} {}'.format(l0,l1,l2,l3,l4,l5,l6,l7,l8,l9))