import sys
sys.stdin = open("segment_tree.txt","r")

idt = [0]*(1<<5)
# print(idt)

data = list(map(int,input().split()))
howmany = len(data)

def update(a,b): #3,1
    where = base + a - 1
    idt[where] = b
    where >>= 1 #나누기 2

    while where:
        idt[where] = idt[where*2] + idt[where*2+1]
        where >>= 1


def rsq(start, end): #1,4
    start = start + base -1 #8
    end = end + base -1 #11
    sum = 0

    while start < end:
        if start&1: #홀수이면 (start%2==1)
            sum += idt[start] # 값을 sum에 더해주고
            start += 1
        if end%2 == 0:
            sum += idt[end]
            end -= 1
        start >>= 1 #부모한테 찾아감
        end >>= 1
    if start == end:
        sum += idt[start]
        # print(sum)
    return sum



base = 1
while base < howmany:
    base <<= 1 #곱하기 2
# print(base)

for now in range(base,howmany+base):
    idt[now] = data.pop(0) #base인덱스부터 데이터를 추가

for parent in range(base-1,-1,-1):
    idt[parent] = idt[parent*2] + idt[parent*2+1] #부모의 값은 자식의 두수 합

update(3,1)
ans = rsq(2,3)
print(ans)
print(idt)