import sys
sys.stdin = open('input.txt')



def find(x):
    if x != parent[x]: #자신이랑 엄마가 같으면 즉, 자신이 엄마면
        return find(parent[x])
    else:
        return parent[x]

def union(x,y):
    x = find(x) #x엄마 찾기
    y = find(y)
    if x!=y:
        parent[y]=x #y의 엄마가 x가 됨



computer = int(input())
parent = [0]*(computer+1)
for make in range(1,computer+1):
    parent[make] = make
# print(parent)

for network in range(int(input())):
    p,c = map(int,input().split())
    union(p,c)

    virus = 0
    for target in range(2,computer+1): #1이 감염
        if find(1) == find(target):
            virus += 1

print(virus)

