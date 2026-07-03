
#%%
soma = 0
qtde_entradas = 4

for i in range (qtde_entradas):
    altura = input("digete a sua altura")
    altura = float(altura)
    soma += altura

print("soma das altura ", soma)