# 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면
# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,
# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
# ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
# [입력]
# 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
# 다음 줄부터 각 테스트 케이스가 주어진다.
# [출력]
# 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
#  (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.) 

# c=int(input())
# for b in range(c):
#     a=str(input())
#     y=a[0:4]
#     m=a[4:6]
#     d=a[6:8]
#     if 1<=int(m)<=12:
#         if int(m) in map(int,[1,3,5,7,8,10,12]):
#             if int(d)<=31:
#                 print(f'#{b+1} {y}/{m}/{d}')
#             else:
#                 print(f'#{b+1} -1')
#         elif int(m) in map(int,[4,6,9,11]):
#             if int(d)<=30:
#                 print(f'#{b+1} {y}/{m}/{d}')
#             else:
#                 print(f'#{b+1} -1')
#         elif int(m) == int(2):
#             if int(d)<=28:
#                 print(f'#{b+1} {y}/{m}/{d}')
#             else:
#                 print(f'#{b+1} -1')
#     else:
#         print(f'#{b+1} -1')

for c in range(int(input())):
    a=str(input())
    y=a[0:4]
    m=a[4:6]
    d=a[6:8]
    M=int(m)
    D=int(d)
    t=f'#{c+1} {y}/{m}/{d}'
    f=f'#{c+1} -1'
    if 1<=M<=12:
        if M in map(int,[1,3,5,7,8,10,12]):
            print(t) if 0<D<=31 else print(f)
        elif M in map(int,[4,6,9,11]):
            print(t) if 0<D<=30 else print(f)
        elif M == int(2):
            print(t) if 0<D<=28 else print(f)
    else:
        print(f)


#print(f'{y}/{m}/{d}/')



# for b in range(a):
#     x,y=map(int,input().split())