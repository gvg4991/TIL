datas = [64,25,10,22,11]
length = len(datas)
for idx in range(length):
    so = datas[idx]
    result_idx = idx
    for target_idx in range(idx,length):
        if so > datas[target_idx]:
            so = datas[target_idx]
            result_idx = target_idx
    datas[idx],datas[result_idx] = datas[result_idx],datas[idx]
    print(datas)







# import sys
# sys.stdin = open("input.txt")
#
#
#
# # def selection(start,end):
# #     if start == end:
# #         return
# #     else:
# #         target = min(datas[start:end])
# #         idx = datas.index(target)
# #         datas[idx] = datas[start]
# #         datas[start] = target
# #     selection(start+1,end)
# #
# # datas = list(map(int,' '.join(map(str,input())).split()))
# # selection(0,len(datas))
# # print(datas)




# datas = list(map(int,input().split()))
# min_d = None
# cnt = 0
# keep = []
# while cnt <= len(datas)-1:
#     min_d = min(datas[cnt:])
#     idx_d = datas.index(min_d)
#     keep = datas[cnt]
#     if keep != min_d:
#         datas[cnt] = min_d
#         datas[idx_d] = keep
#     cnt += 1
# print(datas)
