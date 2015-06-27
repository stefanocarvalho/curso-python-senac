from random import randint
print("Bienvenidos!")
num_sorteado = randint(1, 100)
#print(num_sorteado)
novo_jogo = True
while novo_jogo != False:
	contador = 1
	while True:
		chute = int(input("Chute um numero: "))
		if chute == num_sorteado:
			print("Aah mizeravi, ACERTOU!")
			break
		else:
			print("Chute acima do sorteado!" if chute > num_sorteado else "Chute abaixo do sorteado!")
			contador+=1
	print("Fim de game!!!")
	print("Numero sorteado: " + str(num_sorteado))
	print("Numero de tentativas: " + str(contador))
	novo_jogo = int(input("Deseja jogar novamente? [1 -> SIM, 0 -> NAO]: "))
