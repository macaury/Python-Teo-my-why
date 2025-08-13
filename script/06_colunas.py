#%%

import pandas as pd     

df = pd.read_csv("../data/transacoes.csv",sep=";")

df.head()

#%%

df.shape
# %%

df.info(memory_usage="deep")
#%%
df.dtypes

#%%

df = df.rename(columns={"QtdePontos":"QUDTdePontos"})
#%%
df.rename(columns={"IdCliente":"idcliente"
      
},inplace=True)

#%%

df["idcliente"][:5]
# %%
 
df[["idcliente","QUDTdePontos"]]

#%%
colunas = ["idcliente","QUDTdePontos"]

df[colunas]

# %%

colunas = list(df.columns)

colunas.sort()

df = df[colunas]


# %%

df.head()