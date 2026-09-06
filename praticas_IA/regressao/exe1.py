
#%%
contador_operacao = 0
equipe = [
    {"nome": "Carlos", "setor": "Operacional"},
    {"nome": "Ana", "setor": "Administrativo"},
    {"nome": "Roberto", "setor": "Operacional"}
]


for funcionario in equipe :
    setor_atual = funcionario["setor"]
    nome_pesssoa = funcionario["nome"]
    if setor_atual == "Operacional":
        contador_operacao += 1
        print(f"{nome_pesssoa} pertence ao setor {setor_atual}")

print(f"numero de pessoas na operação {contador_operacao}")