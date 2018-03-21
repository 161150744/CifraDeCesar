import os
import platform

try:
	import colorama
	from colorama import Fore, Back, Style
except ImportError:
	print("ERRO! - Necessario biblioteca COLORAMA \n Instale com - easy_install colorama")

colorama.init()

def desenhaBanner():
	banner = """
 ██████╗██╗███████╗██████╗  █████╗     ██████╗ ███████╗     ██████╗███████╗███████╗ █████╗ ██████╗ 
██╔════╝██║██╔════╝██╔══██╗██╔══██╗    ██╔══██╗██╔════╝    ██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗
██║     ██║█████╗  ██████╔╝███████║    ██║  ██║█████╗      ██║     █████╗  ███████╗███████║██████╔╝
██║     ██║██╔══╝  ██╔══██╗██╔══██║    ██║  ██║██╔══╝      ██║     ██╔══╝  ╚════██║██╔══██║██╔══██╗
╚██████╗██║██║     ██║  ██║██║  ██║    ██████╔╝███████╗    ╚██████╗███████╗███████║██║  ██║██║  ██║
 ╚═════╝╚═╝╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝    ╚═════╝ ╚══════╝     ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝
 			Criado por Felipe Homrich Melchior - UNIPAMPA
 	        		www.homdreen.github.io
 			caesarcipher.py --help para mais funções

 			- [1] - CRIPTOGRAFAR
 			- [2] - DESCRIPTOGRAFAR SEM CHAVE
 			- [3] - DESCRIPTOGRAFAR COM CHAVE"""

	print(Fore.WHITE+banner)

def main():
	so = platform.system()
	if(so == "Windows"):
		os.system("cls")
	else:
		os.system("clear")

	desenhaBanner()

if __name__ == '__main__':
	main()