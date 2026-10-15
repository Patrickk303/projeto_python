

#%%
#exercício 1
print("digite os valore das variaveis")
a = int(input("digite o valor A"))
b = int(input("digite o valor B"))

print("soma = ", a + b)
print("diferença = ", a - b)
print("produto = ", a * b)
print("média aritmética = ", (a + b)/2)

#%%
#exercício 2
nota = int(input("Digite a sua nota :"))

if nota >= 7 :
    print("aprovado")
elif nota > 5 :
    print("recuperação")
else :
    print("reprovado")

#%%
#exercício 3
coordenadas = (-3.7319, -38.5267)
latitudade, longitude = coordenadas
print(f"latitudade : {latitudade}")
print(f"longitudade : {longitude}")

#%%
##exercício 4

for i in range(21) :
    if i % 2 == 0 :
        print(i)