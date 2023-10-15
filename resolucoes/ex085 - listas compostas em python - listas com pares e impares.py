'''
Crie um programa onde o usuário possa digitar sete valores
numéricos e cadastre-os em uma única lista que mantenha separados
os valores pares e ímpares. No final, mostre os valores pares e
ímpares em ordem crescente.
'''
print("")

pares = []
impares = []
lista = []
lista.append(pares)
lista.append(impares)

for i in range(1,8):
    valor = int(input(f"Digite o {i}o. valor: "))
    if (valor % 2 == 0):
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(25 * "-=")
print(f"Os valores pares digitados foram: {sorted(lista[0])}")
print(f"Os valores ímpares digitados foram: {sorted(lista[1])}")
