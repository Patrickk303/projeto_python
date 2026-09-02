
#valor base variaveis
valor_base_entregas = 5
bonus_bike = 0
qualidade = 0
total_final =  0
notas =  0
## Avaliador de bonus de entrega

entregas = int(input("Quantas entregas vc fez hoje?"))

print("Qual a média das entregas?\n Digite um valor de 0 a 5")

while True :
    notas = float(input())
    if notas <= 5 :
        break
    elif notas > 5 :
        print("só pode um valor de 0 a 5")

    
print("""
        Qual veiculo vc usou?
        \n digite "1" para carro
        \n digite "2" para moto
        \n digite "3" para bike
        """)


while True :
    veiculos = input()
    if veiculos == "1" :
        veiculos = "carro"
        break
    elif veiculos == "2" :
        veiculos = "moto"
        break
    elif veiculos == "3" :
        veiculos = "bike"
        break
    else :
        print("digite um valor valido")

## regra de volume
if entregas > 20 :
    valor_base_entregas = 6.50

## bonus bike
if veiculos == "bike":
    bonus_bike = 15

valor_entregas = (valor_base_entregas * entregas) + bonus_bike

if notas < 3 :
    qualidade = valor_entregas * 0.10
    total_final = valor_entregas - qualidade
elif notas == 5 :
    qualidade = valor_entregas * 0.20
    total_final = valor_entregas + qualidade
else :
    qualidade = 0
    total_final = valor_entregas + qualidade

print(total_final)

