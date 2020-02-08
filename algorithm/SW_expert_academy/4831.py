# A도시는 전기버스를 운행하려고 한다. 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.
# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.
# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.
# [예시]
# 다음은 K = 3, N = 10, M = 5, 충전기가 설치된 정류장이 1, 3, 5, 7, 9인 경우의 예이다.
# [입력]
# 첫 줄에 노선 수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
# 각 노선별로 K, N, M이 주어지고, 다음줄에 M개의 정류장 번호가 주어진다. ( 1 ≤ K, N, M ≤ 100 )
# [출력]
# #과 노선번호, 빈칸에 이어 최소 충전횟수 또는 0을 출력한다.

test = int(input())
for tc in range(test):
    case = list(map(int,input().split())) #[갈수있는거리, 종점 거리, 충전기수]
    datas = list(map(int,input().split())) #충전기 위치: [1,3,5,7,9]

    stop = [] #정류장 리스트
    for stop_i in range(case[1]+1+case[0]):
        stop += [stop_i] #[0,1,2,...,10]
        
    location=count=0 #버스위치=충전수=0
    result=None #while문 벗어나는 조건 변수
    while stop[location+case[0]]<case[1] and result!=False:
        k_area = [] #이동 가능 범위
        for k in range(1,case[0]+1):
            k_area += [stop[location + k]] #버스 위치 + 갈수있는 거리: [1,2,3]
        for data in datas[::-1]: # 충전기 위치를 거꾸로 가지고옴
            if data in k_area:
                location = data
                count += 1
                result = True
                break
            else:
                result = False
    
    if result == False:
        count = 0

    print(f'#{tc+1} {count}')
            
            

            
    
