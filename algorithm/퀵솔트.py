import sys
sys.stdin = open("input.txt")


def quicksort(a,l,r):
    if l < r:
        s = partition(a,l,r)
        quicksort(a,l,s-1)
        quicksort(a,s+1,r)

def partition(a,l,r):
    p = a[l] #3
    i = l
    j = r
    while i <= j:
        while a[i] <= p: #2 -> 4 -> 6
            i += 1 #1 -> 2
        while a[j] > p: #5 -> 1 -> 1
            j -= 1 #7 -> 4
        if i < j:
            empty = a[i] #4
            a[i] = a[j] #1
            a[j] = empty #4
    a[l] = a[j]
    a[j] = p

    return j

datas = list(map(int,input().split()))
quicksort(datas,0,len(datas)-1)
print(datas)