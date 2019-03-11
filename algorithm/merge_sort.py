def merge_sort(n):
    global result
    if len(n) <= 1:
        return n
    mid = len(n)//2
    left = n[:mid]
    right = n[mid:]

    left = merge_sort(left) #7
    right = merge_sort(right) #2

    return merge(left,right) #7,2

def merge(left,right):
    global result
    result = [0]*(len(left)+len(right)) #00
    i = l = r = 0

    while l<len(left) and r<len(right): # 둘다 0보다 클때 반복
        if left[l] < right[r]:
            result[i] = left[l]
            l += 1
        else:
            result[i] = right[r]
            r += 1
        i += 1

    if len(left)-l>0:
        result[i:] = left[l:]
    elif len(right)-r>0:
        result[i:] = right[r:]

    return result


datas = [7,2,9,4,3,8,6,1]
# result = [0]*len(datas)
merge_sort(datas)
print(result)