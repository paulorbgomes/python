'''
Crie um programa onde o usuário possa digitar vários valores
numéricos e cadastre-os em uma lista. Caso o número já exista
lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.
'''
print("")

lista = []
while True:
    num = int(input("Digite um valor: "))
    if num not in lista:
        lista.append(num)
        print("Valor adicionado com sucesso ...")
    else:
        print("Valor duplicado! Não vou adicionar ...")
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
lista.sort()
print(20 * "-=")
print(f"Você digitou os valores {lista}")

