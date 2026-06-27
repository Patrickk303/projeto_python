# 🍕 Desafio: Sistema de Pedidos de uma Pizzaria
# Escreva um programa em Python que simule o pedido de uma pizzaria. O programa deve seguir os seguintes passos:
# 1. O Menu inicial:
# Mostre para o usuário uma mensagem de boas-vindas e um menu com 3 opções de sabores de pizza e seus preços:
# (1) Calabresa - R$ 25.00
# (2) Mussarela - R$ 20.00
# (3) Marguerita - R$ 22.00
# 2. A Escolha da Pizza:
# Peça para o usuário digitar o número da pizza que ele quer.
# 3. Validação e Preço:
# Usando if / elif / else, defina o preço da pizza escolhida.
# Se o usuário digitar um número que não seja 1, 2 ou 3, o valor do item deve ser 0.
# 4. Quantidade ou Erro:
# Faça uma verificação:
# Se o valor da pizza for 0, mostre a mensagem: "Opção inválida! Pedido cancelado."
# Caso contrário, pergunte quantas pizzas o usuário quer (lembre-se de converter para número inteiro).
# 5. A Novidade (Taxa de Entrega):
# Calcule o valor total parcial (preço da pizza multiplicado pela quantidade).
# Agora, pergunte ao usuário se ele quer entrega em domicílio: digite (1) para SIM ou (2) para NÃO.
# Se ele escolher 1 (SIM), adicione 5.00 (cinco reais da taxa de entrega) ao valor total.
# 6. Finalização:
# Por fim, imprima na tela o valor total final que o cliente deve pagar.


# texto para print
texto1 = """
Bem-vindo a Pizzaria!!
Escolha a sua pizza! Basta digitar um número!
(1) Calabresa - R$ 25.00
(2) Mussarela - R$ 20.00
(3) Marguerita - R$ 22.00
"""
texto2 = """
Você deseja entrega em domicílio?
(1) Sim
(2) Não
"""

# Bloco de código para selecionar a pizza e exibir o resultado
print(texto1)
valor_pizza = 0
opcao = input("Digite um número : ")
if opcao == "1":
    valor_pizza = 25.00
    print("Pizza selecionada : Calabresa")
elif opcao == "2":
    valor_pizza = 20.00
    print("Pizza selecionada : Mussarela")
elif opcao == "3":
    valor_pizza = 22.00
    print("Pizza selecionada : Marguerita")
# Validação da entrada do usuario
if valor_pizza == 0:
    print("opção inválida! Pedido cancelado.")
else :
# QTDE de pizza
    qtde = int(input("Quantas pizzas você deseja? :"))
    total_pizza = qtde * valor_pizza  
    #variaveis
    frete = 0  
    #estrutura de lógica de frete
    opcao2 = input(texto2)
    if opcao2 == "1":
        frete = 5
    elif opcao2 == "2":
        frete = 0
    else :
        frete = -1
# Validação do usuairo
    total = total_pizza + frete 
    if frete == -1 :
        print("opção inválida! Pedido cancelado.")
    else :
        print("total a pagar R$", total)