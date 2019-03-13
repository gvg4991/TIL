a=24
b=18
x=a
y=b

result = None
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
if a == 0:
    result = int(b)
    print(b)
else:
    result = int(a)
    print(a)

print(x*y//result)