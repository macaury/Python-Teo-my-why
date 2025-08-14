#%%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")

clientes

#%%

clientes = clientes.dropna(how='any')

clientes
# %%

df = pd.DataFrame(
    {
        "nome" : [None,None,"mah"],
        "idade": [None,20,34],
        
    }
)

df.dropna(how='any',subset=["idade","nome"])

#%%

#df["idade"].fillna(0)  # substituindo Nan

df.fillna({
    "nome":"Sem nome","idade": 0
})

