'''
Crie um programa que vai gerar cinco números aleatórios e colocar
em uma tupla.
Depois disso, mostre a listagem de números gerados e também
indique o menor e o maior valor que estão na tupla.
'''
print("")

# Minha solução ...
import random
print("Os números sorteados foram:", end=" ")
numeros = []
for i in range(0,5):
    val = random.randint(1,10)
    print(f"{val}", end=" ")
    numeros.append(val)
    if i == 0:
        menor = val
        maior = val
    else:
        if val < menor:
            menor = val
        if val > maior:
            maior = val
tupla = tuple(numeros)
print(f"\nO maior valor sorteado foi: {maior}")
print(f"O menor valor sorteado foi: {menor}")


    
    





