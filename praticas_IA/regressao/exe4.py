#%%


lotes_producao = [
    ("Unidade Centro", 150),
    ("Unidade Aldeota", 90),
    ("Unidade Centro", 60),
    ("Unidade Beira Mar", 200),
    ("Unidade Aldeota", 120)
]

total_por_unidade = {}

for unidade, vendas in lotes_producao :
    if unidade in total_por_unidade :
        total_por_unidade[unidade] += vendas
    else :
        total_por_unidade[unidade] = vendas

for unidade, vendas in total_por_unidade.items():
    print(unidade, vendas)