def buscaLucro(acoes_listadas,lucro):
	i = 0
	while i<len(acoes_listadas) and acoes_listadas[i]['lucro']!=lucro:
		i+=1
	if i == len(acoes_listadas):
		return None
	else:
		return acoes_listadas[i]

acao1 = {'nome':'petr4','lucro':1500}
acao2 = {'nome':'vale5','lucro':2000}
acao3 = {'nome':'bbas3','lucro':1000}
acao4 = {'nome':'itub4','lucro':2500}

acoes_listadas = [acao1,acao2,acao3,acao4]

print(buscaLucro(acoes_listadas,1000))