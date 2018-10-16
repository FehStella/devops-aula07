import jogovelha
import sys
        v1.1


        master
erroInicializar = False

jogovelha.inicializar()
jogo = jogovelha.tabuleiro()
 v1.1


 master
if len(jogo) != 3:
	erroInicializar = True
else:
	for linha in jogo:
 v1.1
		if len(linha) != 3:
			erroInicializar = True
		else:
			for elemento in linha:
				if elemento != '.':
					erroInicializar = True


if erroInicializar:
		print('Erro!')
		sys.exit(1)

else:
		sys.exit(0)

			if len(linha) != 3:
					erroInicializar = True
			else:
				for elemento in linha:
					if elemento != '.':
							erroInicializar = True
if erroInicializar:
			print('Erro!')
			sys.exit(1)
else:
			sys.exit(0)
 master
