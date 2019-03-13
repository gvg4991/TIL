homework

2/14

* baby_ gin

  ```python
  Data = [1,1,1,2,5,7]
  
  print(Data)
  
  count_array=[0]*(max(Data)+1)
  
  for i in Data:
      count_array[i]+=1
  
  # print(count_array)
  
  for i in range(len(count_array)):
      if count_array[i]==3:
          count_array[i]-=3
      elif count_array[i]==6:
          count_array[i]-=6
  
  for i in range(len(count_array)-2):
      if count_array[i]>=1 and count_array[i+1]>=1 and count_array[i+1]:
          count_array[i]-=1
          count_array[i+1]-=1
          count_array[i+2]-=1
  
  # print(count_array)
  
  sum=0
  for i in count_array:
      sum+=i
  
  if sum==0:
      print('babygin!')
  else:
      print('not babygin')
  ```

* counting_sort

  ```python
  Data = [4,6,1,2,8,1,1,0,2,0,3]
  
  print(Data)
  
  count_array=[0]*(max(Data)+1)
  
  for i in Data:
      count_array[i]+=1
  
  # print(count_array)
  
  for i in range(len(count_array)-1):
      count_array[i+1]=count_array[i]+count_array[i+1]
  
  temp=[0]*len(Data)
  # print(Data)
  
  for i in range(len(Data)-1, -1, -1):
      count_array[Data[i]] -= 1
      temp[count_array[Data[i]]] = Data[i]
  
  print(temp)
  ```

* permutation

  ```python
  import sys
  
  sys.stdin = open('permutation.txt', 'r')
  
  Data = list(map(int, input().split()))
  
  print(Data)
  
  cand1=0
  for i in range(len(Data)-1):
      if Data[i]<Data[i+1]:
          cand1=i
  
  cand2=len(Data)-1
  while Data[cand1]>Data[cand2]:
      cand2-=1
  
  Data[cand1],Data[cand2]=Data[cand2],Data[cand1]
  Data[cand1+1:]=Data[:cand1:-1]
  print(Data)
  ```

  

2/20

- ladder비재귀

  ```python
  # ladder 비재귀
  import sys
  sys.stdin=open('ladder.txt','r')
  
  for test in range(10):
      tc = int(input())
      ladder = [list(map(int, input().split())) for i in range(100)]
      # print(ladder)
      dx = [-1, 1, 0]
      dy = [0, 0, -1]
      y = 99
      x = 0
      result=0
      while x < 100:
          temp = x
          visited = [[0] * 100 for i in range(100)]
          if ladder[y][x] == 2:
              while y > 0 :
                  for dir in range(3):
                      if y + dy[dir] < 0 or x + dx[dir] < 0 or y + dy[dir] > 99 or x + dx[dir] > 99:
                          continue
                      if ladder[y + dy[dir]][x + dx[dir]] == 1 and not visited[y + dy[dir]][x + dx[dir]]:
                          y = y + dy[dir]
                          x = x + dx[dir]
                          visited[y][x] = True
                          break
              result=x
          x = temp + 1
      print('#{} {}'.format(tc,result))
  ```

  

2/21

- 괄호검사

  ```python
  # 괄호검사
  import sys
  
  sys.stdin=open('괄호검사.txt','r')
  
  T=int(input())
  for tc in range(1,T+1):
      data=input()
      N=len(data)
      stack = []
      # print(data)
  
      Info = [0] * 128  # Char: 1byte, ASCII: 7bit
      Info[ord(')')] = '('
      # Info[ord(']')] = '['
      Info[ord('}')] = '{'
      # Info[ord('>')] = '<'
  
      top=-1
      for i in range(N):
  
          if data[i] == '(' or data[i] == '{':
              stack.append(data[i])
              top += 1
          else:
              if top >= 0:
                  if stack[top] == Info[ord(data[i])]:
                      stack.pop()
                      top -= 1
                  elif (data[i] == '}' or data[i] == ')') and data[i] not in stack:
                      top=0
                      break
              else:
                  if data[i] == ')' or data[i] == '}':
                      top = 0
                      break
      print(f'#{tc}', end=' ')
      if top==-1:
          print(1)
      else:
          print(0)
  ```

