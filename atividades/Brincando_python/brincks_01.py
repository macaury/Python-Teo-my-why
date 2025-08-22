#%%

def jur_compost(ano:int,investimento=float|int,percet=float, status = bool)-> float:
    
    """ Juros compostos deve considerar lorem lorem lorem lorem lorem a ser retornado sem tempo pae
    
    investimento : Um numero float ou int que represente o valor em real
    Percet : representa o valor da taxa
    ano : um numero inteiro >=1 que representa a quantidade de anos que o investimento terá liquidez
    """
    total = investimento * percet ** ano
    lucro = total - investimento
    
    retorno = [total,lucro]
    
    return retorno


result = jur_compost(3,1000,1.13)

print(jur_compost(ano=4.2,investimento=1000,percet=1.13)[0])



#%%
def impar_par (x:int):
    if x % 2 ==0:
        print("o numero é par")
    else:
        print("o numero é impar")
        

impar_par(8)

# %%
# [ SOMA ]


def media( a:list,c=0)-> float:
    
  return (sum(a)/len(a))



print(media([10,20,30,40,50]))


# %%


def media_ar(a:float,b:float, *args:float)->float:
    
    valores = [a,b]+ list(args)
    print(f"a = {a} \n b = {b} \n args {args}")
    
    print(f"valores {valores}")
    
    
    
    
media_ar(2,3,4,5,4,53)

# %%
