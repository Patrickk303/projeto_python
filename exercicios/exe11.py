# Escreva um programa que receba uma lista de números do usuário e
# conte quantas vezes um número específico aparece na lista.
# Solicite ao usuário um número e exiba a contagem.
#%%
lista = [2,1,8,3,2,9,1,3,2,9,4,7,9,0,7,3,2]

numero = int(input("Entre com um numero : "))

contador = 0
for i in lista:
    if i == numero:
        contador += 1

print("Quantidade de ", numero, ":", contador)