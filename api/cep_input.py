#%%

import requests

cep = input("digite seu cep : ")

url = "https://viacep.com.br/ws/{cep_api}/json/"
resposta_api = requests.get(url.format(cep_api=cep))
endereco =  resposta_api.json()

dados = dict()

if resposta_api.status_code == 200 :
    dados = endereco


for chave, valor in dados.items() :
    print(chave,"->", valor)