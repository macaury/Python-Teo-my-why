#%%

import pandas as pd

lista = [
      10,
      20,
      30,
      40,
      50,
      60,
      70,
      2,
      13
]

series_idade = pd.Series(lista)

series_idade.mean()

variancia = series_idade.var()

summary = series_idade.describe()

summary
# %%
