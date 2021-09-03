
def abaixoMedia(lista):
	soma = 0
	for elem in lista:
		soma+=elem
	media = soma/len(lista)
	print(media)
	cont = 0
	for elem in lista:
		if elem < media:
			cont+=1
	return cont

print(abaixoMedia([2,3,4,1,0,6]))


