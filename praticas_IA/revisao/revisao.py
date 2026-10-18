

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



# exercício 5

#%%
frutas = ["banana","maça","uva","mamão","pera"]

print(frutas)

#%%
frutas.append("tomate")

print(frutas)

#%%

del frutas[1]

print(frutas)

#%%
for i in frutas :
    print(i.upper())




# exercico 6

#%%

produto = {
    "nome" : "Mercedez f1 w11",
    "preço" : "150",
    "estoque" : 79
}

produto["preço"] = 130
produto["categoria"] = "miniatura"

print(f"super promoção do {produto['nome']}\n saindo pela bagatela de {produto['preço']}")


