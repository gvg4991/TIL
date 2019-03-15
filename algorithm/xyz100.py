# #비재귀
# result = []
# for x in range(1,11):
#     for y in range(1,11):
#         for z in range(1,11):
#             if x <= y and y <= z and x+y+z==10:
#                 result.append((x,y,z))
# print(len(result))

#재귀
count = 0
def hundred(x,y,z):
    global count
    if x+y+z > 100:
        return
    if x>y or y>z:
        return
    if x+y+z == 100:
        count += 1
        return

    if visited[x+1][y][z] == False:
        visited[x+1][y][z] = True
        hundred(x+1,y,z)
    if visited[x][y+1][z] == False:
        visited[x][y+1][z] = True
        hundred(x,y+1,z)
    if visited[x][y][z+1] == False:
        visited[x][y][z+1] = True
        hundred(x,y,z+1)


visited = [[[0]*100 for i in range(100)] for j in range(100)]
count = 0
hundred(1,1,1)
print(count)



