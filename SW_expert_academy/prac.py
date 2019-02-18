# 다음은 학생의 점수를 나타내는 리스트입니다.
# [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
# while 문과 리스트 객체의 pop()을 이용해 80점 이상의 점수들의 총합을 구하시오.
# 출력: 454

a = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]

# a.sort()
# print(a)

# print(len(a))
# print(type(len(a)))


# print("!".join(a))

# for i in range(5,2,-1):
#     print(i)

# b=a.index(max(a))
# print(b)

# d=max(3,9,5)
# print(d)

ds=[]
for i in range(3):
    ds += [list(map(int,input().split()))]
print(ds)