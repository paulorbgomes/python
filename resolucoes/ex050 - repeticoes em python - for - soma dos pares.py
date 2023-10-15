'''
Desenvolva um programa que leia seis números inteiros e mostre
a soma apenas daqueles que forem pares. Se o valor digitado for
ímpar, desconsidere-o.
'''

print("")
soma = 0
valores = []
for i in range(1,7):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if (num % 2 == 0):
        valores.append(num)
        soma = soma + num
print(f"Os números pares são: {valores}")
print(f"A soma deles vale: {soma}")
