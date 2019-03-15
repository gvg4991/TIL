datas = [5,1,-4,2,-1,-5,-2,8,-3,6]

result = [0]*len(datas)
ans = []
cnt = 0
target = 0
for i in datas:
    if target >= 0:
        target += i
        result[cnt] = target
        ans.append(i)
    else:
        result[cnt] = i
        target = i
        ans = [i]
    cnt += 1
print(result)
print(max(result))
print(ans)


rangesum = [0]*len(datas)
usedata = [0]*len(datas)
for now in range(len(datas)):
    rangesum[now] = max(rangesum[now-1]+datas[now],datas[now])
    if rangesum[now] == rangesum[now-1]+datas[now]:
        usedata[now] = 1
    else:
        usedata = [0]*len(datas)
        usedata[now] = 1

print(rangesum)
print(max(rangesum))
print(usedata)