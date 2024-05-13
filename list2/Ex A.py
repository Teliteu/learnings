p = float(input())
h = float(input())
IMC = p/(h**2)
a = IMC-24.9
minimo= a*(h**2)
print("%.2f"%IMC)
if(IMC < 18.5):
    print("Baixo peso")
elif(IMC <= 24.9):
    print("Peso normal")
elif(IMC <= 29.9):
    print("Sobrepeso")
    print("%.2f"%(minimo))
elif(IMC <= 34.9):
    print("Obesidade grau I")
    print("%.2f"%(minimo))
elif(IMC <= 39.9):
    print("Obesidade grau II")
    print("%.2f"%(minimo))
else:
    print("Obesidade grau III")
    print("%.2f"%(minimo))
