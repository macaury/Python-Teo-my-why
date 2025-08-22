#%%

def calc_taxa(pr_venda:float,imposto:float,**kwargs)->float:
    imposto = pr_venda * imposto
    for i in kwargs:
        imposto  +=  imposto * kwargs[i]
        
        print(f' kwargs {i} = {kwargs[i]}')
    
    return imposto
    
    
impostos_gerais = {
    "municipal":0.3,
    "estadual":0.04,
    "nacional":0.30
}
    
print(calc_taxa(100,00.3,**impostos_gerais))
# %%
