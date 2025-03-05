"""FUNÇÕES FINALMENTE """
"""
introdução as funções em python
trecho de codigo que replica determinado ação ao longo do codigo
eles recebem valores ('parametros' no momento em que são criados )
e retornam um valor especifico (retornam a flag none)
"""

def imprimir(a ,b ,c): #define uma função que retorna o valor none 
    #definidos os parametros
    print(a, b, c)
    
imprimir(1, 3 , 69 ) #se colocar so dois argumentos, nçao bate com os parametros

def saudação(nome) : 
    print(f'ola {nome}!')


saudação('naitan ')

"""
ARGUMENTOS NOMEADOS E NÃO NOMEADOS E TAMBEM POSICIONAIS
ARGUMENTO NOMEADO ACOMPANHA O SINAL DE IGUAL
ARGUMENTO NÃO NOMEADO DEPENDE DE ATENÇÃO E NÃO RECEBE SINAL ALGUM"""

def soma(x, y, z=None):
    print(x + y +z)
    
    if z is not None:
        print(f'{x=} {y=} {z=}', x + y + z  )
    else:
        print(f'{x=} {y=}', x + y) 
    
soma(y='6', x='9', z='9') #argumentos nomeados no começo, todos nomeados a seguir

soma(2, 88, z=290) #se voce não usar argumentos nomeados a partir do momento que voce
# nomear algo os fatores seguintes teram que ser nomeados

soma(5, 20, 0)

