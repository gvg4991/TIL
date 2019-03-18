def prime1(n):  #O(n)
   if n<2: return False
   for i in range(2, n):
       if n%i ==0 : return False
   return True

def prime2(n):#O(n/2)
   if n<2: return False
   for i in range(2, n//2+1):
       if n%i ==0 : return False
   return True

def prime3(n): #O(Root n)
   if n<2: return False
   i = 2
   while i*i<=n :
          if n%i ==0 : return False
          i+=1
   return True

#print(prime1(100000007))
#print(prime2(100000007))
print(prime3(100000007))