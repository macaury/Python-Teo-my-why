#%%
nome_arquivo= "historia.txt"

open_file = open(nome_arquivo)


# %%
with open(nome_arquivo) as open_file:
    conteudo = open_file.read()
    
    
#%%

nome_arquivo = "historia2.txt"

texto = "lorem relos demais"
with open(nome_arquivo,mode='a') as open_file:
    open_file.write(texto)
    
    
    
# %%

with open(nome_arquivo) as open_file:
    print(open_file.read())
    
# %%


nome_csv = "dados.csv"

with open(nome_csv) as open_arquivo:
    conteudo = (open_arquivo.readlines())
    



#%%
dados = dict()
chaves = conteudo[0].strip("\n").split(";")
for c in chaves:
    dados[c] = []
    
print(dados)


#%%
print(conteudo[1:])

for linha in conteudo[1:]:
   valores =  linha.strip("\n").split(";")
   
   for i in range(len(valores)):
       dados[chaves[i]].append(valores[i])
       
#%%     

idades = []

for i in dados["idade"]:
    idades.append(int(i))
    
    
media = sum(idades)

media = media/len(idades)

media


    
    

# %%
