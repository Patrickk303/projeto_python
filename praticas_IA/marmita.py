

empresa = input("Qual nome da empresa?")
qtd_marmita = int(input("Quantas marmitas foram vendidas?"))
preco_unit = float(input("Qual preço unitáiro das marmitas?"))


print("responda com S ou N")

tem_frete = input("tem frete?")

if tem_frete == "S":
    frete = float(input("digite o valor do frete"))
else :
    frete = 0

valor_total = qtd_marmita * preco_unit + frete

print("A nota fiscal da empresa ",empresa,"ficou no valor de R$",valor_total)