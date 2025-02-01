def moeda(valor):
    valorMonetario = "{:.2f}".format(valor).replace(".",",")
    return valorMonetario

def aumentar(valorAtual, valorAumentar, formatacao):
    if formatacao == True:
        return moeda(valorAtual + (valorAumentar / 100) * valorAtual)
    else:
        return valorAtual + (valorAumentar / 100) * valorAtual 

def diminuir(valorAtual, valorDiminuir, formatacao):
    if formatacao == True:
        return moeda(valorAtual - (valorDiminuir / 100) * valorAtual)
    else:
        return valorAtual - (valorDiminuir / 100) * valorAtual 

def dobro(valor, formatacao):
    if formatacao == True:
        return moeda(2 * valor)
    else:
        return 2 * valor 

def metade(valor, formatacao):
    if formatacao == True:
        return moeda(valor / 2)
    else:
        return valor / 2


