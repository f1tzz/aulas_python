def criar_saldação(saudação, nome):
    def saudar():
        return f"{saudação}, {nome}"
    return saudar

imprimir = criar_saldação("boa noite", "guilherme")

print(imprimir())

"""clousure e o fechamento de ciclo que uma função abre com a resposta ate que vem um clouser
e fecha a execução dessa função"""