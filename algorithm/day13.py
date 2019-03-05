# tree
# 전위순회 = 루트 - 레프트 - 라이트
# 중위순회 = 레프트 - 루트 - 라이트
# 후위순회 = 레프트 - 라이트 - 루트


# # 트리테이블
#
# datas = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
#
# result = [[0]*5 for i in range(max(datas)+1)]
# # result[i][0] = left-child
# # result[i][1] = right-child
# # result[i][2] = 자녀수
# # result[i][3] = 부모
# # result[i][4] = level
#
# harf = len(datas)//2 # 부모,자식 순서로 데이터 받음
# parent = []
# child = []
# for i in range(harf):
#     parent.append(datas[2*i]) #짝수번째(부모)
#     child.append(datas[2*i+1])  #홀수번째(자식)
#
# for i in range(harf):
#     if result[parent[i]][0] == 0: #부모의 left-child가 없으면
#         result[parent[i]][0] = child[i] #left-child에 자식을 넣고
#         result[parent[i]][2] += 1 #자녀수를 늘림
#         result[child[i]][3] = parent[i] #자녀 index에서 부모 입력
#         result[child[i]][4] = result[parent[i]][4] + 1 #자녀 index에서 레벨을 부모로부터 1 더해줌
#     else:
#         result[parent[i]][1] = child[i]
#         result[parent[i]][2] += 1
#         result[child[i]][3] = parent[i]
#         result[child[i]][4] = result[parent[i]][4] + 1
#
# print(result)




#-----------------------------------------------------------------------------------------------------------------
#연습문제 (전위중위후위 순회)

# result[i][0] = left-child
# result[i][1] = right-child
# result[i][2] = 자녀수
# result[i][3] = 부모
# result[i][4] = level
# def tree(value):
#     if result[value][0] != 0:
#         ans.append(result[value][0])
#         tree(ans[-1])
#
#     if result[value][1] != 0:
#         ans.append(result[value][1])
#         tree(ans[-1])
#
#     return
#
#
# datas = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]
#
# # 전위
# result = [[0]*5 for i in range(max(datas)+1)]
# # result[i][0] = left-child
# # result[i][1] = right-child
# # result[i][2] = 자녀수
# # result[i][3] = 부모
# # result[i][4] = level
#
# harf = len(datas)//2 # 부모,자식 순서로 데이터 받음
# parent = []
# child = []
# for i in range(harf):
#     parent.append(datas[2*i]) #짝수번째(부모)
#     child.append(datas[2*i+1])  #홀수번째(자식)
#
# for i in range(harf):
#     if result[parent[i]][0] == 0: #부모의 left-child가 없으면
#         result[parent[i]][0] = child[i] #left-child에 자식을 넣고
#         result[parent[i]][2] += 1 #자녀수를 늘림
#         result[child[i]][3] = parent[i] #자녀 index에서 부모 입력
#         result[child[i]][4] = result[parent[i]][4] + 1 #자녀 index에서 레벨을 부모로부터 1 더해줌
#     else:
#         result[parent[i]][1] = child[i]
#         result[parent[i]][2] += 1
#         result[child[i]][3] = parent[i]
#         result[child[i]][4] = result[parent[i]][4] + 1
#
# ans = []
# for i in range(harf):
#     if result[parent[i]][3] == 0:
#         ans.append(parent[i])
#
# tree(ans[0])
# print(ans)


def preorder(value):
    ans.append(value)
    if result[value][0] != 0:
        preorder(result[value][0])
    if result[value][1] != 0:
        preorder(result[value][1])
    return

def inorder(value):
    if result[value][0] != 0:
        inorder(result[value][0])
    ans.append(value)
    if result[value][1] != 0:
        inorder(result[value][1])
    return

def postorder(value):
    if result[value][0] != 0:
        postorder(result[value][0])
    if result[value][1] != 0:
        postorder(result[value][1])
    ans.append(value)
    return


datas = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]

# 전위
result = [[0]*5 for i in range(max(datas)+1)]
# result[i][0] = left-child
# result[i][1] = right-child
# result[i][2] = 자녀수
# result[i][3] = 부모
# result[i][4] = level

harf = len(datas)//2 # 부모,자식 순서로 데이터 받음
parent = []
child = []
for i in range(harf):
    parent.append(datas[2*i]) #짝수번째(부모)
    child.append(datas[2*i+1])  #홀수번째(자식)

for i in range(harf):
    if result[parent[i]][0] == 0: #부모의 left-child가 없으면
        result[parent[i]][0] = child[i] #left-child에 자식을 넣고
        result[parent[i]][2] += 1 #자녀수를 늘림
        result[child[i]][3] = parent[i] #자녀 index에서 부모 입력
        result[child[i]][4] = result[parent[i]][4] + 1 #자녀 index에서 레벨을 부모로부터 1 더해줌
    else:
        result[parent[i]][1] = child[i]
        result[parent[i]][2] += 1
        result[child[i]][3] = parent[i]
        result[child[i]][4] = result[parent[i]][4] + 1

ans = []
for i in range(harf):
    if result[parent[i]][3] == 0:
        answer = parent[i]

preorder(answer)
print(ans)
ans = []
inorder(answer)
print(ans)
ans = []
postorder(answer)
print(ans)