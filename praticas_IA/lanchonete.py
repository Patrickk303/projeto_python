

#%%
cardapio = {
    'x-burguer':12.00,
    'suco':6.00,
    'batata frita':8.00
}
conta = 0
contador = {}

print("""
    Bem-vindo!!!\n
    Escolha um item do cardápio :\n
    x-burguer:12.00\n
    suco:6.00\n
    batata frita:8.00\n
""")

while True :
    pedido = input("Faça seu pedido : ")
    if pedido == "":
        break
    elif pedido in cardapio:
        conta += cardapio[pedido]
        print("pedido registrado")
        if pedido not in contador :
            contador[pedido] = 1
        else :
            contador[pedido] += 1
    else :
        print("""
        digite um item do menu!!\n
        seu animal!!
        """)


print("Total da conta :",conta)

for item, qtd in contador.items() :
    print(item, ":", qtd)

