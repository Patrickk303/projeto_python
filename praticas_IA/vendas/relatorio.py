

#%%

arquivo = "vendas.csv"

with open(arquivo) as openfile :
    arquivo = openfile.readlines()

print(arquivo)

banco = dict()

chaves = arquivo[0].strip("\n").split(";")

print(chaves)

for c in chaves :
    banco[c] = []

# %%


for lista in arquivo[1:]:
    valores = lista.strip("\n").split(";")
    for i in range(len(valores)) :
        banco[chaves[i]].append(valores[i])


# %%