- 그래프경로

  ```python
  # 그래프경로
  import sys
  sys.stdin=open('4871.txt', 'r')
  
  T=int(input())
  for tc in range(1,T+1):
      v, e=map(int,input().split())
      matrix = [[0] * (v + 1) for i in range(v + 1)]
      for i in range(e):
          # l.append(list(map(int,input().split())))
          a,b=map(int,input().split())
          matrix[a][b]=1
      # print(f'#{tc}')
      # print(matrix)
      S,G=map(int,input().split())
  
      def find(start,end):
          result=0
          for x in range(len(matrix)):
              temp=matrix[start]
              if matrix[start][x]==1:
                  if x==end:
                      return 1
                  if find(x,end)==1:
                      return 1
  
      result=find(S,G)
      if result==1:
          print(f'#{tc} {result}')
      else:
          print(f'#{tc} 0')
  ```

- 반복문자지우기

  ```python
  # 반복문자 지우기
  import sys
  sys.stdin=open('4873.txt','r')
  
  T=int(input())
  
  for tc in range(1,T+1):
      s=input()
      # print(s)
  
      top=-1
      new_s=[]
      for i in range(len(s)):
          if new_s==[]:
              new_s.append(s[i])
              top+=1
          else:
              if s[i]==new_s[top]:
                  new_s.pop()
                  top-=1
              else:
                  new_s.append(s[i])
                  top+=1
  
      print(f'#{tc} {len(new_s)}')
  ```

- 작업순서

  ```python
  import sys
  sys.stdin=open('작업순서.txt','r')
  
  for tc in range(1,11):
      print('#{}'.format(tc))
      v, e = list(map(int, input().split()))
      data=list(map(int,input().split()))
      # print(data)
      node = [0] * (v + 1)
      myMap=[[0]*(v+1) for i in range(v+1)]
      for i in range(len(data)//2):
          y=data[i*2]
          x=data[i*2+1]
          node[x]+=1
          myMap[y][x]=1
      # print(myMap)
      visited=[0]*(v+1)
      que=[0]*(v+1)
      top=rear=-1
      # print(node)
  
      result=[]
      while node!=[0]*(v+1):
          for i in range(1, v + 1):
              if node[i] == 0 and not visited[i]:
                  rear += 1
                  que[rear] = i
                  break
          while top!=rear:
              top += 1
              y = que[top]
              result.append(y)
              visited[y]=1
              for x in range(v+1):
                  if myMap[y][x]==1 and not visited[x]:
                      if node[x]<2:
                          rear += 1
                          que[rear] = x
                      node[x]-=1
      print(result)
  ```

- 종이붙이기

  ```python
  # 종이붙이기
  import sys
  
  sys.stdin=open('4869.txt','r')
  
  T=int(input())
  for tc in range(1,T+1):
      n=int(input())
  
      def paper(x):
          while x>=30:
              return paper(x-10)+paper(x-20)*2
          if x==20:
              return 3
          elif x==10:
              return 1
  
      result=paper(n)
  
      print(f'#{tc} {result}')
  ```

  

2/22

- forth

  ```python
  import sys
  
  sys.stdin=open('forth.txt','r')
  
  T=int(input())
  for tc in range(1,T+1):
      data=list(input().split())
      stk=[]
      for i in range(len(data)):
          if data[i]=='+' or data[i]=='-' or data[i]=='*' or data[i]=='/':
              if len(stk) < 2:
                  result = 'error'
                  break
              else:
                  n1 = stk.pop()
                  n2 = stk.pop()
                  if data[i] == '+':
                      stk.append(n2 + n1)
                  elif data[i] == '*':
                      stk.append(n2 * n1)
                  elif data[i] == '/':
                      stk.append(n2 / n1)
                  else:
                      stk.append(n2 - n1)
          elif data[i]=='.':
              if len(stk) != 1:
                  result = 'error'
                  break
              result = stk.pop()
              if round(result) == result:
                  result = round(result)
              break
          else:
              stk.append(float(data[i]))
  
      print(f'#{tc} {result}')
  ```

