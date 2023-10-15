'''
Faça um programa que tenha uma função chamada maior(), que
receba vários parâmetros com valores inteiros. Seu programa tem
que analisar todos os valores e dizer qual deles é o maior e o
menor.
'''
print("")

from time import sleep
def maior(*args):
    print(30 * "-=")
    print("Analisando os valores passados ...")
    sleep(1)
    if args == ():
        print("Foram informados 0 valores ao todo.")
        args = (0,)
    else: 
        for i in args:
            sleep(1)
            print(i, end=" ")
        print(f"Foram informados {len(args)} valores ao todo.")
    for i in range(0, len(args)):
        if i == 0:
            mn = args[0] # menor
            mr = args[0] # maior
        else:
            if args[i] < mn:
                mn = args[i]
            if args[i] > mr:
                mr = args[i]
    sleep(1)
    print(f"O menor valor informado foi {mn}.")
    sleep(1)
    print(f"O maior valor informado foi {mr}.")

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
    

