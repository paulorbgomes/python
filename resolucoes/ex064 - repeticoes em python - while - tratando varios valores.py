'''
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar 999, que é a
condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (desconsiderando o flag).
'''

print("")
n = 0
cont = 0
soma = 0
while n != 999:
    n = int(input("Digite um valor inteiro [999 para parar]: "))
    if n != 999:
        cont = cont + 1
        soma = soma + n
print("")
print(f"Você digitou {cont} valores. A soma entre eles é {soma}.")

