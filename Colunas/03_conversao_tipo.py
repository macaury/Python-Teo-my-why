#%%

import pandas as pd

#%%

df = pd.read_csv("../data/clientes.csv",sep=";")

df.head()
#%%


replace = {
      "0000-00-00 00:00:00.000" : "2024-02-01 09:00:00.000"
      }

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace), errors="coerce")



df["DtCriacao"] = df["DtCriacao"].dt.date

df["ano_criacao"] = df["DtCriacao"].dt.year



# %%
