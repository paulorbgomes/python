'''
Faça um programa que leia três números e mostre qual é o maior
e qual é o menor.
'''

n1 = float(input("Digite o 1º número: "))
n2 = float(input("Digite o 2º número: "))
n3 = float(input("Digite o 3º número: "))
lista = [n1, n2, n3]
lista = sorted(lista)
print(f"Menor Valor: {lista[0]}")
print(f"Maior Valor: {lista[2]}")
    
