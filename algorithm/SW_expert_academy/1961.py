import sys
sys.stdin = open("input.txt")


# test = int(input())
# for tc in range(test):
#     n = int(input())
#     datas = []
#     for case in range(n):
#         datas.append(list(map(int,input().split())))
#
#     print('#{}'.format(tc+1))
#     col0 = []
#     col1 = []
#     col2 = []
#     col0 = list(map(list,zip(*datas[::-1])))
#     col1 = list(map(list,zip(*col0[::-1])))
#     col2 = list(map(list,zip(*datas)))[::-1]
#     print(col0)
#     print(col1)
#     print(col2)
#
#     ans = []
#     for i in range(n):
#         ans.append(col0[i])
#         ans.append(col1[i])
#         ans.append(col2[i])
#     print(ans)
#
#     ans0 = ''
#     for i in range(len(ans)//3):
#         ans0 += ''.join(map(str,ans[0:3][0:n]))
#
#     print(*ans0)



    # col0 = []
    # col1 = []
    # col2 = []
    # col3 = []
    # col4 = []
    # col5 = []
    # col6 = []
    # col7 = []
    #
    # col0 = list(map(list,zip(*datas))) #전치행렬
    # col1 = datas[::-1] #역순
    # col2 = list(map(list,zip(*datas)))[::-1]
    # col3 = list(map(list,zip(*datas[::-1])))
    # col4 = list(map(list,zip(*col0)))[::-1]
    # col5 = list(map(list,zip(*col0[::-1])))
    # col6 = list(map(list,zip(*col1)))[::-1]
    # col7 = list(map(list,zip(*col1[::-1])))
    #
    # print(col0)
    # print(col1)
    # print(col2)
    # print(col3)
    # print(col4)
    # print(col5)
    # print(col6)
    # print(col7)






































T = int(input())
for t in range(T):
    N = int(input())
    total_data = []
    for n in range(N):
        data = list(input().split())
        total_data.append(data)

    one_total_data = list(map(list, zip(*total_data[::-1])))
    two_total_data = list(map(list, zip(*one_total_data[::-1])))
    three_total_data = list(map(list, zip(*two_total_data[::-1])))
    print(one_total_data)
    print(two_total_data)
    print(three_total_data)

    print('#{}'.format(t + 1))
    for n in range(N):
        print(*one_total_data[n], sep='', end=' ') #갈호제거, 사이간격, 프린트간간격
        print(*two_total_data[n], sep='', end=' ')
        print(*three_total_data[n], sep='', end=' ')
        print()
