'''
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
-> Até 9 anos: MIRIM
-> Até 14 anos: INFANTIL
-> Até 19 anos: JÚNIOR
-> Até 25 anos: SÊNIOR
-> Acima: MASTER
'''

from datetime import date
ano_atual = date.today().year
print("")
nasc = int(input("Prezado(a) atleta, digite seu ano de nascimento: "))
idade = ano_atual - nasc
print(f"O atleta tem {idade} anos de idade.")
if idade <= 9:
    print(f"Você tem {idade} anos, sua categoria é MIRIM.")
elif idade > 9 and idade <= 14:
    print(f"Você tem {idade} anos, sua categoria é INFANTIL.")
elif idade > 14 and idade <= 19:
    print(f"Você tem {idade} anos, sua categoria é JÚNIOR.")
elif idade > 19 and idade <= 25:
    print(f"Você tem {idade} anos, sua categoria é SÊNIOR.")
elif idade > 25:
    print("Você tem mais de 20 anos, sua categoria é MASTER.")
