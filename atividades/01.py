#%%

import pandas as pd 

#%%

df = pd.read_csv("../data/clientes.csv",sep=";")

df.head()
# %%
# Clientes com vinculos com a twitch
clientes_twitch = df["FlTwitch"]==1

clientes_twitch = df["FlTwitch"][clientes_twitch].count()
clientes_twitch  # quantidade dos clientes


#%%

# clientes com pontos acima de 1000
cliente_maio_1000 = df["QtdePontos"] >= 1000

cliente_maio_1000 = df["QtdePontos"][cliente_maio_1000].count()

cliente_maio_1000 # quantidade dos pontos

#%%

# Quantas transações ocorreram no dia 2025-02-01? 

# nem uma 

df["DtCriacao"] = pd.to_datetime(df["DtCriacao"], format="mixed")


trans_dia = (df["DtCriacao"].dt.year == 2025) & (df["DtCriacao"].dt.month == 2) & (df["DtCriacao"].dt.day == 3)


df[trans_dia]


# %%
