'''
Faça um programa que leia um número qualquer e mostre o seu
fatorial:
Ex:
5! = 5 x 4 x 3 x 2 x 1 = 120
'''

print("")
num = int(input("Digite um número inteiro: "))
numi = num
fatorial = 1
while num >= 1:
    fatorial = fatorial * num
    num = num - 1
print(f"O fatorial de {numi} é {fatorial}.")

# Outra forma ...
import math
num = int(input("Digite um número inteiro: "))
print(f"O fatorial de {num} é {math.factorial(num)}.")

