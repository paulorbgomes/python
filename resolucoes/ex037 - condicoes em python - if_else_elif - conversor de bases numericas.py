'''
Escreva um programa que leia um número inteiro qualquer e peça
para o usuário escolher qual será a base de conversão:
-> 1 para binário
-> 2 para octal
-> 3 para hexadecimal
'''

print("")
print(15 * "=*")
print(" CONVERSOR DE BASES NUMÉRICAS ")
print(15 * "=*")
print("[1] - Conversão para BINÁRIO")
print("[2] - Conversão para OCTAL")
print("[3] - Conversão para HEXADECIMAL")
print(15 * "=*")

num = int(input("Digite um número inteiro: "))
conv = int(input("Digite a base numérica desejada [1], [2] ou [3]: "))
print(f"Opção escolhida: [{conv}]")
if conv == 1:
    resul = bin(num)
    resul = resul[2:]
    print(f"O número {num} em BINÁRIO é: {resul}.")
elif conv == 2:
    resul = oct(num)
    resul = resul[2:]
    print(f"O número {num} em OCTAL é: {resul}.")
elif conv == 3:
    resul = hex(num)
    resul = resul[2:]
    print(f"O número {num} em HEXADECIMAL é: {resul}.")
else:
    print("Você digitou uma OPÇÃO INVÁLIDA! Repita o procedimento.")
    
    


