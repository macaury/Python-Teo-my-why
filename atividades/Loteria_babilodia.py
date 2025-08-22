##
# Construa um programa que realize o sorteio de um numero entre 1 e 15

# O usuario terá 3 chances de acerta o valor 
# a cada tentativa voce deve informar se o chute é mnaior ou menor que o número sorteado
# Caso o usuário acerte, dê parabens
# ##
 #%%
import random
#%%

def loteria(aposta:int,numb_sorte:int):
    
    if aposta == numb_sorte:
        
        print(f" Parabens, Você acertou o numero sorteado {numb_sorte}")
        
    else:

        return(1)

#%%
def maior_menor(aposta:int,sorte:int):
    
    if aposta > sorte:
        
        print(" O número da aposta escolhido é maior")
        
    elif aposta < sorte:
        
        print(" O número da aposta  escolhido é menor")
        
#%%

sorte = random.randint(1,15)

tentativa = 0
#%%


def get_input():
      while True:
        try:
            numero_escolhido = int(input("Digite o valor que você quer apostar \n"))
            
        except ValueError as e:
            print("Digite um valor inteiro")
            continue
        
        if 1<= numero_escolhido <= 15:
            return numero_escolhido
        
        print("Valor invalido")
 

tentativa = 0
for i in range(3):
    
  
    numero_escolhido = get_input()
    
    if loteria(numero_escolhido,numb_sorte=sorte)==1:
        tentativa+=1
        print(f'Voce errou a tentativa \n Agora voce possui {tentativa} / 3')
        
        maior_menor(aposta=numero_escolhido,sorte=sorte)
        
    else:
        loteria(numero_escolhido,numb_sorte=sorte)
        break
    
else:
    print("\n\n Suas tentativas acabaram!")


# %%
