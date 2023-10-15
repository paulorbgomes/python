'''
Faça um programa que tenha uma função chamada contador(), que
receba três parâmetros: início, fim e passo e realize a
contagem.

Seu programa tem que realizar três contagens através da função
criada:

-> De 1 até 10, de 1 em 1.
-> De 10 até 0, de 2 em 2.
-> Uma contagem personalizada.
'''
print("")

from time import sleep
def contagem(inicio, fim, passo):
    if (fim > inicio) and (passo > 0):
        cont = inicio
        while cont <= fim:
            print(cont, end=" ")
            sleep(1)
            cont = cont + passo
    if (inicio > fim) and (passo > 0):
        cont = inicio
        while cont >= fim:
            print(cont, end=" ")
            sleep(1)
            cont = cont - passo
    if (inicio > fim) and (passo < 0):
        cont = inicio
        while cont >= fim:
            print(cont, end=" ")
            sleep(1)
            cont = cont + passo
    if (inicio > fim) and (passo == 0):
        cont = inicio
        passo = 1
        while cont >= fim:
            print(cont, end=" ")
            sleep(1)
            cont = cont - passo
    if (fim > inicio) and (passo == 0):
        cont = inicio
        passo = 1
        while cont <= fim:
            print(cont, end=" ")
            sleep(1)
            cont = cont + passo
    print("FIM!")
print(20 * "-=")
print("Contagem de 1 até 10 de 1 em 1")
for i in range(1,11):
    print(i, end=" ")
    sleep(1)
print("FIM!")
print(20 * "-=")
print("Contagem de 10 até 0 de 2 em 2")
for i in range(10,-2,-2):
    print(i, end=" ")
    sleep(1)
print("FIM!")
print(20 * "-=")
print("Agora é sua vez de personalizar a contagem!")
inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
print(20 * "-=")
if (fim > inicio) and (passo == 0):
    print(f"Contagem de {inicio} até {fim} de 1 em 1")
    contagem(inicio, fim, passo)
elif (inicio > fim) and (passo == 0):
    print(f"Contagem de {inicio} até {fim} de 1 em 1")
    contagem(inicio, fim, passo)
elif (inicio > fim) and (passo < 0):
    passo = (-1) * passo
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    contagem(inicio, fim, passo)
elif (inicio > fim) and (passo > 0):
    print(f"Contagem de {inicio} até {fim} de {passo} em {passo}")
    contagem(inicio, fim, passo)
