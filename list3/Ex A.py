A, B = input().split()
A, B = [int(A), int(B)]
media=0
contador=0
while A>0 and B>0:
    if A>B:
        maxi=B
    elif B<A:
        maxi=A
    else:
        maxi=A
    aaap=1
    for i in range (2,maxi):
        if (A%i==0) and (B%i==0):
            aaap=i
    print(aaap)
    media=media+aaap
    contador=contador+1
    A, B = input().split()
    A, B = [int(A), int(B)]
med=(media/contador)
print(med)
        
   



