# # import sys
# # sys.stdin = open("input.txt")
#
#
# def quicksort(a,l,r):
#     if l < r:
#         s = partition(a,l,r)
#         quicksort(a,l,s-1)
#         quicksort(a,s+1,r)
#
# def partition(a,l,r):
#     p = a[l] #3
#     i = l
#     j = r
#     while i <= j:
#         while a[i] <= p: #2 -> 4 -> 6
#             i += 1 #1 -> 2
#         while a[j] > p: #5 -> 1 -> 1
#             j -= 1 #7 -> 4
#         if i < j:
#             empty = a[i] #4
#             a[i] = a[j] #1
#             a[j] = empty #4
#     a[l] = a[j]
#     a[j] = p
#
#     return j
#
# # datas = list(map(int,input().split()))
# datas = [69,10,30,2,16,8,31,22]
# quicksort(datas,0,len(datas)-1)
# print(datas)



def partition(a,begin,end):
    pivot = (begin+end)//2
    l = begin
    r = end
    while l<r:
        while a[l]<a[pivot] and l<r:
            l += 1
        while a[r]>=a[pivot] and l<r:
            r -= 1
        if l<r:
            if l == pivot:
                pivot = r
            a[l],a[r] = a[r],a[l]
    a[pivot],a[r] = a[r],a[pivot]
    print(pivot,a[pivot],a)
    return r

def quicksort(a,begin,end):
    if begin < end:
        p = partition(a,begin,end)
        quicksort(a,begin,p-1)
        quicksort(a,p+1,end)

datas = [69,10,30,2,16,8,31,22]
quicksort(datas,0,len(datas)-1)
# print(datas)
