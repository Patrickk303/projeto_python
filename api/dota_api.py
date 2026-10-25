#%%


import requests
import pandas as pd
from tqdm import tqdm


url = "https://api.opendota.com/api/heroes"

resp = requests.get(url)

data =  pd.DataFrame(resp.json())

data.to_csv("heros_dota.csv", sep=";", index=False)