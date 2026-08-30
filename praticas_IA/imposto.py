#%%

item1 = {
    "nome" : "Barbie",
    "preco" :50,
    "quantidade" : 2
}

item2 = {
    "nome" : "mclaren mp4",
    "preco" :100,
    "quantidade" : 1
}

item3 = {
    "nome" : "pirulito",
    "preco" :0.25,
    "quantidade" : 3
}

pedido = [item1, item2, item3]
subtotal_final = 0
contador = 0

for item in pedido :
    subtotal_item = item["preco"] * item["quantidade"]
    subtotal_final = subtotal_item + subtotal_final
    contador += item["quantidade"]
    print(item["nome"], "-> suntotal", subtotal_item)
    print("total da sua compra deu : ", subtotal_final)

if contador <= 4:
    percentual_desconto = 0
elif contador <= 9:
    percentual_desconto = 0.05
else:
    percentual_desconto = 0.10

print("seu total desconto é ", percentual_desconto)

valor_desconto = subtotal_final * percentual_desconto
subtotal_total_desconto = subtotal_final - valor_desconto

def calcular_imposto(subtotal, **imposto):
    total_imposto = 0
    for nome_imposto in imposto :
        valor_imposto = subtotal * imposto[nome_imposto]
        print("Imposto", nome_imposto, "-> R$", valor_imposto)
        total_imposto = total_imposto + valor_imposto
    return total_imposto

imposto_a_pagar = calcular_imposto(subtotal_total_desconto, icms=0.05, muncipal=0.02)


def calcular_frete(compra):
    frete = 0
    if compra > 200 :
        frete = 0
    else :
        frete = 15
    return frete

valor_frete = calcular_frete(subtotal_total_desconto)
print("Valor do frete -> R$", valor_frete)

total_final = subtotal_total_desconto + imposto_a_pagar + valor_frete

print("total a pagar no caixa", total_final)