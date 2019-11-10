datas = [55,7,78,12,42]
length = len(datas)

for start in range(length-1):
    for idx in range(start,length-1):
        if datas[idx] > datas[idx+1]:
            datas[idx],datas[idx+1] = datas[idx+1],datas[idx]
    print(datas)
# print(datas)
