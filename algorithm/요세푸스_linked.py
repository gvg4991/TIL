class node:
    def __init__(self,data,link = None): #링크가 없으면 none
        self.data = data
        self.link = link


input = 41

for i in range(input,-1,-1):
    node(i)
