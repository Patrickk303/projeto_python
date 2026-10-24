

import random

def validar_input() :
    while True :
        try:
            num_use = int(input("Digite seu numero : "))
        except ValueError as err:
            print("valor invalido!")
            continue

        if 1 <= num_use <= 15 :
            return num_use
        print("valor precisa ser entre 1 e 15")

def check_num(sorteio:int,numero:int):
    """descrevendo como essa merda funciona"""
    if numero == sorteio :
        print("parabéns")
        return True
    elif numero > sorteio :
        print("numero muito grande")
        return False
    else :
        print("numero muito pequeno")
        return False

sorteio_numero = random.randint(1,15)


for i in range(3):

    num_use = validar_input()
    if check_num(sorteio=sorteio_numero,numero=num_use):
        break


else :
    print("vc perdeu")

