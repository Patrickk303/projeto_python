
#%%

prato = 15

payload_api = {
    "status": "sucesso",
    "unidade": "Matriz",
    "registros": [
        {"nome": "Carlos", "setor": "Operacional", "refeicoes": 5},
        {"nome": "Ana", "setor": "Administrativo", "refeicoes": 2},
        {"nome": "Roberto", "setor": "Operacional", "refeicoes": 4},
        {"nome": "Mariana", "setor": "Diretoria", "refeicoes": 1},
        {"nome": "João", "setor": "Operacional", "refeicoes": 6}
    ]
}

relatorio_geral = {}

for funcionario in payload_api["registros"]:
    setor = funcionario["setor"]
    qtede_rei = funcionario["refeicoes"]
    if setor in relatorio_geral :
        relatorio_geral[setor] += qtede_rei
    else :
        relatorio_geral[setor] = qtede_rei

for setor, total_refeicao in relatorio_geral.items() :
    gasto = total_refeicao * prato
    print(f"o setor {setor} gastou um total de {gasto} com alimentação")


