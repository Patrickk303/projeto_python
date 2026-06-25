# Altere o programa anterior para considerar a quantidade de garrafas de água

texto = """
Bem-vindo! Para escolher sua agua é só digitar um número
(1) para água de mineral
(2) água com gás!
"""
print(texto)
opcao = input("Escolha uma garrafa de água : ")
quatidade = int(input("Quantas garrfas você quer? "))
 = 0
if opcao == "1" :
    conta = 1.50
elif opcao == "2" :
    conta = 2.50

total = conta * quatidade


if conta == 0:
    print("Pedido recursado!Número errado!")
else :
    print("Pedido feito! Pague R$", total)