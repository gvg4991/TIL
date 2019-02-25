# 준혁이는 집에서 여자친구를 만나러 약속장소로 가려고 한다. 출발점과 도
# 착점을 포함하여 경유하는 지역 n개, 한 지역에서 다른 지역으로 가는 방법이 총 m
# 개이며 준혁이 집은 지역 1이고 약속장소는 지역 n이라고 할 때 집에서 약속장소까지 가는 최소 비용을
# 구하시오.
# 단, n은 10 이하, m은 30 이하, 그리고 한 지역에서 다른 지역으로 가는 데에 필
# 요한 비용은 모두 200 이하 양의 정수이며 한 지역에서 다른 지역으로 가는 어떠한
# 방법이 존재하면 같은 방법과 비용을 통해 역방향으로 갈 수 있다.
# 다음 그래프는 예를 보여준다.(단, 정점a->정점b로의 간선이 여러 개 있을 수 있으
# 며, 자기 자신으로 가는 정점을 가질 수도 있다.)
# 최소 비용이 드는 경로 : 1→3→5→7, 최소 비용 : 69+59+21=149
# 입력
# 첫 번째 줄에는 정점의 수 n과 간선의 수 m이 공백으로 구분되어 입력된다. 다음
# 줄부터 m개의 줄에 걸쳐서 두 정점의 번호와 가중치가 입력된다. (자기 간선, 멀티
# 간선이 있을 수 있다.)
# 출력
# 여자친구 만나러 가는 데 드는 최소 비용을 출력한다. 만약 갈 수 없다면 “-1”을 출력.

import sys
sys.stdin = open("day08_01.txt","r")

n,m = map(int,input().split())
mymap = [[0] * (n+1) for i in range(n+1)]
visited = [0] * (n+1)
# stack = [0] * 10
# top = -1

result = 0
min_cost = None
for mv in range(m):
    a,b,cost = map(int,input().split())
    mymap[a][b] = cost
    mymap[b][a] = cost
# print(mymap)

def find(start):
    global n, result, visited, min_cost
    visited[start] = 1
    for i in range(1,n+1):
        if mymap[start][i] != 0 and visited[i] == 0:
            if i != n:
                now = i
                result += mymap[start][i]
                find(now)
                # result -= mymap[start][i]
                visited[i] = 0

            else:
                result += mymap[start][i]
                if min_cost == None or min_cost > result:
                    min_cost = result
                    result -= mymap[start][i]
                    return

        elif i == n and mymap[start][i] == 0:
            # result -= mymap[start][i]
            return

find(1)
print(min_cost)