n=int(input())
cont=0
med=0
for i in range (n):
    a, b=input().split()
    a, b=[int(a),int(b)]
    r=0
    if a>b:
        r=a
    elif b>a:
        r=b
    else:
        r=b
    for i in range(1,r):
        if ((a%i==0)) or ((b%i==0)):
            valor=1
    vari=valor
    mmc=(a*b)/valor
    med=med+mmc
    cont=cont+1
    print("%.0f"%mmc)
media=med/contador
print("%.2f"%media)
