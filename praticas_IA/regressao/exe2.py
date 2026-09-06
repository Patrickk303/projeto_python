
#%%
acessos = ["Operacional", "Administrativo", "Operacional", "Diretoria", "Operacional"]

estante_setores = {}

for setor in acessos :
    if setor in estante_setores :
        estante_setores[setor] += 1
    else :
        estante_setores[setor] = 1

print(estante_setores)