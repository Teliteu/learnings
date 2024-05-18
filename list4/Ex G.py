def checar (x, y):
    if x==y:
        return 1
    else:
        return 2
    
n=int(input())
"""
while n<=0:
      n=int(input())"""
      
check1=n/2
check2=n//2
retorno=checar(check1, check2)

if retorno==1:   
   for _ in range(n//2):
         print(n)
         n=n-2
         
else:
    n=n-1
    for _ in range(n//2):
           print(n)
           n=n-2
