''' listas imutaveis em python '''
# listas em python 
# tipo list - mutavel
# suporta varios de qualquer tipo
# conhecimentos reutilizaveis - indices e fatiamento
# metodos uteis: append, insert, pop, del, clear, extend +
# Create read Update Delete
# Criar ler Alterar Apagar
# = lista[i] CRUD()

"""      +01234
         -54321"""
string = 'ABCDE'

#indices para seleção
#         #0,.....1,.......2,....3 (em relaçãoo aos demais em baixo)
lista = [123, 'guilherme', 10.5, True]
lista[1] = 'luiz otavio' #alterando o item especifico com o uso do indice da lista 
del lista[2]
print(lista[2]) #ja que eu alterei o indice 2 anterior, ele printa o novo indice 2 

print(lista[1])

"""EM UMA LISTA DE PYTHON E RECOMENDADO QUE VOCE NÃO ALTERE DEMAIS OS ITENS DA
PRINCIPALMENTE SE FOR FORÇAR UMA MOVIMENTAÇÃO DE TODA A LISTA, E SIM SO ADICIONE
OU REMOVA DO FINAL, CENTRO OU COMEÇO"""

#append - adicionar coisas no final da lista 
lista.append(50)
print(lista, 'o item 50 foi adicionado')

#POP - REMOVE O ULTIMO ITEM DA LISTA 
lista.pop() #tambem serve para remover indices
print(lista, 'o ultimo item foi removido')

#clear - limpa a lista (so sobra os [])

# insert - adiciona em um indice que ja existe
lista.insert(0, 100)
print(lista) # um noovo indice e criado no lugar daquele que exitia antes e assim oso indices anterioes se movem
#