#%%
# Uma maneira de definir lista
idade = [19, 28, 43, 35, 49, 16, 23]
print(idade)

#%%
patrick = ["namorando", "doom", 19, 1.75, "Calixto", False]
print(patrick)


#%%
type(patrick)

#%%
# tem filhos?
print(patrick[5])
# estado
print(patrick[0])
# Sobrenome
print(patrick[4])


#%%

idade = [19, 28, 43, 35, 49, 16, 23, 10,25,10,25,17]
print("Soma das idade : ",sum(idade))
print("numero de idade :", len(idade))
print("Média das idade : ",sum(idade)/len(idade))
print("Menor das idade : ",min(idade))
print("Maior das idade : ",max(idade))
