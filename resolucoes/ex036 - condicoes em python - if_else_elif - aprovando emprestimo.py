'''
Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. O programa vai peguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário ou então o empréstimo será negado.
'''

print("")
print(10 * "=*")
print("EMPRÉSTIMO BANCÁRIO")
print(10 * "=*")

valor_casa = float(input("Qual é o valor da casa? R$ "))
salario = float(input("Qual é o salário do comprador? R$ "))
anos = int(input("Em quantos anos deseja pagar? "))

prestacao = valor_casa / (12 * anos)

if prestacao <= salario * 0.3:
    print("Empréstimo APROVADO! Parabéns")
    print(f"Valor da prestação: R$ {prestacao:.2f} em {12 * anos}x sem juros.")
else:
    print(f"Empréstimo NEGADO! A prestação excede R$ {salario * 0.3:.2f} mensais.")
print(10 * "=*")
