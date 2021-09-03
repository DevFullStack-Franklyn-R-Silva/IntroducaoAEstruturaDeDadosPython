
def contaNeg(lista):
	cont = 0
	for elem in lista:
		if elem<0:
			cont+=1
	return cont

lista = [1,2,0,-1,3,-2,4,-6]
print(contaNeg(lista))