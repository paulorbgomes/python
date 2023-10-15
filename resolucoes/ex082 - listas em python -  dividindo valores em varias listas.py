'''
Crie um programa que vai ler vários números e colocar em uma
lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
print("")

lista = []
pares = []
impares = []
while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(20 * "-=")
print(f"A lista completa é {lista}")
for i in lista:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
print(f"A lista de pares é {pares}")
print(f"A lista de ímpares é {impares}")


