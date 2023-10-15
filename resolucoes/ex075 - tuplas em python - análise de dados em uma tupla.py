'''
Desenvolva um programa que leia quatro valores pelo teclado e
guarde-os em uma tupla. No final mostre:
-> Quantas vezes apareceu o valor 9.
-> Em que posição foi digitado o primeiro valor 3.
-> Quais foram os números pares.
'''
print("")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
n3 = int(input("Digite mais um número: "))
n4 = int(input("Digite o último número: "))
tupla = (n1, n2, n3, n4)

print(f"Você digitou os valores: {tupla}")

if 9 not in tupla:
    print("Você não digitou o valor 9!")
else:
    print(f"O valor 9 apareceu {tupla.count(9)} vezes")
    
if 3 not in tupla:
    print("Você não digitou o valor 3!")
else:
    print(f"O primeiro valor 3 apareceu na posição {tupla.index(3) + 1}")

print(f"Os valores pares digitados foram:", end=" ")
for i in tupla:
    if i % 2 == 0:
        print(f"{i}", end=" ")



