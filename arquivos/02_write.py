#%%

nome_arquivo = "historia2.txt"
txt = "meu novo arquivo de teste!!\n"

with open(nome_arquivo, mode="a") as open_file:
    open_file.write(txt)
