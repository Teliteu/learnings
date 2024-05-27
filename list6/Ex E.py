n=int(input())
m=[]
p=0
for e in range(n):
    l=input().split()
    m.append(l)

while (p<n):
    for i in range(n):
        for j in range(n):
            if m[i][j]=='o' and (i+1)!=n:
                if m[i+1][j]=='.':
                    m[i][j]='.'
                    m[i+1][j]='o'
    p+=1
for i in range(n):
    print(' '.join(m[i]))
                    

    
