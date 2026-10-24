

contagem = 0
num = 7

def vali_input():
    while True :
        try :
            num_user = int(input("Digte um numero :"))
        except ValueError as err :
            print("valor invalido!")
            continue

        if 1 <= num_user <= 15 :
            break
        else :
            print("valor precisa está entre 1 e 15")
    return num_user

while True :
    num_user = vali_input()

    if num_user == num :
        print("parabéns vc acertou")
        break
    elif num_user > num :
        print("o numero que vc escolheu é maior do que o numero correto")
        print("você sõ tem mais ", 2 - contagem,"chances")
        contagem += 1
    else :
        print("o numero que vc escolheu é menor do que o numero correto")
        print("você sõ tem mais ", 2 - contagem,"chances")
        contagem += 1
    if contagem == 3 :
        print("vc perdeu")
        break
