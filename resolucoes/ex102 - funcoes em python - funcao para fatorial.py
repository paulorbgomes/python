'''
Crie um programa que tenha uma função fatorial() que receba dois
parâmetros: o primeiro que indique o número a calcular e o outro
chamado show, que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo do fatorial.
'''
print("")

def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número.
    : param num: O número a ser calculado.
    : param show: (opcional) Mostrar ou não a conta.
    : return: O valor do fatorial do número num.
    """
    cont = 1
    fat = num
    while cont < num:
        fat = fat * cont
        cont = cont + 1
    print(30 * "-")
    if show == True:
        for i in range(num, 1, -1):
            print(f"{i} x", end=" ")
        print(f"1 = {fat}")
        return ""
    else:
        return fat
    
# Programa principal
print(fatorial(5, True))
help(fatorial)
