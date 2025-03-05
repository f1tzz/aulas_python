'''Game text''' 
print(f'bem vindo, advinhe qual a palavra em 10 tentativas! (errro "*"/ acerto "letra") ')
#variaveis

palavra_secreta = 'peixe'
#--------------------------------------------
entrada_letra = ' '
entrada_len = len(entrada_letra)  #retorno numerico
#--------------------------------------------------
tentativas = 1
palavra_tentativa = ' '

#sistema
while not palavra_tentativa == palavra_secreta:
    
    entrada_letra = input('digite uma letra: ')
    
    #print(tentativas, 'tentativa')
    
    if len(entrada_letra) > 1:
        print('digite apenas uma letra sem espaço')
        continue
    if entrada_letra not in palavra_secreta:
        print(f'* {entrada_letra}, não esta na frase'
        )
    elif entrada_letra in palavra_secreta:
        print(entrada_letra, 'esta na frase'
        )
        
    tentativas += 1
    
    if tentativas >= 6: 
        palavra_tentativa = input('digite a palavra com os dados que possui: '
        )    
    if not palavra_tentativa == palavra_secreta :
            continue
    elif palavra_tentativa == palavra_secreta:
        print(F'PARABENS!. A palavra secreta era "{palavra_secreta}" {tentativas} tentativas'
        )
        
