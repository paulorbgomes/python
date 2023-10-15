'''
Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os (com idade) em um dicionário se por
acaso a CTPS for diferente de zero, o dicionário receberá também
o ano de contratação e o salário. Calcule e acrescente, além
da idade, com quantos anos a pessoa vai se aposentar.
'''
print("")

from datetime import date
registro = {}
nome = str(input("Nome: ")).strip()
data_nasc = int(input("Ano de Nascimento: "))
num_cart = int(input("Carteira de Trabalho (0 não tem): "))
data_atual = date.today().year
idade = data_atual - data_nasc

registro["Nome"] = nome
registro["Idade"] = data_atual - data_nasc
if num_cart == 0:
    registro["CTPS"] = 0
else:
    ano_contratacao = int(input("Ano de contratação: "))
    salario = float(input("Salário: R$ "))
    registro["CTPS"] = num_cart
    registro["Contratação"] = ano_contratacao
    registro["Salário"] = salario
    registro["Aposentadoria"] = ano_contratacao - data_nasc + 35
print(30 * "-=")
for k, v in registro.items():
    print(f"   - {k} tem o valor {v}")


