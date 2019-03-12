class node:
    def __init__(self,data,link = None): #링크가 없으면 none
        self.data = data
        self.link = link

def josephus(item):
    global head
    newnode = node(item)
    if head == None:
        head = newnode
    else:
        p = head # -> node(1)
        while p.link:
            p = p.link
        p.link = newnode


#노드 만들기
input = 41
head = None
for i in range(1,input+1):
    josephus(i)

p = head
while p.link:
    # print(p.data)
    p = p.link
p.link = head #반복할수 있도록 돌려줌 (마지막 노드의 링크에 헤드를 넣어줌)

# print(p.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.link.data)


#요세푸스
people = input
p = head
while people > 2:
    people -= 1
    p.link.link = p.link.link.link #세번째 사람 건너뜀
    p = p.link.link #건너뛴 네번째사람한테로 감

for i in range(2): #데이터 출력
    print(p.data)
    p = p.link