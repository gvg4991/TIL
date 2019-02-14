import sys

#최대값 찾기
sys.stdin = open('day01_01.txt','r')
Data = list(map(int,input().split()))

l = None
for i in Data:
    if l == None or l < i:
        l = i
print(l)

# 강사님
# howmany = len(Data)
# max = -1
# maxindex = -1
# for now in range(howmany):
#     if max < Data[now]:
#         max = Data[mow]
#         maxindex = now

# ----------------------------------------------------------------------------------------------------------------------
# 최대 낙상거리(막대그래프 90도회전 후 중력!)
sys.stdin = open('day01_02.txt','r')
data = list(map(int,input().split()))

# 틀린코딩!
mv = None
emp=ind=0
for i in data:
    if mv == None or mv < i: #최대값 찾기
        mv = i
        emp += 1 #같은 값을 제외한 데이터의 갯수
        ind += 1 #최대값까지의 데이터 갯수!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
    elif mv > i:
        emp += 1
print(emp-ind) #빈칸의 수 - 자신 데이터 이전

# 강사님
# size=len(data)
# max=0
# for now in range(size):
#     jumpcnt = size-now+1
#     for next in range(now+1,size):
#         if data[next] >= data[now]:
#             jumpcnt -= 1
#     if jumpcnt > max:
#         max = jumpcnt
# print(jumpcnt)

# ----------------------------------------------------------------------------------------------------------------------
# 넥스트 퍼뮤테이션
sys.stdin = open('day01_03.txt','r')
data03 = list(map(int,input().split()))

choice = None
cand1 = None
for i in range(len(data03)-1):
    if data03[i] < data03[i+1]:
        choice = i
# print(data03[choice])

for candi in range(len(data03)-1,choice,-1):
    if data03[choice] < data03[candi]:
        cand1 = candi
        break
data03[choice],data03[cand1] = data03[cand1],data03[choice]
# print(data03)

data03[choice+1:] = data03[len(data03):choice:-1]
print(data03)


#강사님


# ----------------------------------------------------------------------------------------------------------------------
# 버블솔트
sys.stdin = open('day01_04.txt','r')
data04 = list(map(int,input().split()))

# # 틀린코딩
# for i in range(len(data04)-1):
#     if data04[i] > data04[i+1]:
#         data04[i],data04[i+1] = data04[i+1],data04[i]
# print(data04)


# # 강사님
# all = len(data04)
# for now in range(all-1):
#     for next in range(now+1,all):
#         if data04[next] < data04[now]:
#             data04[now], data04[next] = data04[next], data04[now]
# print(data04)



# ----------------------------------------------------------------------------------------------------------------------
#카운팅솔트
sys.stdin = open('day01_05.txt','r')
data05 = list(map(int,input().split()))

empty=[0]*len(data05)
cnt=[0]*(max(data05)+1)
count=0
counts=[]

for i in data05:
    cnt[i]+=1

for ei in cnt:
    count+=ei
    counts+=[count]

for i in data05:
    counts[i]-=1
    empty[counts[i]]+=i

print(empty)


# ----------------------------------------------------------------------------------------------------------------------
# 베이비진
sys.stdin = open('day01_06.txt','r')
data06 = list(map(int,input().split()))

empty=[0]*len(data06)
cnt=[0]*(max(data06)+1)

for i in data06:
    cnt[i]+=1
# print(cnt)

for cnt_triple in range(len(cnt)):
    if cnt[cnt_triple]>=6:
        cnt[cnt_triple]-=6
    elif cnt[cnt_triple]>=3:
        cnt[cnt_triple]-=3
# print(cnt)

for cnt_run in range(len(cnt)-2):
        if cnt[cnt_run]>=2 and cnt[cnt_run+1]>=2 and cnt[cnt_run+2]>=2:
                cnt[cnt_run]-=2
                cnt[cnt_run+1]-=2
                cnt[cnt_run+2]-=2
        elif cnt[cnt_run]>=1 and cnt[cnt_run+1]>=1 and cnt[cnt_run+2]>=1:
                cnt[cnt_run]-=1
                cnt[cnt_run+1]-=1
                cnt[cnt_run+2]-=1
# print(cnt)

if sum(cnt) == 0:
        print(True)
else:
        print(False)
        

