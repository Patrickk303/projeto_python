# Altere o programa anterior para considerar a quantidade de garrafas de água

texto = """
Bem-vindo! Para escolher sua agua é só digitar um número
(1) para água de mineral
(2) água com gás!
"""
print(texto)
opcao = input("Escolha uma garrafa de água : ")
valor_item = 0
if opcao == "1" :
    valor_item = 1.50
elif opcao == "2" :
    valor_item = 2.50


if valor_item == 0:
    print("Pedido recursado!Número errado!")

else :
    qtde = input("quantas garrfas? ")
    qtde = int(qtde)

    total = valor_item * qtde

    print("total a pagar : ", total)