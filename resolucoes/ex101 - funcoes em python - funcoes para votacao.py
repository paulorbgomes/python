'''
Crie um programa que tenha uma função chamada voto() que vai
receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto
NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
'''
print("")

def voto(ano_nasc):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - ano_nasc
    if idade in [16, 17] or idade > 70:
        return f"Com idade {idade} anos: VOTO OPCIONAL."
    elif idade < 16:
        return f"Com idade {idade} anos: NÃO VOTA."
    elif 18 <= idade <= 70:
        return f"Com idade {idade} anos: VOTO OBRIGATÓRIO."

# Programa pricipal
ano_nasc = int(input("Em que ano você nasceu? "))
print(voto(ano_nasc))
