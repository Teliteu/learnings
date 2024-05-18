def valor(n):
    while n!=0:
        if n%2==0:
            s=0
            for c in range (n,0,-2):
               s+=n^2
            print(s)

n=int(input())
valor(n)
