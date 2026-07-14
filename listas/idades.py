


#%%

idades = []

while True:
    idade = input("Digte uma idade :")
    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades)/len(idades)
somatotal = sum(idades)
maioridade = max(idades)
menoridade = min(idades)
qtd = len(idades)

print("Estatistica das idades")
print("soma das idades :", somatotal)
print("quantidades das idades :", qtd)
print("média das idades :", media)
print("menor das idades :", menoridade)
print("maior das idades :", maioridade)

