#%%
registros_balanca = [12.5, -3.0, 45.1, 105.0, 8.2, -1.5, 33.4, 112.5, 0.0]

def limpa_dados(lista_suja):
    """
    nesta função vc deve jogar uma lista com numero deve ser tratados
    """
    dados_certos = []
    for i in lista_suja :
        if i > 0 and i < 100 :
            dados_certos.append(i)
    return dados_certos

lista_final_limpa = limpa_dados(registros_balanca)

print("A lista pronta para análise é:", lista_final_limpa)