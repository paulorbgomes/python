'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''

print("")
i = "S"
soma = 0
cont = 0
num = int(input("Digite um número inteiro: "))
maior = num
menor = num
while i == "S":
    soma = soma + num
    cont = cont + 1
    if num <= menor:
        menor = num
    if num >= maior:
        maior = num
    i = str(input("Deseja continuar [S/N]? ")).strip().upper()
    if i == "S":
        num = int(input("Digite um número inteiro: "))
print("")
print(f"Você digitou {cont} números.")
print(f"A média dos valores digitados é: {soma/cont}")
print(f"O menor valor digitado foi: {menor}")
print(f"O maior valor digitado foi: {maior}")

