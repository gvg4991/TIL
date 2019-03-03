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

