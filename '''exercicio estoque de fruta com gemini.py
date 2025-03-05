'''exercicio estoque de fruta com gemini'''
#   VARIAVEIS
lista_frutas = ['maça', 'pera', 'banana', 'jaca', 'abacate']
lista_estoque = [3, 4, 10, 2, 4]
lista_combinada= zip(lista_estoque, lista_frutas)

#   MECAMISMO
print(lista_frutas)

fruta_usuario = input('qual fruta voce deseja: ')

for item in lista_combinada:
    if fruta_usuario in lista_frutas :
        quantidade_fruta_usuario = input(f'quantas {fruta_usuario}: ')
        tuple(quantidade_fruta_usuario)
        if quantidade_fruta_usuario > item:
            print('frutas insuficientes')


