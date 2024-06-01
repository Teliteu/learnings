N=int(input())
problemas=[]
for i in range(N):
    nome,solucao,dificuldade = input().split()
    dificuldade = int(dificuldade)
    problemas.append((solucao,dificuldade))
problemas_sort = sorted(problemas, key=lambda x:-x[1])
for item in problemas_sort:
    print(item[0],end='')
print()

