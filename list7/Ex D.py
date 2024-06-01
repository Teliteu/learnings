N=int(input())
n=0
s=0
l=0
o=0
for i in range(N):
    D,Q=input().split()
    D,Q=[str(D),int(Q)]
    

    if D=='N':
        n+=Q
    if D=='S':
        s+=Q
    if D=='L':
        l+=Q
    if D=='O':
        o+=Q

if n>=s:
    S=n-s
    N=0
else:
    S=0
    N=s-n
if l>=o:
    O=l-o
    L=0
else:
    O=0
    L=o-l

print(N,S,L,O)

