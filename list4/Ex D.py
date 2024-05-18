def fatorial (n):
    if n<0:
        print('-1')
    elif n%2==0:
        s=0
        for c in range (n-2,0,-2):
            s+=c
        print(s)
    else:
        s=0
        for c in range (n-3,0,-2):
            s+=c
        print(s)


n=int(input())
fatorial(n)