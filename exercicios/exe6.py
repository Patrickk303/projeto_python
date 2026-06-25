# Faça um programa que vende uma garrafa de água:
# Se o cliente escolher água mineral natural, será cobrado R$1,50
# Se o cliente escolher água mineral com gás, será cobrado R$2,50



texto = """
Bem-vindo! Para escolher sua agua é só digitar um número
(1) para água de mineral
(2) água com gás!
"""
print(texto)
opcao = input("Escolha uma garrafa de água : ")
conta = 0
if opcao == "1" :
    conta = 1.50
elif opcao == "2" :
    conta = 2.50

if conta == 0:
    print("Pedido recursado!Número errado!")
else :
    print("Pedido feito! Pague R$", conta)