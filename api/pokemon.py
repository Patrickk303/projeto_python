
#%%
import requests
import json


url = "https://pokeapi.co/api/v2/pokemon/pikachu"


resultado = requests.get(url)

dados = resultado.json()
# %%

if resultado.status_code == 200 :
    with open("pikachu.json", mode="w", encoding="utf-8") as open_file :
        json.dump(dados, open_file, ensure_ascii=False, indent=4)