
orcamento = float(input("orçamento para o mês : "))
gasto = float(input("gastos até o momento : "))
dias = int(input("quantos dias faltam para acabar o mês :"))

real = orcamento - gasto
teto = real / dias

print("teto para proximos dias : ", teto)

## medidor de gastos

while True :
    valor = input("digite o gasto do dia : ")
    valor = float(valor)
    if valor > teto :
        print("não pode gastar")
    elif valor <= teto :
        print("pode gastar")
        teto -= valor
        print("novo teto", teto)
    else :
        break