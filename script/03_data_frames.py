#%%

import pandas as pd

idades = [
      32,38,30,30,31,35,25,29,31,37,
      27,23,36,33,39
]

nome = [
      'maria','jose','pedro','macaury','mario','jose','amrmo','komuna','pedrivck','izapb',
      'manos','lrais','flari','vladirmi','mussov',
]


series_idade = pd.Series(idades)

series_nome = pd.Series(nome)

# %%

df = pd.DataFrame()

df['idades'] = series_idade

df['nomes'] = nome

print(df)

df['nomes'][2]


for items in df['idades'].values:
      if items%2==0 :
            print (f"ELE é PAR {items}")
# %%
df.describe()