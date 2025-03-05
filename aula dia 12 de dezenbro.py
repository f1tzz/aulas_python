'''aula dia 18 de dezembro (range and for)'''
#range e uma forma de contagem numerica que envolve tres passos principais 
#range(start, stop, steps)

numero_1 = range(5, 10) #exibe o ponto inicial e final
numero_2 = range (5, 10, 2)
numero_exp_de_uso = range(0, 100, 8) # de 0 a 100 me mostra os multiplos de 8

print(numero_1)
print(numero_2)
print(numero_exp_de_uso)

for number in numero_exp_de_uso:
    print(number)
    
'''''IMPORTANTEEEEEE'''''
# O QUE E ITERAVEL (ALGO QUE PODE ENTRAGAR VARIOS VALORES DAE UM EM UM)
# MAS O QUIE DE FATOO SERIA O ITERAVEL ?
# SIMPLES! E ALGO QUE TEM ITER (UM METODO(UMA AÇÃO QUE EU CHAMO PARA OPERAR JUNTO DO MEU OBJETO))
# NEXT (TAMBEM ESTA EM FUNCIONAMENTO QUANDO FOR E USADO) ELE E UM AVAÇADOR QUE COMANDA UMA OPERAÇÃO PARA SER REPETIDA DE MANEIRA SEQUENCIAL



'''COMO FUNCIONA O 'FOR' PO DEBAIXO DOS PANOS ?
BEM, O FOR A PRIMEIRA COISA QUE ELE REALIZA E UMA CHECAGEM PELO ITERADOR DESSE ITER ELE E CHECADO POR OUTRA FUNÇÃO QUE 
RETORNA ESSA INFORMAÇÃO DO ESPAÇO DO COMPUTADOR UM ELEMENTO POR VEZ DEPOIS VEM O NEXT QUE FAZ ISSO COM A PROXIMA 
ITER ATRAVES DO ITERADOR'''

while True: # E ISSO QUE O 'FOR' FAZ!!!!
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break