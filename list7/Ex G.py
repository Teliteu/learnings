n=int(input())
lista=[]
for i in range(n):
    arquivo=input().split()
    lista.append((arquivo[0],arquivo[1:]))
tags=input().split()
request = list(filter(lambda f: list(filter(lambda tag: tag in tags, f[1])), lista))
for x in request:
    print(x[0])
