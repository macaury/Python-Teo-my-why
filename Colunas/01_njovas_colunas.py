#%%
import numpy as np
import pandas as pd

df = pd.read_csv("../data/clientes.csv",sep=";")
df.head()

#%%
df["novos_pontos"]= df["QtdePontos"]+100


df.head()

#%%

df["cliente_verificado"] = (df["FlTwitch"] == 1 ) & (df["FlEmail"] == 1)



df["cliente_verificado"].sort_values()


# %%


df["qutdSocial"] = (df["FlEmail"] + df["FlTwitch"] + df["FlYouTube"] + df["FlBlueSky"] + df["FlInstagram"])

filtro  = df["qutdSocial"] >= 1

df[filtro]

#%%

df["todas_sociais"] = (df["FlEmail"]* df["FlTwitch"]* df["FlYouTube"]* df["FlBlueSky"]* df["FlInstagram"])


df["todas_sociais"]


#%%

df["log_pontos"]= np.log( df["QtdePontos"]+1)

df["log_pontos"].describe()