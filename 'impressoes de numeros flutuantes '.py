'impressoes de numeros flutuantes '
#numeros flutuantes acabam por não ser bem salvos na memeoria 
#acaba por não ser muito preciso

numero = 0.1
numero_2 = 0.7
numero_3 = numero_2+ numero
print(numero_3)

print(f'{numero_3:.2f}') #arrendonda o numero
#retorna uma string

print(round(numero_3, 2)) #round e uma função que faz exatamente essa função de arrendodamento 

'''existe um imp chamado "decimal" ele funciona  com o coamndo Decimal com D maiusculo
funciona tambem como um modificar do str para float e int  '''
import decimal 

