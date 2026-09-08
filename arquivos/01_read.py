

#%%
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file :
    conteudo = open_file.read()
print(conteudo)




#%%
# abre o arquivo
open_file = open(nome_arquivo)

# processa os dados e pode exibir
conteudo = open_file.read()
print(conteudo)

# fecha o arquivo para não prejudicar a integridade dele
open_file.close()