N=int(input())
dicionario={}
for i in range(N):
    T,P=input().split()
    T,P=[str(T),str(P)]
    dicionario[T]=P

frase=input()
frase=frase.split()
fraseresultado=''

for T in frase:
    if T in dicionario:
        fraseresultado+=dicionario[T]+' '

if fraseresultado=='':
    print('Tudo bem!')
else:
    print(fraseresultado[:-1])
