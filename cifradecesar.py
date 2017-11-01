#!usr/bin/python

import argparse

def getArguments():
	parser = argparse.ArgumentParser(
		description="Um programa que Criptografa e Descriptografa Cifra de Cesar")
	
	parser.add_argument('-t', action = 'store', dest = 'frase', required = True,
					  default = 'Uma frase eh necessaria para a criptografia/descriptografia',
					  help = 'Frase a ser criptografada/descriptografada')

	parser.add_argument('-c', action = 'store_true', dest = 'opcao', required = False, 
					  default = None,
					  help = 'Criptografa uma frase')

	parser.add_argument('-d', action = 'store_false', dest = 'opcao',  required = False, 
					  default = None,
					  help = 'Descriptografa uma frase')

	parser.add_argument('-k', action = 'store', dest = 'chave', required = False,
					   default = None,
					   help = 'Chave usada para criptografar/descriptografar a frase')

	arguments = parser.parse_args()

	return arguments


def criptografa(frase, chave):
	print(frase,chave)

def descriptografaComChave(frase, chave):
	print("DescComChave")
def descriptografaSemChave(frase):
	print("DescSemChave")

'''
def desenhalogo():
	print("/  ]|    ||     ||    \  /    |    |   \    /  _]       /  ]  /  _]/ ___/ /    ||    \ \n"
  		 "/  /  |  | |   __||  D  )|  o  |    |    \  /  [_       /  /  /  [_(   \_ |  o  ||  D  ) \n"
 		"/  /   |  | |  |_  |    / |     |    |  D  ||    _]     /  /  |    _]\__  ||     ||    / \n" 
	   "/   \_  |  | |   _] |    \ |  _  |    |     ||   [_     /   \_ |   [_ /  \ ||  _  ||    \ \n"	
	   "\     | |  | |  |   |  .  \|  |  |    |     ||     |    \     ||     |\    ||  |  ||  .  \ \n"
 		"\____||____||__|   |__|\_||__|__|    |_____||_____|     \____||_____| \___||__|__||__|\_| \n")
'''

if __name__ == '__main__':
	arguments = getArguments();

	#desenhalogo()
	
	if(arguments.opcao == True):
		if(arguments.chave != None):
			criptografa(arguments.frase, arguments.chave)
		else:
			print("Para Criptografar uma frase, o uso de uma chave eh obrigatoria")
			exit(1)

	if(arguments.opcao == False):
		if(arguments.chave != None):
			descriptografaComChave(arguments.frase, arguments.chave)
		else:
			descriptografaSemChave(arguments.frase)


