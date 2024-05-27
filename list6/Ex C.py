a,b=input().split()
a,b=[int(a),int(b)]
l=[]
d=''
for i in range(a+1):
    l.append("x")

l[b]='o'

for xy in range(a):
    x,y=input().split()
    x,y=[str(x),int(y)]
    if l[y]=='o':
        d=x
    del l[y]

print(d)
