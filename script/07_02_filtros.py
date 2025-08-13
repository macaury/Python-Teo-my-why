#%%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")

filtro = clientes["QtdePontos"] == 0

clientes_0 = clientes[filtro].copy()

clientes_0["flag_1"] = 1

clientes_0

