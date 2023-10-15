'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maior
idade e quantas já são maiores.
'''

print("")
from datetime import datetime
ano_atual = datetime.now().year
maiores = 0
menores = 0
for i in range(1,8):
    ano_nasc = int(input(f"Digite o ano de nascimento da {i}ª pessoa: "))
    if ano_atual - ano_nasc < 18:
        menores = menores + 1
    elif ano_atual - ano_nasc >= 18:
        maiores = maiores + 1
print("")
print(f"Das 7 pessoas informadas, {menores} são menores de idade, e {maiores} são maiores de idade.")
