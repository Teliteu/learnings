n=int(input())
N=n
q=0
soma=0
contador=0
for _ in range(n):
     q=q+1
     n=q
     if N%n==0:
         print(n, end=" ")
         soma=n+soma
         contador=contador+1
     if n==N:
         print("\n%0.f"%soma)
         print(contador)
         break

        
