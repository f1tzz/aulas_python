"""regular expressions """
import re
import sys

cpf = '1102.414.793-20'
cpf = re.sub(r'[^0-9]', #0 a nove
    '',# substitui por nada
    '1102.414.793-20') #nessa string 

#checagem para validar cpf
cpf_check_in = cpf == cpf[0] * len(cpf)

if cpf_check_in :
    print('voce digitou dados sequenciais')
    sys.exit()
import random    
print(cpf)

for a in range(100):

    #rand int para digitos aleatorios inteiros
    nove_digitos =''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))
    print(nove_digitos)
