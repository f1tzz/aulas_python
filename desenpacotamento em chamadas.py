"""desempacotamento em chamadas """

string = 'e foda '
lista = ['peitos', 'bunda', 2, 3, 4, 5, 'labios'] #estao aqui tres indices indo do 0 ate o 2 
tupla = ('pneu', 'queda', 'gigante')

p, b, *_, u = lista #informo tres variaveis que se compatibilizam com os indices depois de igualar variaveis
"""QUANDO USO O ASTERISCO E O SINAL '_' ELE PUXA PARA DESEPACOTAMENTO TODOS OS VALORES ATE O FINAL
EU POSSO SEPARAR O FINAL COLOCANDO UM ULTIMO VARIAVEL PARA RECEBER O VALOR E ASSIM POSSO PULAR VALORES
QUE NÃO QUERO QUE SEJAM EXIBIDOS"""

print(p, u) #peço dois indices da variavel igualada 