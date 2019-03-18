import sys
sys.stdin = open("input.txt")


two = list(input())
ans = []
for start in range(0,len(two)-6,7):
    if len(two)-start > 7:
        result = ''.join(map(str,two[start:start+7]))
        ans.append(int(result,2))
    else:
        result = ''.join(map(str,two[start:]))
        ans.append(int(result,2))
print(ans)


# #n^2
# data = input()
# for start in range(0,len(data)-7,7):
#     s = 0
#     for now in range(start, start+7):
#         s=s*2 + int(data[now])
#     print(s)


# #n^2
# data = input()
# for tc in range(0,10):
#     num = 0
#     for now in range(tc*7, tc*7+7):
#         num<<=1
#         num += int(data[now])
#     print(num)


# #n
# data = input()
# t = 0
# for i in range(len(data)):
#     t = t*2 + int(data[i])
#     if (i+1)%7 == 0:
#         print(t,end = '')
#         t=0



# 대현이형
# lst = [0,0,0,0,0,0,0,1,1,1,
#        1,0,0,0,0,0,0,1,1,0,
#        0,0,0,0,0,1,1,1,1,0,
#        0,1,1,0,0,0,0,1,1,0,
#        0,0,0,1,1,1,1,0,0,1,
#        1,1,1,0,0,1,1,1,1,1,
#        1,0,0,1,1,0,0,1,1,1]
#
# result = 0
# for i in range(len(lst)):
#     temp = (1<<6)>>(i%7)
#
#     if temp&(lst[i]<<6)>>(i%7):
#         result+=temp
#
#     if i%7==6:
#         print(result)
#         result = 0