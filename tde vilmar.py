#vou fazer em inglês com explicação para treinar

# siga os passos, primeiro a opção 1 , depois 1 

# escreva a mensagem e gere os códigos

# depois receba a mensagem pela opção 2 com a alice

# depois digite o K_sessão gerado por bob corretamente

# depois o código %*#@& que é o primeiro nounce key gerado automático pelo sistema

# a frase será gerada criptografada e em linhas

# depois só escrever para o bob pela opção 2 

import random 

def cryptography_bob(phrase):

  #4 A chave de sessão deve ser obtida através de uma comunicação criptografada com o KDC, utilizando a chave mestre;
  
  keysessão = ""
  
  for letter in phrase:
  
     # 5 Quando ambas entidades possuírem a chave de sessão, Bob gera um nonce e encaminha para Alice, cifrando na K_sessão aqui será criado o nounce junto com a frase;
  
    if letter in "poiuytrewqPOIUYTREWQ":
  
      keysessão = keysessão + "%"
  
    if letter in "çlkjhgfdsaÇLKJHGFDSA":
  
      keysessão = keysessão + "*"
  
    if letter in "mnbvcxzMNBVCXZ":
  
      keysessão = keysessão + "#"
  
    if letter in "0987654321":
  
      keysessão = keysessão + "@"
  
    if letter in "!@#$%¨&*()":
  
      keysessão = keysessão + "&"
  
    else: 
  
      keysessão = keysessão + letter
  
  return keysessão

def cryptography_alice(phrase):

  new_key = ""

  for new_letter in phrase:

    if new_letter in "poiuytrewqPOIUYTREWQ":

      new_key = new_key + "%"

    if new_letter in "çlkjhgfdsaÇLKJHGFDSA":

      new_key = new_key + "*"

    if new_letter in "mnbvcxzMNBVCXZ":

      new_key = new_key + "#"

    if new_letter in "0987654321":

      new_key = new_key + "@"

    if new_letter in "!@#$%¨&*()":

      new_key = new_key + "&"

    else: 

      new_key = new_key + new_letter

  return new_key

def word_remove(word, remove):

    size_remove = len(remove)

    size_word = len(word)

    while True:

        position_remove = word.find(remove)

        if position_remove != -1:

            start_word = word[0:position_remove]

            end_word = word[position_remove+size_remove:size_word]

            word = start_word + end_word

        else:

            break

    return word

menu=''

K_sessão = 0

new_nounce_alice = 0

K_alice_new = ''

while menu != '3':

  print("Type the option")

  print("\t 1 - Type for generate a K_sessão and K_bob phrase")

  print("\t 2 - start K_Alice section and create a new nounce")

  menu = input()

# 3 Bob e Alice devem conversar através de uma chave de sessão (K_sessão);

  if menu == '1':

    menu_bob=''

    while menu_bob != 3:

      print("1 - Written for Alice")

      print("2 - Receive of Alice")

      menu_bob = input()

      if menu_bob == '1':

        from random import randint

        # 1 Bob e o KDC devem compartilhar uma chave mestre: K_bob;

        # Aqui será gerado a chave mestre e a frase de bob. Essa chave mestre alice deverá conter.

        K_sessão = randint(0,100000)

        print("Your K_sessão is {}".format(K_sessão))

        K_bob = cryptography_bob(input("type your phrase K_bob for KDC "))

        print("Your Nounce is '%*#@&', you must put on before each letter of your sentence")

      if menu_bob == '2':

        if new_nounce_alice == 0:

          print("You not has mensage")

        else:

          new_nounce = input("type the new nounce")

          # 7. Bob compara o valor recebido com o valor de nonce enviado realizando a função;

          if new_nounce == new_nounce_alice:

            print("New nounce correct")

            print(K_bob)

            print("---")

            print("deciphering")

            print("---")

            words = K_alice_new

            word_for_remove_two = ["@", "#", "%", "&", "*"]

            for wordss in words:

                finish_two = wordss

                for remove_2 in word_for_remove_two:

                    finish_two = word_remove(finish_two, remove_2)

                print(finish_two)

      break 

  elif menu == '2':

    menu_alice=''

    print("1 - Written for bob")

    print("2 - Receive of bob")

    menu_alice = input("Type")

    if menu_alice == '1':

        #6. Alice responde Bob executando uma função sobre o nonce recebido, cifrando na K_sessão;

      from random import randint

      new_nounce_alice = randint(0,100000)

      K_alice_new = cryptography_alice(input("type your phrase K_alice for KDC "))

      print("Your new nounce is {}, you must put on before each letter of your sentence".format(new_nounce_alice))

    if menu_alice == '2':

      K_aliceSessão = int(input("Type the Key sessão generated for Bob"))

        # 2 Alice e o KDC devem compartilhar uma chave mestre: K_alice; aqui a comprovação de que alice a bob compartilham dessa chave

      if K_aliceSessão == K_sessão:

        print("K_sessão correct")

        nounce = input("Press the nounce key")

        if nounce == '%*#@&':

          print(K_bob)

          print("---")

          print("deciphering")

          print("---")

          words = K_bob

          word_for_remove = ["@", "#", "%", "&", "*"]

          for word in words:

              finish = word

              for remove in word_for_remove:

                  finish = word_remove(finish, remove)

              print(finish)

        else:

          print("Nounce incorrect")

    else:

      print("K_sessão incorrect")

  else:

    print("incorret")
  
  menu = input("Type Enter")