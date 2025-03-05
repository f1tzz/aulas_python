"""exercicio com listas (concatenação)"""

lista_a = [1,2,3]
lista_b = [5,4,5]
lista_c = lista_a + lista_b
lista_d = lista_a * 2

print(lista_c)
print(lista_d)
# Quando um método não retorna nada, quer dizer que ele faz uma determinada ação, mas não te entrega
# um valor de volta.
# Geralmente, quando isso ocorre em um dado que a gente espera um valor de volta, quer dizer que ele
# está mexendo no valor que você colocou aqui, no próprio objeto em si.


"""
-cuidados com dados imutaveis -

= - coopiando o valor (imutaveis)
= - aponta para o mesmo valor (imutaveis)

"""

nome = 'guilherme'
noutro_nome = nome
nome = 'reyna'
print(nome) #PYHTON LE AS COISA DE CIMA PRA BAIXO ENTÃO ELE DEVOLVE PRIMEIRO O NOME QUE EU MUDEI E DEPOIS
# ELE VAI RETORNAR O VALOR ANTERIO SALVO EM OUTRA VARIAVEL
print(noutro_nome)

'''sistema mutavel'''
lista_e = ['luiz', 'maria']
lista_f = lista_e #esta copiando a variavel e caso ela for alterado essa variavel tambem sera 
lista_e[1] = 'joao'
lista_f = lista_e.copy() #nesse caso so os dados da variavel são copiados então a variavel mesmo que depois
# alterada não apresentara poblemas 
print(lista_f) #nessa situaçãoo ele retorna caso a alteração seja concluida 



