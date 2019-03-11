class node:
    def __init__(self,data,link = None): #링크가 없으면 none
        self.data = data
        self.link = link


def enqueue(item):
    global head
    newnode = node(item) #node(1), data=1 -> node(2), data=2
    if head == None:
        head = newnode #node(1) 끝
    else: # head가 있으면(노드2가 들어올때)
        p = head # -> node(1)
        while p.link: #처음 들어오는 item은 p의 링크가 없다. -> 그다음 item은 그전 p의 link를 타고 들어가 link가 없을때 그 링크에 item을 넣어줌!
            p = p.link
        p.link = newnode #노드(데이터,링크) 만들기


def enpqueue(item):
    global head
    newnode = node(item)
    if head == None:
        head = newnode
    else:
        p = head
        while p.link:
            if p.link.data > newnode.data:
                newnode.link = p.link
                p.link = newnode
                break
            p = p.link
        p.link = newnode




# 데이터 받기
# node1 = node(1)
# node2 = node(2)
# node3 = node(3)
# node4 = node(4)
# node5 = node(5)
# node1.link = node2
# node2.link = node3
# node3.link = node4
# node4.link = node5

# node5 = node(5)
# node4 = node(4,node5)
# node3 = node(3,node4)
# node2 = node(2,node3)
# node1 = node(1,node2)
# print(node5.data)
# print(node4.link.data)


# print('-'*20)

#
# head = None
# enqueue(1) #노드1 만들기
# enqueue(2) #노드2 만들기
# enqueue(5)
# enqueue(4)
# enqueue(3)
# # print(head.data)
# # print(head.link.data)
# # print(head.link.link.data)
# # print(head.link.link.link.data)
# # print(head.link.link.link.link.data)
#
# # p = head
# # print(p.data)
# # print(p.link.data)
# # print(p.link.link.data)
# # print(p.link.link.link.data)
# # print(p.link.link.link.link.data)
#
# # head = node1 #헤드는 항상 선발대 고정(첫번째 데이터)
# p = head #p를 이동시킴
# while p: #p가 있는동안
#     print(p.data)
#     p = p.link


# print('-'*20)


# #함수 적용
head = None
enpqueue(1)
enpqueue(2)
enpqueue(5)
enpqueue(4)
enpqueue(3)
p = head #p를 이동시킴
while p: #p가 있는동안
    print(p.data)
    p = p.link





