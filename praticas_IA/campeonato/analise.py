#%%
#bibliotecas usadas
from statistics import mean
from collections import Counter

#%%
# abrindo um arquivo e gerando seus indices
arquivo = "resultado.csv"

with open(arquivo) as open_file :
    conteudo = open_file.readlines()


dicionario_torneio = dict()
chaves = conteudo[0].strip("\n").split(";")

for i in chaves :
    dicionario_torneio[i] = []

dicionario_torneio
# %%
# colocando os dados dentro do dicionario
for i in conteudo[1:] :
    valores = i.strip("\n").split(";")

    for l in range(len(valores)):
        dicionario_torneio[chaves[l]].append(valores[l])

dicionario_torneio

# %%
# estatisticas
# converte os valores da lista em float
pontos = dicionario_torneio["pontuacao"]
pontos = [float(p) for p in pontos]
#%%
# categoria que aparece
categoria = dicionario_torneio["categoria"]
categoria = Counter(categoria)


#%%
total_jogadores = len(dicionario_torneio["nome"])
media_pontos = mean(pontos)
max_pontos = max(pontos)
count_categoria = categoria

# %%

nome_arquivo = "relatorio.txt"
texto = f"""
==================================================
         RELATÓRIO FINAL DO TORNEIO 
==================================================

O torneio foi um sucesso! Tivemos a participação de
um total de {total_jogadores} jogadores que disputaram cada ponto.

Ao final de todas as rodadas, a média de pontos
alcançada pelos competidores foi de {media_pontos} pontos.

O grande destaque do evento foi a pontuação máxima
atingida, onde o topo do ranking cravou {max_pontos} pontos!

Numero de vezes que cada categoria aparece {count_categoria}

==================================================
"""

with open(nome_arquivo, mode="w") as openfile :
    openfile.write(texto)


#%%
with open(nome_arquivo, mode="w") as openfile:
    openfile.write(texto)