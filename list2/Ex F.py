numero=int(input())
y=numero
b=0
x=0
while numero!=0:
      x=x+1
      b=b+numero
      if numero>y:
          y = numero
      numero=int(input())
z = float(b/x)
if(x > 0):
    print(x)
    print(y)
    print("%.2f"%z)
else:
    print(x)
    print(y)
    print("%.2f"%0)
        
