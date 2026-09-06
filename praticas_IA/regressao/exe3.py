

#%%
compras = [["Operacional", 150.0], ["Administrativo", 300.0], ["Operacional", 50.0], ["Diretoria", 120.0], ["Administrativo", 100.0]]

gastos_agrupados = {}

for setor, gastos in compras:
    if setor in gastos_agrupados :
        gastos_agrupados[setor] += gastos
    else :
        gastos_agrupados[setor] = gastos

print(gastos_agrupados)