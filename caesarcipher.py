import sys
import os
import platform

from banner_script import *

def limpaTela():
	so = platform.system()
	if(so == "Windows"):
		os.system("cls")
	else:
		os.system("clear")

def criptografa():
	limpaTela()
	desenhaCript()

	try:
		texto = input("Digite o texto para ser criptografado => ").upper()
	except ValueError:
		print("ERRO! - A entrada deve ser um texto/frase")


	try:
		chave = int(input("Digite a chave para ser na criptografado => "))
	except ValueError:
		print("ERRO! - A chave deve ser um número")

	if((chave < 0) or (chave > 26)):
		print("ERRO! - A chave deve ser um numero valido em relação ao alfabeto")
		sys.exit()

	lista = [texto]

	for i in lista:
		print(i)


def descriptografaSemChave():
	limpaTela()
	desenhaDecript()


def descriptografaComChave():
	limpaTela()
	desenhaDecriptKey()

def menu(opcao):
	if(opcao == 1):
		print("Criptografa")
		criptografa()
	elif(opcao == 2):
		print("DSC")
		descriptografaSemChave()
	elif(opcao == 3):
		print("DCC")
		#descriptografaComChave()
	else:
		print("Até a próxima!")
		sys.exit()


def main():
	limpaTela()

	desenhaBanner()

	try:
		opcao = int(input("Digite a opcao desejada => "))
	except ValueError:
		print("ERRO! - O valor deve ser um numero inteiro!")

	menu(opcao)

if __name__ == '__main__':
	main()