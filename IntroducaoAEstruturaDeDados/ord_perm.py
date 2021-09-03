import random

def ordena(lista):
	lista_ord = lista
	cont = 0
	while verificaOrdenacao(lista_ord) != True:
		lista_ord = perm(lista[:])
		cont+=1
	print('numero de permutacoes: %d'%cont)
	return lista_ord

def verificaOrdenacao(lista):
	for i in range(1,len(lista)):
		if lista[i]<lista[i-1]:
			return False
	return True

def perm(lista):
	permutacao = []
	while len(lista)>0:
		pos = random.randint(0,len(lista)-1)
		permutacao.append(lista.pop(pos))
	return permutacao
		
lista = [2,5,4,1,3,9,26,6,11,23,2,5,4,1,3,9,26,6,11,23]
print(ordena(lista))


