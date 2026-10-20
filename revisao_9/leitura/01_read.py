#%%

nome_arquivo =  "historia.txt"

with open("historia.txt") as arquivo :
    conteudo = arquivo.read()

print(conteudo)




#%%
nome_arquivo =  "historia.txt"

open_file = open(nome_arquivo)

print(open_file)