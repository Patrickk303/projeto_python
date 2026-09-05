
#%%
registros_balanca = [12.5, -3.0, 45.1, 105.0, 8.2, -1.5, 33.4, 112.5, 0.0]
dados_certos = []
dados_errados = []


for i in registros_balanca :
    if i < 0 or i > 100 :
        dados_errados.append(i)
    else :
        dados_certos.append(i)

errados = len(dados_errados)
certos = len(dados_certos)

print(f"Numero de acertos : {certos}, numero de erros : {errados}")
