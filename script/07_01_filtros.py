#%%
import pandas as pd

df = pd.read_csv("../data/transacao_produto.csv",sep=";")

filtros = (df["IdProduto"] == 5  )| (df["IdProduto"] == 11  )

produtos_5_e_11 =  df[filtros]["IdProduto"].count()

#%%

filtro = df["IdProduto"].isin([5,11])

df[filtro]

#%%

#data de crição valida

df = pd.read_csv("../data/clientes.csv",sep=";")

df.head()

filtro = df["DtCriacao"].notnull()


df[filtro]


#%%
# exercicios

tabelea_result = []

# 1 | quantos clientes tem vinculo com a twitch ?

filtro_twitch = df["FlTwitch"].isin([1])


clientes_twitch = (df[filtro_twitch]["FlTwitch"]).count()

clientes_twitch

#%%

# 2 | quantos clientes possuem mais de 1000 pontos

filtro_pontos = df["QtdePontos"] >= 1000

df[filtro_pontos]


#%%

# 3 |

df_transacoes = pd.read_csv("../data/transacoes.csv",sep=";")

filtro_dia = df_transacoes["DtCriacao"] >= "2025-02-01"

transacoes = df_transacoes[filtro_dia]["DtCriacao"].count()

print(transacoes)



# %%
