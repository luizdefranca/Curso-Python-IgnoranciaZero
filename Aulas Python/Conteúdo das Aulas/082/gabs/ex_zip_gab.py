"""
Você foi contratado para fazer um database dos preços 
dos itens de um determinado supermercado. Para tal o 
supermercado lhe forneceu um arquivo txt contendo os itens
seguidos de seus respectivos preços. 

Monte um database usando o modulo shelve em que as chaves
são os itens e os valores são os preços. De uma olhada
no objeto shelve.DbfilenameShelf (use a função help), especialmente no seu
método update para facilitar o trabalho. De uma olhada no método
dict também.
"""

import shelve

def main():
	itens = []
	preços = []
	for linha in open('Lista Supermercado.txt'):
		print(linha)
		l = linha.split(' - ')
		try:
			itens.append(l[0].rstrip())
			preços.append(float(l[1].rstrip()))
		except (IndexError, ValueError):
			break

	database = shelve.open('supermercado.db')
	database.update(dict(zip(itens, preços)))
	database.close()

def imprimeDatabase():
	database = shelve.open('supermercado.db')
	for key in database:
		print(key, ': R$', database[key])



main()
imprimeDatabase()			
	
	
