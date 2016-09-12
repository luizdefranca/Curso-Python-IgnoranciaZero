"""
Escreva um programa para checar se uma senha numérica está correta

Pergunte para o usuário se ele quer definir uma senha,
veficar o usuário ou sair.

Escreva, com apenas uma linha, uma forma de 
verificar se a senha está correta
"""
senha = ""
while True:
	a = input('Desenha definir uma senha(d), verificar o usuário(v) ou sair(s)?\n').lower()
	
	if a.startswith('d'):
		while True:
			senha =input('Digite a senha(apenas digitos)\n')
			if not senha.isdigit():
				print('Digite apenas digitos!!')
			else:
				break

	elif a.startswith('v'):
		tentativa = input('Digite sua senha\n')
		if all([senha[i] == tentativa[i] and len(senha) == len(tentativa) for i in range(len(senha))]):
			print('A senha está correta!!')
		else:
			print('A senha está incorreta!!')
	elif a.startswith('s'):
		break
	else:
		print('Não entendi seu comando, digite novamente')	
