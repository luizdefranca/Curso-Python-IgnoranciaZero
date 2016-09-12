def funcao_auxiliar(candidatas_totais):
	arquivo = open("FRASE.txt", "w")
	frase = []
	for i in range(len(candidatas_totais)):
		frase.append("")
	for a0 in range(len(candidatas_totais[0])):
		frase[0]= candidatas_totais[0][a0]
		for a1 in range(len(candidatas_totais[1])):
			frase[1]= candidatas_totais[1][a1]
			for a2 in range(len(candidatas_totais[2])):
				frase[2]= candidatas_totais[2][a2]
				for a3 in range(len(candidatas_totais[3])):
					frase[3]= candidatas_totais[3][a3]
					for a4 in range(len(candidatas_totais[4])):
						frase[4]= candidatas_totais[4][a4]
						frase_s = ""
						for palavra in frase:
							frase_s += palavra
							frase_s += " "
						arquivo.write(frase_s + "\n")
	arquivo.close()