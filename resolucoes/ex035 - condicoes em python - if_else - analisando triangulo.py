'''
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
'''

l1 = float(input("Comprimento da primeira reta: "))
l2 = float(input("Comprimento da segunda reta: "))
l3 = float(input("Comprimento da terceira reta: "))

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("As retas podem formar um triângulo!")
else:
    print("As retas não podem formar um triângulo!")
