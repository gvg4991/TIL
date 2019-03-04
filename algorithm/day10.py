#문자열
#-------------------------------------------------------------------------------------
#reverse

s = 'Reverse this strings'

s_list = list(s)
empty = None
for i in range(len(s_list)//2):
    empty = s_list[i]
    s_list[i] = s_list[-(i+1)]
    s_list[-(i+1)] = empty
print(''.join(s_list))

# print(s)
# print(s_list)




#-------------------------------------------------------------------------------------
#atoi

datas = ['4', '2', 'F', 'B']

for i in range(len(datas)):
    if '0' <= datas[i] <= '9':
        datas[i] = ord(datas[i]) - ord('0')
    else:
        datas[i] =ord(datas[i]) - ord('A') + 10

print(datas)




#-------------------------------------------------------------------------------------
#itoa

data = 1234
n=0
while True:  # n=4
    if data < 10**n:
        break
    n += 1

change = ''
count = 0
while count != n:
    num = data % 10
    change = chr(ord('0') + num) + change
    data = (data - num)//10
    count += 1

print(change)