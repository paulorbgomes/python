'''
Rafaça o desafio 009, mostrando a tabuada de X de um número que o
usuário escolher, só que agora utilizando um laço for.

DESAFIO 009: Faça um programa que leia um número inteiro qualquer
e mostre na tela a sua tabuada. 
'''

print("")
num = int(input("Digite um número para ver a sua tabuada de X: "))
print(10 * "-=")
print(f" TABUADA DE X DE {num} ")
print(10 * "-=")
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
print(10 * "-=")
