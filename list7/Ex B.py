N=int(input())
dicionario={}
for i in range(N):
    nome=input().split()
    pessoa,marmita=nome[0].lower(),nome[1:]
    resultado=''

    for palavra in marmita:
        resultado+=palavra+' '
        print(resultado)
    

    dicionario[pessoa]=resultado[:-1]
print(len(dicionario))

for marmita in sorted(dicionario):
    print(dicionario[marmita])

