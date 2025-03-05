'''GAME TEXT CORREÇÃO'''
import os
#variaveis 
secret_word = 'batata'
acertos_usuario = ''
tentativas = 0 

while True :
    letra_digitada = input('digite uma letra: ')
    
    if len(letra_digitada) > 1 :
        print('digite apenas uma letra')
        continue
    
    if letra_digitada in secret_word:
        acertos_usuario += letra_digitada
        
    palavra_tentativa = ''
    
    for palavras_ocultas in secret_word:
        if palavras_ocultas in acertos_usuario:
            palavra_tentativa += palavras_ocultas
    
        else:
            palavra_tentativa += '*'
            
    tentativas += 1
    
    print(palavra_tentativa)  #tentativas)
    
    if palavra_tentativa == secret_word:
        os.system('clear')
        
        print(F'PARABENS, A PALAVRA SECRETA E {secret_word}, {tentativas} tentativas')
        acertos_usuario = ''
        tentativas = 0 #pra recomeçar o game
        
        
        #break
    
