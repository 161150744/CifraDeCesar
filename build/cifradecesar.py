#!usr/bin/python

import sys
import os
import platform

from banner_script import *
from cifra import *

def limpaTela(): # Funcao usada para limpar a tela no windows e nos outros SO
	so = platform.system()
	if(so == "Windows"):
		os.system("cls")
	else:
		os.system("clear")

def criptografa(): # Funcao que criptografa o texto com uma chave
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

	resultado = list(texto)

	if((chave < 0) or (chave > 26)):
		print("ERRO! - A chave deve ser um numero valido em relação ao alfabeto")
		sys.exit()

	for i in range(0, len(texto)):
		resultado[i] = cifra(texto[i], chave, 1)

	print()
	print(Fore.YELLOW+"O Texto cifrado é esse =>", Fore.WHITE+"".join(resultado))

def criptografaROT13(): # Funcao que criptografa com chave 13, padrao da ROT13
	limpaTela()
	desenhaCriptROT13()

	chave = 13

	try:
		texto = input("Digite o texto para ser criptografado => ").upper()
	except ValueError:
		print("ERRO! - A entrada deve ser um texto/frase")

	resultado = list(texto)

	for i in range(0, len(texto)):
		resultado[i] = cifra(texto[i], chave, 1)

	print()
	print(Fore.YELLOW+"O Texto cifrado é esse =>", Fore.WHITE+"".join(resultado))


def descriptografaSemChave(): # Funcao que descriptografa sem chave, gerando muitas respostas
	limpaTela()
	desenhaDecript()

	try:
		texto = input("Digite o texto para ser criptografado => ").upper()
	except ValueError:
		print("ERRO! - A entrada deve ser um texto/frase")

	resultado = list(texto)

	for chave in range(0, 26):
		for i in range(0, len(texto)):
			resultado[i] = cifra(texto[i], chave, 2)

		print()
		print(Fore.YELLOW+"O Texto descriptografado com a chave ", chave, " é esse => ", Fore.WHITE+"".join(resultado))


def descriptografaComChave(): # Funcao que descriptografa um texto com uma chave específica
	limpaTela()
	desenhaDecriptKey()

	try:
		texto = input("Digite o texto para ser criptografado => ").upper()
	except ValueError:
		print("ERRO! - A entrada deve ser um texto/frase")

	try:
		chave = int(input("Digite a chave para ser na criptografado => "))
	except ValueError:
		print("ERRO! - A chave deve ser um número")

	resultado = list(texto)

	for i in range(0, len(texto)):
		resultado[i] = cifra(texto[i], chave, 2)

	print()
	print(Fore.YELLOW+"O Texto descriptografado é esse => ", Fore.WHITE+"".join(resultado))

def descriptografaROT13(): # Funcao que descriptografa um texto com uma chave específica
	limpaTela()
	desenhaDecriptKey()

	chave = 13

	try:
		texto = input("Digite o texto para ser criptografado => ").upper()
	except ValueError:
		print("ERRO! - A entrada deve ser um texto/frase")

	resultado = list(texto)

	for i in range(0, len(texto)):
		resultado[i] = cifra(texto[i], chave, 2)

	print()
	print(Fore.YELLOW+"O Texto descriptografado é esse => ", Fore.WHITE+"".join(resultado))


def menu(opcao): # Funcao de tomada de decisao do menu
	if(opcao == 1):
		criptografa()

	elif(opcao == 2):
		criptografaROT13()

	elif(opcao == 3):
		descriptografaSemChave()

	elif(opcao == 4):
		descriptografaComChave()
	
	elif(opcao == 5):
		descriptografaROT13()

	else:
		print("Até a próxima!")
		sys.exit()


def main(): # Funcao main
	limpaTela()

	desenhaBanner()

	try:
		opcao = int(input("Digite a opcao desejada => "))
	except ValueError:
		print("ERRO! - O valor deve ser um numero inteiro!")

	menu(opcao)

if __name__ == '__main__':
	main() # chamada main