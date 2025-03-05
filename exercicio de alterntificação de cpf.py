"""exercicios de altentificação de cpf"""

cpf_usuario = input('cole um cpf: ')
cpf_convertido = list(cpf_usuario)
cpf_ENTRADA= cpf_convertido.remove('-')
cpf_entrada_2 =  cpf_convertido.remove('.' ) 
cpf_entrada_3 =  cpf_convertido.remove('.' ) 

cpf =  cpf_convertido #/ CPF DEFINIDO 
"""VARIAVEIS""" """MEU RESULTADO"""
# resultado_multiplicação = [x * y for x, y in zip(nove_primeiros, itens_requisito)]
# soma_de_itens_cpf = (sum(resultado_multiplicação) * 10 % 11) 
# primeiro_digito_final = soma_de_itens_cpf

# if primeiro_digito_final <= 9: primeiro_digito_final = soma_de_itens_cpf
# else: primeiro_digito_final = 0

# print(primeiro_digito_final )
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
"""RESULTADO PROFISSIONAL"""

nove_primeiros  = cpf [:9] #0,2] SEM OS ULTIMOS DOIS NUMEROS 
#fatiamento de string do primeiro ao ultimo 
itens_requisito = [10,9,8,7,6,5,4,3,2]
contagen_10a0_primeiro = 10
resultado_primeiro = 0

for digito in nove_primeiros:
    resultado_primeiro += int(digito) * contagen_10a0_primeiro # 0 += a cada loop o numero em inteiro
    contagen_10a0_primeiro -=1
    
digito = ((resultado_primeiro * 10) % 11)
digito_novo_1 = digito if digito <= 9 else 0
# deixa igual a esse se esse for nessa condição se não e 0
print(digito_novo_1, 'primeiro ultimo digito ')

#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""SEGUNDO DIGITO"""
DEZ_DIGITOS = cpf [:10]
itens_requisito_2 = [11,10,9,8,7,6,5,4,3,2]
contagen11a0_segundo = 11
resultado_segundo = 0 

for number in DEZ_DIGITOS :
    resultado_segundo += int(number) * contagen11a0_segundo
    contagen11a0_segundo -=1
number = (resultado_segundo *10 % 11)
segundo_digito = number if number <= 9 else 0
print (segundo_digito, 'segundo ultimo digito')

if digito_novo_1 and segundo_digito in cpf[9:11]:
    print('digitos coincidem. cpf validado') 
else: print('n')
    
# novo_cpf = f'{nove_primeiros}, {list(digito_novo_1, segundo_digito)}'
# print(novo_cpf)
"""exite uma função que pode ser usada em string que serviviria para tratar as 
informações que o usuario me fornece REPLACE exemplo (.replace('.', ''))"""
