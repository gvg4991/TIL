def collatz(x):
    count=0
    while x>=1:
        count+=1
        if count!=500:
            if x%2:
                x*3+1
            else:
                x/2
        else:
            count=-1
    return count

print(collatz(6))