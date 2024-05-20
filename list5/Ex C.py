a,b=input().split()
p=a.lower()
q=b.lower()
m=p,q
o=sorted(m)
v=o[1]
if p==v:
    print('A')
elif q==v:
    print('B')