- 계산기

  ```python
  import sys
  
  sys.stdin=open('계산기.txt','r')
  
  for tc in range(1,11):
      # print(f'#{tc}')
      n = int(input())
      # print(n)
      data=list(input())
      # print(data)
      opeStk=[]
      post=[]
      for i in data:
          if i.isnumeric():
              post.append(i)
          else:
              if i=='(':
                  opeStk.append(i)
              elif i=='*':
                  if len(opeStk)>0:
                      if opeStk[len(opeStk)-1]=='*':
                          value=opeStk.pop()
                          post.append(value)
                  opeStk.append(i)
              elif i=='+':
                  if len(opeStk)>0:
                      if opeStk[len(opeStk)-1]=='+' or opeStk[len(opeStk)-1]=='*':
                          value=opeStk.pop()
                          post.append(value)
                  opeStk.append(i)
              else:
                  while opeStk[len(opeStk)-1]!='(':
                      value=opeStk.pop()
                      post.append(value)
                  opeStk.pop()
  
      stk=[]
      for i in post:
          if i.isnumeric():
              stk.append(int(i))
          else:
              n2=stk.pop()
              n1=stk.pop()
              if i=='+':
                  stk.append(n1+n2)
              else:
                  stk.append(n1*n2)
      result=stk.pop()
      print(f'#{tc} {result}')
  ```

- 미로dfs

  ```python
  import sys
  sys.stdin=open('미로dfs.txt','r')
  
  T=int(input())
  for tc in range(1,T+1):
      n=int(input())
      miro=[list(map(int,input())) for i in range(n)]
      # print(miro)
  
      dx=[0,-1,0,1]
      dy=[-1,0,1,0]
  
      for y in range(n):
          for x in range(n):
              if miro[y][x]==2:
                  start_y=y
                  start_x=x
  
      def isSafe(y,x):
          if y>=0 and y<n and x>=0 and x<n:
              return True
          else:
              return False
  
      def dfs(y, x):
          global result
          miro[y][x]=1
          for dir in range(4):
              if isSafe(y+dy[dir],x+dx[dir]):
                  if miro[y+dy[dir]][x+dx[dir]] == 0:
                      dfs(y+dy[dir], x+dx[dir])
                  elif miro[y+dy[dir]][x+dx[dir]]==3:
                      result=1
                      return
      result = 0
      dfs(start_y,start_x)
      print('#{} {}'.format(tc, result))
  ```

  

2/25

- 미로의 거리

  ```python
  # 미로의 거리
  import sys
  sys.stdin=open('미로의거리.txt','r')
  
  dx=[0,-1,0,1]
  dy=[-1,0,1,0]
  
  T=int(input())
  for tc in range(1,T+1):
      n=int(input())
      maze = [[int(x) for x in input()] for _ in range(n)]
  
      for y in range(n):
          for x in range(n):
              if maze[y][x]==3:
                  goal=(y,x)
              elif maze[y][x]==2:
                  start=(y,x)
  
      que=[0]*(n**2)
      front=rear=-1
      visited=[[0]*n for i in range(n)]
      distance = [[0] * n for i in range(n)]
  
      def Maze(y,x):
          global front,rear,goal
          rear+=1
          que[rear]=(y,x)
          visited[y][x] = True
          while front!=rear:
              front+=1
              cor=que[front]
              y=cor[0]
              x=cor[1]
              for dir in range(4):
                  newY = y + dy[dir]
                  newX = x + dx[dir]
  
                  if newY<0 or newY>n-1 or newX<0 or newX>n-1:
                      continue
                  if not visited[newY][newX]:
                      if maze[newY][newX] == 0:
                          rear+=1
                          que[rear]=(newY,newX)
                          visited[newY][newX]=True
                          distance[newY][newX]=distance[y][x]+1
                      elif maze[newY][newX]==3:
                          return distance[y][x]
          return 0
  
      print(f'#{tc} {Maze(start[0],start[1])}')
  ```

