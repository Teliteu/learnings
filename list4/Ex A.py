def compare(a,b):
    if a>b:
        r=1
    elif a<b:
        r=-1
    else:
        r=0
    return r


x=int(input())
y=int(input())

resultado = compare(x , y)
if(resultado == 1):
    print('x e maior que y')
elif(resultado == 0):
    print('x e igual a y')
else:
    print('x e menor que y')
