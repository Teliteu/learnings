t=str(input())
s=str(input())
tj=t.upper().count('J')
to=t.upper().count('O')
th=t.upper().count('H')
tn=t.upper().count('N')
tt=tj+to+th+tn
sj=s.upper().count('J')
so=s.upper().count('O')
sh=s.upper().count('H')
sn=s.upper().count('N')
o=sj+so+sh+sn
i=tt-o
print(i,o,end=' ')