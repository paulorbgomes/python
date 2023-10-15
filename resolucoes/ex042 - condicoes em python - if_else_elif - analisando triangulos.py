'''
Refaça o desafio 035 dos triângulos, acrescentando o recurso
de mostrar que tipo de triângulo será formado:
-> Equilátero: todos os lados iguais
-> Isósceles: dois lados iguais
-> Escaleno: todos os lados diferentes

DESAFIO 035:
Desenvolva um programa que leia o comprimento de três retas e
diga ao usuário se elas podem ou não formar um triângulo.
'''

print("")
print(12 * "=*")
print(" ANALISANDO TRIÂNGULOS ")
print(12 * "=*")
r1 = float(input("Comprimento da primeira reta: "))
r2 = float(input("Comprimento da segunda reta: "))
r3 = float(input("Comprimento da terceira reta: "))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print("Os segmentos descritos (PODEM) formar um triângulo.")
    if (r1 == r2) and (r1 == r3) and (r2 == r3):
        print("Classificação: triângulo EQUILÁTERO.")
    elif (r1 != r2) and (r1 != r3) and (r2 != r3):
        print("Classificação: triângulo ESCALENO.")
    else:
        print("Classificação: triângulo ISÓSCELES.")
else:
    print("Os segmentos descritos (NÃO PODEM) formar um triângulo.")
