numero1=float(input())
numero2=float(input())
numero3=float(input())

if numero2>=numero1 and numero2>=numero3:
  A=numero2
  B=numero1
  C=numero3
  if A>=B+C:
    print("NAO FORMA TRIANGULO")

  elif (A**2)==(B**2)+(C**2):
    print("TRIANGULO RETANGULO")

  elif A==B==C:
    print("TRIANGULO EQUILATERO")

  elif A==B or A==C or B==C:
    print("TRIANGULO ISOSCELES")

  else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")

elif numero1>=numero2 and numero1>=numero3:
  A=numero1
  B=numero2
  C=numero3
  if A>=B+C:
    print("NAO FORMA TRIANGULO")

  elif (A**2)==(B**2)+(C**2):
    print("TRIANGULO RETANGULO")

  elif A==B==C:
    print("TRIANGULO EQUILATERO")

  elif A==B or A==C or B==C:
    print("TRIANGULO ISOSCELES")

  else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")

elif numero3>=numero1 and numero3>=numero2:
  A=numero3
  B=numero1
  C=numero2
  if A>=B+C:
    print("NAO FORMA TRIANGULO")

  elif (A**2)==(B**2)+(C**2):
    print("TRIANGULO RETANGULO")

  elif A==B==C:
    print("TRIANGULO EQUILATERO")

  elif A==B or A==C or B==C:
    print("TRIANGULO ISOSCELES")
    
  else:
    print("TRIANGULO ACUTANGULO OU OBTUSANGULO")
