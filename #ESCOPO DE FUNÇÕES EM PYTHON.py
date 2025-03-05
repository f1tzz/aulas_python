#ESCOPO DE FUNÇÕES EM PYTHON 
#ESCOPO SIGNIFICA O LOCAL
#ESCOPO GLOBAL E O ESCOPO(LOCAL) ONDE TOD O CODIGO E ALCANÇAVEL
#ESCOPO LOCAL E O ESPAÇO(ESCOPO) ONDE APENAS NOMES DO MESMO
#LOCAL PODEM SER ALCANÇADOS
#não se tem acesso a nomes de escopos internos nos escopos externos
#a palavra global faz o externo ser a mesma que a do interno

x = 10 #esse aqui e de escopo geral, 

def escopo (): #funções tem seu poprio escopo 
    
    global x #deixa o x global e lida com ele como se ele fosse um x de fora da função

    x = 1 # esse so pode ser usado nessa ou em outra que esteja dentro dela
    print(x) #resultado do print e 1 e o x global e 1
    
    def novo ():
        # x = 10 / força a usar o anterior a essa função 
        y= 10
        print(x, y)
#pede a execução e volta pra cima em busca da função

    novo() #essa função so pode ser execultada se for identada no mesmo lugar da função 
    
escopo()
print(x) # resultado do print e 10 ou 1

"""CALL STACK / PILHA DE CHAMADAS """

#RESPONSAVEL POR DIVIDIR ESCOPOS NUM SISTEMA DE EMPILHAMENTO
