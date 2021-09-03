def somaMax(lista):
	somaMaior = -1
	iMax = 0
	jMax = 0
	for i in range(len(lista)):
		for j in range(len(lista)):
			if i != j:
				soma = lista[i]+lista[j]
				if soma > somaMaior:
					somaMaior = soma
					iMax = lista[i]
					jMax = lista[j]
	return somaMaior,iMax,jMax
				
lista = [1]*100000
print(somaMax(lista))