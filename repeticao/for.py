# %%
nome = "Patrick"

for letra in nome :
    print(letra)


# %%

numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "x", i, "=", numero * i)

#%%

# Quais números são divisiveis por 4
# no intervalo de [4-100] ?


for i in range(1, 101):
    if i % 4 == 0:
        print(i)