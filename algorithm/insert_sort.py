def insert(datas,n):
    for j in range(n):
        target = datas[j]
        i = j-1
        while i>0 and datas[i]>target:
            datas[i+1] = datas[i]
            i = i-1
        datas[i+1] = target

datas = [1,9,3,6,7,0,4,9,5,5]
insert(datas,1)
print(datas)
