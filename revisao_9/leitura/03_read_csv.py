


#%%


arquivo = "data.csv"

with open(arquivo) as open_file :
    lines = open_file.readlines()


#%%

dados = dict()

chaves = lines[0].strip("\n").split(";")

for c in chaves :
    dados[c] = []

#%%

# percorrendo todas as linhas a partir da segunda
for l in lines[1:] :
# entrou no laço vai pegar ela remover o \n e depois quebra os valosres transformando eles de string pra uma lista 
    valores = l.strip("\n").split(";")

    for i in range(len(valores)) :
        dados[chaves[i]].append(valores[i])

dados