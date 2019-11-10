datas=[0,4,1,3,1,2,4,1]
dae = max(datas)
cnt = [0]*(dae+1)
length = len(datas)

result=[0]*length
for idx in range(length):
    cnt[datas[idx]] += 1
print(cnt)

for idx in range(1,dae+1):
    cnt[idx] += cnt[idx-1]
print(cnt)

for idx in range(-1,-1*length,-1):
    result[cnt[datas[idx]]-1] = datas[idx]
    cnt[datas[idx]] -= 1
    print(result)

# for idx in range(length-1,-1,-1):
#     result[cnt[datas[idx]]-1] = datas[idx]
#     cnt[datas[idx]] -= 1
# print(result)
