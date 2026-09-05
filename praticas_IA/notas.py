
# Promotores: Clientes que deram nota 9 ou 10.
# Detratores: Clientes que deram nota 6 ou menor.
# Neutros: Clientes que deram nota 7 ou 8.

Promotores = 0
Detratores = 0
Neutros = 0

notas_clientes = [8, 10, 5, 9, 7, 10, 4, 9, 6, 10]


for i in notas_clientes :
    if i >= 9 :
        Promotores += 1
    elif i >= 7 :
        Neutros += 1
    else :
        Detratores += 1

soma_total = sum(notas_clientes)
media = soma_total / len(notas_clientes)

print(f"Total de Promotres : {Promotores}, total de Detratores : {Detratores} e total de neutros : {Neutros}")
print(f"Total da média é {media}")