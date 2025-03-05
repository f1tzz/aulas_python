#VARAIAVEIS
lista = []
lista_terminada = ''
items = 0
lista_variaveis = ['a', 'i', 'l']
lista = 
#SISTEMA

while True:
    
    print('#LISTA MAKER#')
    entrada_usuario = input(f'selecione uma opção: \n'
f'[i]nserir   [a]pagar    [l]istar  :')
    
    
    #try:
    if entrada_usuario == 'i':
        valor = input('valor: ')
        lista.append(valor)
        items += 1
    #----------------------------------------------------------------------    
    if not entrada_usuario in lista_variaveis or len(entrada_usuario) > 1:
        print('digite somente um dos tres itens para proseguir...')
    #--------------------------------------------------------------------------    
    if entrada_usuario == 'a' and len(lista) > 0:
        item_apagar = input('digite o indice que deseja apagar :')
        item_inteiro = int(item_apagar)
        del lista[item_inteiro]
        print(lista)
        
    elif len(lista) == 0 :
        print('insira itens na lista antes de apagar ou listar ')
    #----------------------------------------------------------------------    
    if entrada_usuario == 'l' and len(lista) > 0:
        for item in enumerate(lista):
            print(item)
    #-------------------------------------------------------------------
    if items == 5 :
        encerrar = input('quer encerrar sua lista: \n'
        f'[s]im     [n]ão       :')
    
        
    
    
    

