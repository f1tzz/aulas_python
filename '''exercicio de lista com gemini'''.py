'''exercicio de lista com gemini'''
#VARIAVEIS
lista = ['banana', "maçã", "laranja", "uva", "pera"]
print('lista original:', lista)
item_usuario = input('Digite mais uma fruta: ')
#MECANISMO
if len(item_usuario) > 1:
    print('digite so um item')
    
lista.append(item_usuario) #adicionando um ultimo item a lista
print(lista)

lista.pop(0) #apagando o primeiro item 
print(lista)

lista.sort() #arruando em ordem alfabetica
print(lista)



