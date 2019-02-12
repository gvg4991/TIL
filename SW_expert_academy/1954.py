# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
# 다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.
# [예제]
# N이 3일 경우,
# N이 4일 경우,
# [제약사항]
# 달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
# [입력]
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스에는 N이 주어진다.
# [출력]
# 각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
#  (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.) 

# a=int(input())
# arr=[]
# for ai in range(a):
#     arr.append([None]*a)
# count=0
# top=left=0
# bottom=right=a-1

# while top<=bottom or left<=right and count < a**2:
#     # left -> right
#     for i in range(left,right):
#         if count == a**2:
#             break
#         arr[left][i]=count
#         count+=1
#     # top -> bottom
#     for i in range(top,bottom):
#         if count == a**2:
#             break
#         arr[i][right]=count
#         count+=1
#     #  right -> left
#     for i in range(right,left,-1):
#         if count == a**2:
#             break
#         arr[bottom][i]=count
#         count+=1
#     # bottom -> top
#     for i in range(bottom,top,-1):
#         if count == a**2:
#             break
#         arr[i][left]=count
#         count+=1

#     if top == bottom == right == left:
#         arr[left][right]=count
    
#     left+=1
#     right+=1
#     top+=1
#     bottom+=1

# for ai in range(a):
#     for aj in range(a):
#         print(arr[ai][aj],end=" ")
#     print("\n")

# ----------------------------------------------------------------------

# 유림누닝
# for k in range(int(input())):
#     n=int(input())
#     a=[[0]*n for i in range(n)]
#     for i in range(n):
#         for j in range(n):
#             g=min(i,j,n-1-i,n-1-j)
#             x=1+4*g*(n-g)
#             y=i+j-2*g
#             if i>j:
#                 a[i][j]=4*(n-1-2*g)-y+x           
#             else:
#                 a[i][j]=y+x
#     print(f'#{k+1}')
#     for i in a:
#         print(*i)
 
# 재형형닝
# n = int(input())
 
# for tc in range(1,n+1):
#     num = int(input())
#     nlist = [[0]*(num+2) for i in range(num+2)]
     
#     for i in range (1,num+1):
#         for j in range(1,num+1):
#             nlist[i][j] = 100
             
#     i = 1
#     j = 1
#     direction = 'right'
#     for n in range (1,num**2+1):
#         nlist[i][j] = n
        
#         if direction == 'right':
#             if nlist[i][j+1] != 100:
#                 direction = 'down'
#                 i+=1
#             else:
#                 j+=1
 
#         elif direction == 'left':
#             if nlist[i][j-1] != 100:
#                 direction = 'up'
#                 i-=1
#             else:
#                 j-=1
#         elif direction == 'up':
#             if nlist[i-1][j] != 100:
#                 direction = 'right'
#                 j+=1
#             else:
#                 i-=1
#         elif direction == 'down':
#             if nlist[i+1][j] != 100:
#                 direction = 'left'
#                 j-=1
#             else:
#                 i+=1
         
#     print(f'#{tc}')
#     for i in range (1,num+1):
#         for j in range(1,num+1):
#             print(nlist[i][j],end=" ")
#             if j%(num) == 0:
#                 print()


#-------------------------------------------------------------------------

# a=int(input())
# for ai in range(a):

#     ARR=[]
#     b=int(input())
#     for bi in range(b+2):
#         arr=[]
#         for bi in range(b+2):
#             arr.append(0)
#         ARR.append(arr)
#     # print(ARR)
#     for by in range(1,b+1):
#         for bx in range(1,b+1):
#             ARR[by][bx]=1
#     # print(ARR)


a=int(input())
for ai in range(a):

    b=int(input())
    arr=[]
    for bi in range(b+2):
        arr.append([0]*(b+2))

    for by in range(1,b+1):
        for bx in range(1,b+1):
            arr[by][bx]=1
    
    # for i in range(1,b**2+1):
    #     if arr[by][bx] != 0:

    