'''
Faça um programa que leia um ângulo qualquer e mostre na tela
o valor do seno, cosseno e tangente desse ângulo.
'''

import math

ang = float(input("Digite o valor do ângulo em graus: "))
print(f"O SENO de {ang}º é: {math.sin(math.radians(ang)):.2f}")
print(f"O COSSENO de {ang}º é: {math.cos(math.radians(ang)):.2f}")
print(f"A TANGENTE de {ang}º é: {math.tan(math.radians(ang)):.2f}")
