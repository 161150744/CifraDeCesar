#!usr/bin/python

import argparse

def getArguments():
	parse = argparse.ArgumentParser(
		description="Um programa que Criptografa e Descriptografa Cifra de Cesar")
	
	parse.add_argument('--t', action = 'store', dest = 'frase', required = True,
					  default = 'Uma frase eh necessaria para a criptografia/descriptografia',
					  help = 'Frase a ser criptografada/descriptografada')

	parse.add_argument('--c', action = 'store', dest = 'opcao'  required = False, 
					  default = 'Alo',
					  help = 'Criptografa uma frase')

	parse.add_argument('--d', action = 'store', dest = 'opcao'  required = False, 
					  default = 'Alo',
					  help = 'Descriptografa uma frase')

	arguments = parser.parse.args()

	for i in range(0, int(arguments.n)):
		print arguments.t

if __name__ == '__main__':