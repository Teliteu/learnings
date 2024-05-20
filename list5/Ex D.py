n=int(input())
x=0
y=0
for i in range (0,n):
    a=str(input())
    m=a.lower()
    p=m.count('p')
    u=m.count('u')
    x+=p
    y+=u
print(x,y)
