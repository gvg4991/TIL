test = int(input())
for tc in range(test):

    pizza_q = []
    fire_q = []
    n,m = map(int,input().split())
    datas = list(map(int,input().split()))
    for index in range(len(datas)):
        pizza_q += [[index+1,datas[index]]] #[ [피자번호,치즈량],[,],[,] ]
    # print(pizza_q)
    for n_i in range(n):
        fire_q += [[1,0]]

    ing = -1
    while fire_q != []:
        ing += 1 # 0-1-2-3-4-5-6
        i = ing % n # 0-1-2-0-1-2

        if pizza_q != []:
            if fire_q[i][1] == 0:
                p = pizza_q.pop(0) 
                fire_q[i] = p

        else:
            if len(fire_q) == 1:
                result = fire_q.pop(0)
            elif fire_q[i] == 0:
                fire_q.pop(i)

        fire_q[i][1] = fire_q[i][1]//2

    print(f'#{tc+1} {result}')

    



