
def par(numero:int):
    if numero % 2 == 0 :
        return "par"
    else:
        return "ímpar"


numero = input("entre com um numero :")
numero = int(numero)

resultado = par(numero)

print("sua numero ", numero, "é ", resultado)