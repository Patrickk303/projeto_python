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

idade = [19, 28, 43, 35, 49, 16, 23, 10,25,10,25,17, 9]
print("Soma das idade : ",sum(idade))
print("numero de idade :", len(idade)) 
print("Média das idade : ",sum(idade)/len(idade))
print("Menor das idade : ",min(idade))
print("Maior das idade : ",max(idade)) 


#%%

patrick = ["namorando",
            "doom",
            19,
            1.75,
            "Calixto",
            False,
            ["estagiario", "aprendiz", "analista"],
            [600, 700, 1200],
            ["Batman", "Spiderman", "IronMan"]] 

# mostra o tamnho da lista
print("Tamnho de patrick :",len(patrick))
# imprime na saida o primeiro resultado do ultimo objeto da lista
patrick[8][0]
# cria uma variavel com todos os dados da lista que está dentro da lista patrick
herois = patrick[8]
# cria uma variavel que usa os 
segundo_heroi = herois[1]
print(segundo_heroi)

#%%

tamanho = len(patrick)
pos = tamanho - 1
herois = patrick[pos]

patrick[pos][len(herois)-1]

#%%
# o -1 ele pega a ultima, basicamente servindo pra pegar os resultado de trás
# pra frente
patrick[-1][-3]


#%%
# com : é possivel pegar mais de um resultado na lista
patrick[0:4]

#%%
patrick[6][1:3]
patrick[6][-2:]

# patrick[start : stop]

#%%
patrick[7][::-1]
#%%
salarios = patrick[7]
salarios[::2]

# patrick [start : stop : step]