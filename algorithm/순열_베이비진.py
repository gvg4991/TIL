import sys
sys.stdin = open("input.txt")




datas = list(map(int,list(input())))

result = []
ans = False
for a in range(len(datas)):
        for b in range(len(datas)):
            if a != b:
                for c in range(len(datas)):
                    if a != c and b != c:
                        for d in range(len(datas)):
                            if a != d and b != d and c != d:
                               for e in range(len(datas)):
                                    if a != e and b != e and c != e and d != e:
                                        for f in range(len(datas)):
                                            if a != f and b != f and c != f and d != f and e != f:
                                                # print(a,b,c,d,e,f)
                                                result = [datas[a],datas[b],datas[c],datas[d],datas[e],datas[f]]
# print(result)

                                                empty=[0]*len(result)
                                                cnt=[0]*(max(result)+1)

                                                for i in result:
                                                    cnt[i]+=1
                                                # print(cnt)

                                                for cnt_triple in range(len(cnt)):
                                                    if cnt[cnt_triple]>=6:
                                                        cnt[cnt_triple]-=6
                                                    elif cnt[cnt_triple]>=3:
                                                        cnt[cnt_triple]-=3
                                                # print(cnt)

                                                for cnt_run in range(len(cnt)-2):
                                                        if cnt[cnt_run]>=2 and cnt[cnt_run+1]>=2 and cnt[cnt_run+2]>=2:
                                                                cnt[cnt_run]-=2
                                                                cnt[cnt_run+1]-=2
                                                                cnt[cnt_run+2]-=2
                                                        elif cnt[cnt_run]>=1 and cnt[cnt_run+1]>=1 and cnt[cnt_run+2]>=1:
                                                                cnt[cnt_run]-=1
                                                                cnt[cnt_run+1]-=1
                                                                cnt[cnt_run+2]-=1
                                                # print(cnt)

                                                if sum(cnt) == 0:
                                                    ans = True
print(ans)

