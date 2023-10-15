'''
Crie um programa que vai ler vários números e colocar em uma
lista.
Depois disso, mostre:
-> Quantos números foram digitados.
-> A lista de valores ordenada de forma decrescente.
-> Se o valor 5 foi digitado e está ou não na lista.
'''
print("")

lista = []
cont = 0
while True:
    num = int(input("Digite um valor: "))
    lista.append(num)
    cont = cont + 1
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(20 * "-=")
print(f"Você digitou {cont} elementos.")
lista.sort(reverse = True)
print(f"Os valores em ordem decrescente são {lista}")
if 5 in lista:
    print(f"O valor 5 faz parte da lista!")
else:
    print(f"O valor 5 não foi encontrado na lista!")
