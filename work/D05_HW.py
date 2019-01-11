#List는 for 문을 실행하면 모든 요소를 순차적으로 돌면서 반복문을 수행합니다. 임의의 리스트 my_list의 값을 하나씩 출력하는 코드를 아래에 작성하시오.
my_list=['재형','종원','민호','지현','영현']
for l in my_list:
    print(l)

# 위에 작성한 코드를 인덱스(index) 값과 함께 출력하는 코드로 변경하시오
my_dict={}
for idx,val in enumerate(my_list):
    print(idx,val)
    my_dict[idx]=val
print(my_dict)

#  딕셔너리는 key, value로 구성되어 있습니다. 따라서, 딕셔너리 my_dict 각각의 상 황에 따라 반복문을 수행할 수 있도록 빈칸을 채우시오.
for key in my_dict.keys():
    print(key)
for value in my_dict.values():
    print(value)
for key2,value2 in my_dict.items():
    print(key2,value2)

#  result에 저장된 값은?
def my_func(a, b):
    c = a + b
    print(c) 
my_func(1, 5)
