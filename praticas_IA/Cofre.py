#%%
# código par revisar entendimento de do laço for com um caso de
# cofre de dinheiro
cofre = int(input("Digite um Valor para guardar : "))
saldo = 0
print("Relátorio financeiro")
for i in range (1,31):
    saldo += cofre
    print("Dia", i, "Total no cofre : ", saldo)



