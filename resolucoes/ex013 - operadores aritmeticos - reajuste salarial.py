'''
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário, com 15% de aumento.
'''

salario = float(input("Digite o seu salário: R$ "))
novo_salario = salario + (salario * 15/100)
print(f"Com 15% de aumento, seu salário agora é R$ {novo_salario:.2f}.")

