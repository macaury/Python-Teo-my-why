#%%

import pandas as pd

clientes = pd.read_csv("../data/clientes.csv",sep=";")

cinco_maiores_pontos = (clientes.sort_values(by="QtdePontos", ascending=False).head(5))


cinco_maiores_pontos

#%%

brinquedo = pd.DataFrame(
      {
            "nome":["nah","mah","teo","jose"],
            "idade":[32,43,35,42],
            "salario":[2234,4533,3245,4533],
      }
)

brinquedo.sort_values(by=["salario","idade"],ascending=[False,True])
