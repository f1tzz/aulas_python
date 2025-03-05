'''exercicico qual letra aparece mais '''
frase = "o python e uma linguagem multiparadigma, pytho foi criado por guido van rossum"

i = 0
numeração_letra_atual = 0
numeração_maior_apareceu = ' '


while i < len(frase):
    letra_atual = frase[i]
    letra_contagem = frase.count(letra_atual)
    
    if letra_atual == ' ':
        i += 1
        continue
    
    if numeração_letra_atual < letra_contagem: #numeração letra atual recebe um valor no começo e se ele for mais alto continuia ate o final do codigo
        numeração_letra_atual = letra_contagem
        numeração_maior_apareceu = letra_atual
    
    i += 1
    #espaços = letra_contagem.index(' ')
    # if espaços:
    #     continue
        
    print(f'{letra_atual}, {letra_contagem} vezes')
  
print(f"a letra que apareceu mais foi o '{numeração_maior_apareceu}' "
)

