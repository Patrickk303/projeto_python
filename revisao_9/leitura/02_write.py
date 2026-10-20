

#%%
txt = "\nteste com o barra"

nome_arquivo = "historia_02.txt"

with open("historia_02.txt",mode="a") as open_file:
    open_file.write(txt)

