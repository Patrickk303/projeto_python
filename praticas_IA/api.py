
#%%
refeicao = 15
valor_total_empresa = 0
relatorio_setores = {}

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

# 1. Primeiro laço: Apenas organiza os dados na estante
for funcionario in payload_api["registros"]:
    nome_setor = funcionario["setor"]
    qtde_refeicao = funcionario["refeicoes"]

    # Usamos o nome_setor sem aspas para acessar a variável
    if nome_setor in relatorio_setores:
        relatorio_setores[nome_setor] += qtde_refeicao 
    else:
        relatorio_setores[nome_setor] = qtde_refeicao

# 2. Segundo laço: Lê as gavetas prontas, calcula o dinheiro e imprime o relatório
for setor, total_refeicoes in relatorio_setores.items():
    custo_do_setor = total_refeicoes * refeicao
    valor_total_empresa += custo_do_setor
    
    print(f"O setor {setor} teve um custo de R$ {custo_do_setor:.2f}")

# O print final encostado na margem esquerda (fora do laço)
print(f"\nO valor total de toda a operação foi de R$ {valor_total_empresa:.2f}")