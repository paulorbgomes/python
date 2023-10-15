'''
Faça um programa que leia o ano de nascimento de um jovem e
informe, de acordo com sua idade:
-> Se ele ainda vai se alistar ao serviço militar.
-> Se é a hora de se alistar.
-> Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que
passou do prazo.
'''

from datetime import date
print("")
print(11 * "=*")
print(" ALISTAMENTO MILITAR ")
print(11 * "=*")

nasc = int(input("Digite o ano de nascimento: "))
ano_atual = date.today().year

if (ano_atual - nasc < 18):
    print("Você ainda irá se alistar no serviço militar.")
    print(f"Faltam {18 - (ano_atual - nasc)} anos para o alistamento.")
elif (ano_atual - nasc == 18):
    print("Você tem 18 anos, é hora de se alistar! Procure a junta militar da sua região.")
else:
    print(f"Seu alistamento está atrasado em {(ano_atual - nasc) - 18} anos. Procure a junta militar da sua região.")

