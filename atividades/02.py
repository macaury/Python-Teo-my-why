#%%
import pandas as pd

import numpy as np


#%%

# 05.01 | Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch

# não entendi


#%%

# Aplique o log na coluna de saldo de pontos, criando uma coluna nova

df_clientes = pd.read_csv("../data/clientes.csv",sep=";")

#%%

df_clientes["log_qtdPontos"] = np.log(df_clientes["QtdePontos"]+1)


# %%

df_clientes



#%%

# 05.03 | Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.


df_clientes["vinculo_social_media"] = (df_clientes['FlTwitch']==1) +(df_clientes['FlYouTube']==1) + (df_clientes['FlBlueSky']==1) + (df_clientes['FlInstagram']==1) 

df_clientes[df_clientes["vinculo_social_media"]]

#%%

# Qual é o id de cliente que tem maior saldo de pontos? E o menor?

maior_pontuador = df_clientes["QtdePontos"].max()
maior_pontuador = df_clientes["QtdePontos"] == maior_pontuador
df_clientes[maior_pontuador] ## Cliente com mais pontos
menor_pontuador = df_clientes["QtdePontos"] == 1
df_clientes[menor_pontuador]


#%%

df_transacoes = pd.read_csv("../data/transacoes.csv",sep=";")
df_transacoes["DtCriacao"] = df_transacoes["DtCriacao"].str.replace(" +0000 UTC",'')

df_transacoes["Data_criacao"] = (pd.to_datetime(
    df_transacoes["DtCriacao"], format='mixed',utc=True)).dt.date

df_transacoes["Data_criacao"]

df_transacoes = df_transacoes.sort_values(by=["IdCliente","Data_criacao"],ascending=False) 
duplicados = df_transacoes.drop_duplicates(keep="first",subset=["IdCliente","Data_criacao"])

duplicados
# %%
