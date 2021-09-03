acao1 = {'nome':'petr4','lucro':1500}
acao2 = {'nome':'vale5','lucro':2000}
acao3 = {'nome':'bbas3','lucro':1000}
acao4 = {'nome':'itub4','lucro':2500}

acoes_listadas = [acao1,acao2,acao3,acao4]

def getMaiorLucro(acoes_listadas):
	acao_maior_lucro = acoes_listadas[0]

	for acao in acoes_listadas[1:]:
		if acao['lucro']>acao_maior_lucro['lucro']:
			acao_maior_lucro = acao

	return acao_maior_lucro