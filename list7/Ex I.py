N=int(input())
jogadas=[]
for i in range(N):
    J,I=input().split()
    I=int(I)
    jogadas.append((J,I))
partida=jogadas[N-1][1]
while jogadas[partida-1][1]!=N:
    partida=jogadas[partida-1][1]
print(jogadas[partida-1][0])
