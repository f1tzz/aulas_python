#valores padrão para parametros

def valor_padrao(x, y, z=None):
    if z is None:
        print(f"{x=} {y=} {z=}", x + y + z)
    else: 
        print(f"{x=} {y=}","z isnt none", x+y )
        
valor_padrao(3,5,5)

def soma(*args):
    
    return sum(args)

print(f"{soma(10,21,4,3) * 2}")
"""EMPACOTAMENTO"""
#----------------------------------------

    
NUMEROS = 1,2,3,4,67,78
print(*NUMEROS) 
"""desempacotamento de objetos para usar como parametros"""