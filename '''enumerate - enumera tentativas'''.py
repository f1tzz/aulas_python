'''enumerate  - enumera tentativas'''

lista = ['maria', 'renata', 'helena', 'joana']
lista.append('joão')

lista_enumerada = list(enumerate(lista))
# print(next(lista_enumerada)) #RETORNA UMA TUPLA (TUPLAS E LISTAS SÃO ITERAVEIS)
print(lista_enumerada) #RETORNA UMA TUPLA (TUPLAS E LISTAS SÃO ITERAVEIS)

for item in lista_enumerada:
    print(item)

#depois que o iterator e pego ele e ultilizado ou seja ele acaba por ser zerado e no final não ha como replica-lo de novo
#isso ocorre quando o iterator esta numa variavel anterior estabelecida caso seja direto na função e possivel sem 
#poblema
