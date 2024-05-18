def fatorial(n):
    if n%2==0:
        for c in range(n,1,-2):
            print (c)
    else:
        for c in range (n-1,1,-2):
            print(c)


n=int(input())
fatorial(n)
