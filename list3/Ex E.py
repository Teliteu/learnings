k=int(input())
kesimo2=1
kesimo1=0
kesimor=0
contador=0
somakesimor=0
z=0
while k<=0:
 for _ in range(k):
  kesimor=kesimo1+kesimo2
  kesimo2=kesimo1
  kesimo1=kesimor
  contador=contador+1
  somakesimor=somakesimor+kesimor
  k=int(input())
if k%2==0 and kesimor%2==0:
    z=k+kesimor
    print(z)
elif k%2!=0 and kesimor%2!=0:
    z=kesimor//k
    print(z)
elif k%2==0 and kesimor%2!=0:
    z=kesimor*k
    print(z)
else:
    z=kesimor-k
    print(z)
print(somakesimor)
print(kesimor)
z=somakesimor/contador
print(z)
        
    
    
