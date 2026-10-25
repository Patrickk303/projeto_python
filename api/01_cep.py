#%%
import requests # para requisição na internet
import json # para tratar json de lista/dicionarios para arquivos
from tqdm import tqdm
import pandas as pd
#%%
# cep para trabalhar na api
ceps = [
    "01519000",
    "13329120",
    "21870370",
    "14400760",
    "21645522",
    "13600110",
    "21051090",
    "09656000",
    "53420160",
    "01311902",
    "13476863",
    "19060100",
    "58038200"
]

# criando uma variavel e deixando um valor dela indexado
url = "https://viacep.com.br/ws/{cep}/json/"
dados = []
# criando um for para percorretor por todos os ceps
for i in tqdm(ceps) :
    # criando uma varivel para guardar o resultado da consulta da api
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200 :
    # uso o if para confirmar se foi dado correto a chamada da api
        dados.append(resposta.json())

#%%
datset = pd.DataFrame(dados)
datset.to_csv("cep.csv", sep=";")


#%%
# abrindo um arquivo em modo de escrita e usando a biblioteca do json com o dumo para colocar os dados dentro do arquivo
# dentro da varivel e com as configuraçoes de formatação
with open("cep.json",mode="w", encoding='latin-1') as open_file:
    json.dump(dados,open_file, ensure_ascii=False, indent=4)