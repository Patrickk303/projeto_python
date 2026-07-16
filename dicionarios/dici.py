#%%

lista = [2, 123, "pt", ["fortaleza", True, 2.1], 5]

lista[3:5]

#%%

# dicionario sáo pares de chave valor

dados_pk = {
    "sobrenome" : "Calixto",
    "nome" : "Patrick", #string
    1 : 123, #inteiros
    "Filhos" : "False", #boleano
    0.23: 26327, #float
    "Formação" : ["analise e desenvolvimento de sistema", "engenharia de dados e big data"], # lista
    "Cargos" : [
        {"nome" : "Jovem aprendiz", "empresa" :"aço cearense"},
        {"nome" : "Estágiario", "empresa" :"Secran"},
        {"nome" : "Estágiario", "empresa" :"Serlares"},
    ]

    }
print(dados_pk)


#%%

dados_pk["Formação"][-1]