#%%

def agrupar_horas (api_serlares):
    """
    em api_serlares se deve ser um dicionario da api da empresa. a api
    puxa os dados da chave registro e faz a descompactação e puxar os
    projetos e suas horas
    """
    total_horas_projeto = {}
    for agrupar_horas in api_serlares["registros"] :
        setor = agrupar_horas['projeto']
        qtde_h = agrupar_horas['horas']
        if setor in total_horas_projeto :
            total_horas_projeto[setor] += qtde_h
        else :
            total_horas_projeto[setor] = qtde_h
    return total_horas_projeto

payload_horas = {
    "empresa": "Serlares",
    "departamento": "TI e Dados",
    "registros": [
        {"engenheiro": "Helder", "projeto": "Pipeline n8n", "horas": 4},
        {"engenheiro": "Carlos", "projeto": "Dashboard BI", "horas": 3},
        {"engenheiro": "Helder", "projeto": "Pipeline n8n", "horas": 2},
        {"engenheiro": "Ana", "projeto": "Dashboard BI", "horas": 5},
        {"engenheiro": "Carlos", "projeto": "Migração SQL", "horas": 4}
    ]
}

valor_hora = 50.0

teste = agrupar_horas(payload_horas)

for grupo, valor_total in teste.items():
    final = valor_hora * valor_total
    print(f"o projeto {grupo} vai ter uma folha de {final}")