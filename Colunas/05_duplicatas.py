#%%

import pandas as pd

#%%

df = pd.DataFrame( {
    "nome" : [
        "teo","nah","mah","robert","sil","sil"
        ],
    "sobrenome" : [
        "silva","silva","pereira","roma","morais","roma"
        ],
    "corp":[
        "pink","pink","green","white","green","white"
        ]
})

df

#%%

df.drop_duplicates(keep="last",subset="sobrenome")
# %%
