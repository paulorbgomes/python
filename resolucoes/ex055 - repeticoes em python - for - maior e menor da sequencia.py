'''
Faça um programa que leia o peso de cinco pessoas. No final,
mostre qual foi o maior e o menor peso lidos.
'''

print("")
peso = float(input(f"Digite o peso da {1}ª pessoa (em Kg): "))
menor = peso
maior = peso
for n in range(2,6):
    peso = float(input(f"Digite o peso da {n}ª pessoa (em Kg): "))
    if peso <= menor:
        menor = peso
    elif peso >= maior:
        maior = peso
print(f"O menor e o maior peso lidos foram {menor} Kg e {maior} Kg, respectivamente.")
