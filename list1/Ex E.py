siglas=[]
regiao,estado,municipio,revenda,produto,data_venda,valor_venda,valor_compra,uni_medida,bandeira = input().split(sep=";")
if regiao=="Região-Sigla":
 regiao,estado,municipio,revenda,produto,data_venda,valor_venda,valor_compra,uni_medida,bandeira = input().split(sep=";")
while regiao!="Fim":
 list(municipio)
 list(revenda)
 tam_mun=len(municipio)
 tam_rev=len(revenda)
 sigla=[]
 if tam_mun > tam_rev:
  for i in range (tam_rev):
   sigla.append(municipio[i])
   sigla.append(revenda[i])
 else:
  for i in range (tam_mun):
   sigla.append(municipio[i])
   sigla.append(revenda[i])
 siglas.append(sigla)
 regiao,estado,municipio,revenda,produto,data_venda,valor_venda,valor_compra,uni_medida,bandeira = input().split(sep=";")
siglas.pop(0)
for sigla in siglas:
 print(''.join(sigla))
