#%%
import pandas as pd

idades = [
      32,38,30,30,31,35,25,29,31,37,
      27,23,36,33,39,
]

series_idada = pd.Series(idades)

series_idada
# %%

series_idada.iloc[3:]

#%%


idades = [
      32,38,30,30,31,35,25,29,31,37,
      27,23,36,33,39
]

indexs = [
      'maria','jose','pedro',30,31,35,25,29,31,37,
      27,23,36,33,39,
]

series_idada = pd.Series(idades,index=indexs)

print(series_idada)


