
#%%

import pandas as pd

df = pd.read_csv("../data/clientes.csv",sep=";")


#%%

# importando from url

import pandas as pd

dfs = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")

df_uf = dfs[1]

df_uf.to_csv("Listagem_dos_estados.csv",sep=';', index=False)

tabela_uf = pd.read_csv("Listagem_dos_estados.csv", sep=";")

print(tabela_uf)
# %%
