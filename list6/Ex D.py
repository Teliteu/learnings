n=int(input())
l=input().split()
m=[]
m+=l
c=0
for mud in range(5):
    b,d,q=input().split()
    b,d,q=[str(b),str(d),int(q)]
    ind=l.index(b)
    ind2=0
    if d=='D':
        if (ind+q)>=n:
            ind2=q+ind-n
        else:
            ind2=ind+q

    else:
        if(ind-q)<0:
            ind2=n-q-ind
        else:
            ind2=ind-q
    

        
    l.insert(ind2,l.pop(ind))

    
for el in range(len(l)):
    if l[el]!=m[el]:
        c=c+1

print(c)

