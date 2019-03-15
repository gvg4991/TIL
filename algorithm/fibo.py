#피보나치
#빅오는 n (속도는 n)
# fibo = [-1]*101
# fibo[0] = 0
# fibo[1] = 1
#
# for now in range(2,101):
#     fibo[now] = fibo[now-1] + fibo[now-2]
#
# print(fibo[100])



#메모아이제이션
#한번 갔다온건 어떤 배열에다가 적어! 그리고 다시 가지마
fibo = [-1]*101
fibo[0] = 0
fibo[1] = 1

def getsome(num):
    #basecase
    if fibo[num] == -1:
         fibo[num] = getsome(num-1) + getsome(num-2)
         return fibo[num]
    else:
        return fibo[num]

print(getsome(100))