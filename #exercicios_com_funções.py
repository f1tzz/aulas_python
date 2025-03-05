#exercicios_com_funçõe(s]
xis = int(input("digite um numero: "))
def par_ou_inpar(nome):
    if nome % 2 == 0: return print("par")
    else: return print("inpar") #e redundante, funçoes so retornam uma vez se esse duperior não funcionasse 
    #altomaticamente iria buscar o proximo return 

par_ou_inpar(xis)