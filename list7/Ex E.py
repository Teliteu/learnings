obra=input()
palavra=''
dicionario={}
for i in obra:
    if(i==',' or i==' ' or i=='.'):
        if (palavra!=''):
            palavra=palavra.capitalize()
            if palavra not in dicionario:
                dicionario[palavra]= 1
            else:
                dicionario[palavra]+=1
            palavra=''
    else:
        palavra+=i
maiorvalor=0
maiorpalavra=''

for palavra in dicionario:
    if dicionario[palavra]>maiorvalor:
        maiorvalor=dicionario[palavra]
        maiorpalavra=palavra

for i in range(maiorvalor):
    lista=[]
    for palavra in dicionario:
        if dicionario[palavra]==maiorvalor-i:
            lista.append(palavra)
    lista.sort()
    for palavra in lista.sort(reverse=True):
        print(palavra+' '+str(dicionario[palavra]))
        



