# D17

1. Insertion Sort

```python
data = [3,9,1,6,7,0,4,9,5,5]

for j in range(1,len(data)):
    i = j-1
    while i > -1:
        if data[i] > data[j]:
            data[i], data[j] = data[j], data[i]
            j-=1
            i-=1
        else:
            break
print(data)
```



2. Merge Sort

```python
data = [38, 27, 43, 3, 9, 82, 10]


def merge(l, r):
    result = []
    while True:
        if l[0] <= r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))

        if len(l) == 0 or len(r) == 0:
            break

    if len(l) > 0:
        result.extend(l)
    if len(r) > 0:
        result.extend(r)

    return result


def merge_sort(m):
    if len(m) <= 1:
        return m
    mid = len(m) // 2
    left = m[:mid]
    right = m[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


print(merge_sort(data))
```



3. 우선순위 큐

```python
class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.link = link

head = None
def enqueue(n):
    global head
    if head == None:
        head = Node(n)
    else:
        parent = None
        p = head
        while True:
            if p.data > n:
                print("와꾸")
                parent.link = Node(n)
                parent.link.link = p
                break
            elif p.link == None:
                print('뺴액')
                p.link = Node(n)
                break
            else:
                print("민박")
                parent = p
                p = p.link

def delete(target):
    p = head
    while True:
        if p.link.data == target:
            break
        p = p.link
    p.link = p.link.link

enqueue(1)
enqueue(5)
enqueue(2)
enqueue(4)
enqueue(3)
delete(2)
enqueue(2)
print(head.link.data)
```



4. Joseph

```python
class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

head = None
def enq(n):
    global head
    if head == None:
        head = Node(n)

    else:
        p = head
        while True:
            if p.link == None:
                if n == 41:
                    print('빼액',p.data)
                    p.link = Node(n)
                    p.link.link = head
                    break
                else:
                    p.link = Node(n)
                    break

            p = p.link

def delete(target):
    global head
    p =head
    if p.data == target:
        head = head.link
    else:
        while True:
            if p.link.data == target:
                p.link = p.link.link
                break
            p = p.link

for i in range(1,42):
    enq(i)

for j in range(1,39):
    if j%3==0:
        delete(j)

i=0
p = head
while True:
    print(p.data)
    p = p.link
    i+=1
    if i > 41:
        break
```

