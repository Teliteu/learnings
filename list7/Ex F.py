texto= input().replace(".", "").replace(",", "").replace("!", "").replace("?", "").replace(":", "")
dicionario={}
for palavra in texto.split():
    palavra=palavra.lower()

    if palavra in dicionario:
        dicionario[palavra]+=1
    else:
        dicionario[palavra]=1
#for palavra in sorted(dicionario,key=lambda x:dicionario[x],reverse=True):
    #print(palavra.capitalize(),dicionario[palavra])
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
        lista.sort(reverse=True)
            
    for palavra in lista :
        print(palavra.capitalize()+' '+str(dicionario[palavra]))
        

