def cifra(letra, chave, opcao):
     # print(letra, chave)

     alfabeto = { # Dicionario com o alfabeto
          0 : 'A',
          1 : 'B',
          2 : 'C',
          3 : 'D',
          4 : 'E',
          5 : 'F',
          6 : 'G',
          7 : 'H',
          8 : 'I',
          9 : 'J',
          10 : 'K',
          11 : 'L',
          12 : 'M',
          13 : 'N',
          14 : 'O',
          15 : 'P',
          16 : 'Q',
          17 : 'R',
          18 : 'S',
          19 : 'T',
          20 : 'U',
          21 : 'V',
          22 : 'W',
          23 : 'X',
          24 : 'Y',
          25 : 'Z',
          26 : ' '
     }

     for key in alfabeto: # Armazena o indice da letra passada
          if(letra == alfabeto[key]):
               indice_letra = key

     # print(indice_letra)
     if(indice_letra == 26):
               return alfabeto[26]

     if(opcao == 1): # Criptografa
          for i in range(0, chave):
               if((indice_letra + 1) > 26):
                    indice_letra = 0
               indice_letra += 1
               # print(indice_letra)

          return alfabeto[indice_letra]
     
     else: # Descriptografa
          for i in range(0, chave):
               if((indice_letra - 1) < 0):
                    indice_letra = 25
               indice_letra -= 1
               # print(indice_letra)

          return alfabeto[indice_letra]