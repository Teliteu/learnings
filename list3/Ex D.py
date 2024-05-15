n=int(input())
contador=0
ouromaior=0
ourosomatoria=0
for _ in range(n):
     ouro=int(input())
     contador=contador+1
     if contador==1:
        ouromaior=ouro
     ourofinal=ouromaior-ouro
     ourosomatoria=ourosomatoria+ourofinal
     if contador==n:
      break
print(ourosomatoria)
    
