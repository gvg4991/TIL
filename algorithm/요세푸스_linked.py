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


input = 41
head = None
for i in range(1,input+1):
    josephus(i)

p = head
while p:
    print(p.data)
    p = p.link
