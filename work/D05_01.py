# #슬라이스를 이용
# def palindrome(word):
#     return word == word[::-1] #s[start:end:step]

#for
def is_palindrome(word):
    list_word=list(word)
    for i in range(len(list_word)//2): #길이로 반복하기(반으로 나눠서 반틈씩 확인하면)
        if list_word[i] != list_word[-i-1]:
            return False
    return True

#재귀
def is_pal(word):
    if len(word)<2:
        return True
    if word[0] != word[-1]:
        return False
    return is_pal(word[1:-1])

# print(palindrome('tomato'))
# print(palindrome('nan'))
print(is_palindrome('tomato'))
print(is_palindrome('nan'))
print(is_pal('tomato'))
print(is_pal('nan'))