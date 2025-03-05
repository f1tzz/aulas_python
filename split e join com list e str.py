"""split e join com list e str """
#split serve para dividir str e lista 

frase = 'eita! que dia mais quente '
lista = frase.split('!') #sem identar onde voce quer dividir voce acaba dividindo ela toda nos epaços vazios
#porem voce pode escolher onde vai ser separado
#print(lista) #retorna uma lista 

for i, frase in enumerate( lista): #retorna a frase sem a lista
    print(lista[i].strip( )) #STRIP TIRA ESPAÇOES NO COMEÇO E NO FINAL DA STR na exibição da str (a direita)
    
print(lista)
print(lista[i].lstrip( )) #STRIP TIRA ESPAÇOES NO COMEÇO E NO FINAL DA STR na exibição da str (a esquerda)
print(lista)

""""Uma boa pratica e não mudar uma lista mutavel para ter acesso a ela antes da mudança
    pódendo criar uma lista vazia e colocar o mesmo valor nela com append para copia-la rapidamente  """
    
    
#JOIN
#metodo de união de str
frases_unidas = '-'.join(lista)

