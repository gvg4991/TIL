신인택 Day14과제

1. 파스칼의 삼각형

   ```python
   T = int(input())
   for tc in range(1, T+1):
       N = int(input())
       Pas = [[0] * (N+1) for _ in range(N)]   # 출력값을 만들기 위한 배열을 만드는 것.
   
       print('#%d' % tc)
       for i in range(N):
           Pas[i][1] = 1
           for j in range(1, N+1):
               if i > 0:
                   Pas[i][j] = Pas[i-1][j-1] + Pas[i-1][j]
           for k in range(1, i+2):
               print(Pas[i][k], end=' ')
           print()
   ```

   

2. 미로-스택2(보충특강)

   ```python
   dy = [-1, 1, 0, 0]  # 상 하
   dx = [0, 0, -1, 1]  #       좌 우
   
   
   def load(x, y):     # Issafe 놓침. 범위를 벗어나 찾을 수 있는 위험, newY, newX를 설정해 주지 않아 반쪽자리 찾기를 실행했다.
       global found
       for move in range(4):
           newy = y + dy[move]
           newx = x + dx[move]
           if newx >= 0 and newx < N and newy >= 0 and newy < N:   # 미로 바깥으로 나가는지...
               if maze[newy][newx] == 3:       # 도착지점 만남
                   found = 1
               if maze[newy][newx] == 0:
                   maze[newy][newx] = -1
                   load(newx, newy)
                   maze[newy][newx] = 0
   
   
   T = int(input())
   
   for tc in range(1, T+1):
       N = int(input())
       maze = [list(map(int, input())) for _ in range(N)]
       # for i in range(N):
       #     print(maze[i])
       found = 0
       starty = 0
       startx = 0
   
       for y in range(N):      # 출발지점 찾기
           for x in range(N):
               if maze[y][x] == 2:
                   starty = y
                   startx = x
   
   
       load(startx, starty)
       print('#%d' % tc, found)
   ```

   

   