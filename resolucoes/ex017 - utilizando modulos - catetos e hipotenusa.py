'''
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o
comprimento da hipotenusa.
'''

import math

co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))

# Utilizando o módulo math
hip = math.sqrt(math.pow(co,2) + math.pow(ca,2))
print(f"O comprimento da hipotenusa é {hip:.2f}")

# Sem usar o módulo math
hip = ((co ** 2) + (ca ** 2)) ** (1/2)
print(f"O comprimento da hipotenusa é {hip:.2f}")
