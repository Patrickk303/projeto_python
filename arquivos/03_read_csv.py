
#%%
arquivo = "data.csv"


with open(arquivo) as open_file :
    lines = open_file.readlines()

print(lines)

#%%

chave = lines[0].strip("\n").split(";")
dados = dict()

for c in chave :
    dados[c] = []

dados


#%%

for l in lines[1:]:
    valores = l.strip("\n").split(";")
    for i in range(len(valores)):
        dados[chave[i]].append(valores[i])

dados