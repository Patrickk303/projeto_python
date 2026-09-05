
#%%
total_gasto = 0
notas_equipe = {"Helder": 9.5, "Ana": 7.0, "Carlos": 4.0, "Mariana": 8.5}
for nome, nota in notas_equipe.items():
    bonus = 500
    if nota >= 9.0 :
        bonus += 300
    elif nota >= 5.0 and nota <= 8.9:
        bonus = bonus
    else :
        bonus = bonus / 2
    total_gasto += bonus
    print(f"O bônus de {nome} será de R$ {bonus}")
print(f"total de gosto com bonus : {total_gasto}")