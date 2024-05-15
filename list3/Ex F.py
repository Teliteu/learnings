A, N=input().split()
A, N=[int(A), int(N)]
somaN=0
somaN3=0
contador=0
maior=0
while A!=-1:
    A, N=input().split()
    A, N=[int(A), int(N)]
    contador=contador+1
    if A%8==0:
        somaN=(somaN+N)
    if N>3 and A!=-1:
        somaN3=(somaN3+N)
     
    
print(somaN)
mediaN3=somaN3/contador
print("%.2f"%mediaN3)



