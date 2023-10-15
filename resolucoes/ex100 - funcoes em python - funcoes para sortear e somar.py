'''
Faça um programa que tenha uma lista chamada números e duas
funções chamadas sorteio() e somaPar(). A primeira função vai
sortear 5 números e vai colocá-los dentro da lista e a segunda
função vai mostrar a soma entre todos os valores pares sorteados
pela função anterior.
'''
print("")

import random
from time import sleep

def sorteio():
    lista = []
    print("Sorteando 5 valores da lista: ", end="")
    for i in range(0,5):
        valor = random.randint(1, 10)
        print(valor, end=" ")
        sleep(1)
        lista.append(valor)
    a = lista[:]
    print("PRONTO!")
    return a
    
def somaPar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma = soma + i
    print(f"Somando os valores pares de {lista}, temos {soma}")

somaPar(sorteio())