- 피자굽기

  ```python
  # 피자굽기
  import sys
  sys.stdin=open('피자굽기.txt','r')
  
  T=int(input())
  for tc in range(1,T+1):
      size, n=map(int,input().split())
      pizza=list(map(int,input().split()))
  
      top=-1
      rear=len(pizza)-1
      oven=[]
      for i in range(size):
          top+=1
          oven.append((i+1,pizza[top]))
      # print(oven)
  
      while len(oven)!=1:
          # for i in range(len(oven)):
          p=oven.pop(0)
          if p[1]//2==0:
              if top!=rear:
                  top+=1
                  oven.append((top+1,pizza[top]))
          else:
              oven.append((p[0],p[1]//2))
      last_pizza=oven.pop()
      print('#{} {}'.format(tc,last_pizza[0]))
  ```

  

2/26

* contact

  ```python
  import sys
  sys.stdin=open('contact.txt','r')
  
  T=10
  for tc in range(1,T+1):
      print('# {}'.format(tc))
      cont=[[0]*101 for i in range(101)]
      n, begin=list(map(int,input().split()))
      print(n)
      print(begin)
      data=list(map(int,input().split()))
      print(data)
      for i in range(n//2):
          start=data[i*2]
          end=data[i*2+1]
          cont[start][end]=1
      for j in cont:
          print(j)
  
      que=[0]*101
      visited=[0]*101
      top=-1
      rear=-1
      def contact(begin):
          global top,rear,cont
          rear+=1
          que[rear]=begin
          visited[begin]=True
          while True:
              top+=1
              y=que[top]
              for x in range(101):
                  if cont[y][x]==1:
                      rear+=1
                      que[rear]=x
  
      contact(begin)
  ```

  

* 수도요금

  ```python
  import sys
  sys.stdin=open('수도요금.txt','r')
  
  T=int(input())
  for tc in range(1,T+1):
          w=list(map(int,input().split()))
          P=w[0]
          Q=w[1]
          R=w[2]
          S=w[3]
          W=w[4]
  
          a_bill=P*W
          if W<=R:
              b_bill=Q
          else:
              b_bill=Q+(W-R)*S
  
          if a_bill<=b_bill:
              print(f'#{tc} {a_bill}')
          else:
              print(f'#{tc} {b_bill}')
  ```



2/27

* atoi

  ```python
  # 문자열->숫자 변환
  def atoi(s):
      n=0
      for i in range(len(s)):
          if s[i]=='A' or s[i]=='B' or s[i]=='C' or s[i]=='D' or s[i]=='E' or s[i]=='F':
              n+=16**(len(s)-1-i)*(ord(s[i])-55)
          else:
              n+=16**(len(s)-1-i)*(ord(s[i])-48)
      return n
  print(atoi('42FB'))
  ```

* itoa

  ```python
  # 숫자->문자열 변환
  def itoa(n):
      s=''
      while True:
          s=chr(n%10+48)+s
          n=n//10
          if n==0:
              return s
  
  print(itoa(123))
  ```

* reverse

  ```python
  # 연습문제1 문자열 뒤집기
  
  s='algorithm'
  l=[]
  for i in s:
      l.append(i)
  length=len(l)
  rep=length//2
  
  for i in range(rep):
      l[i],l[length-1-i]=l[length-1-i],l[i]
  
  new_s=''.join(l)
  print(new_s)
  ```

  

