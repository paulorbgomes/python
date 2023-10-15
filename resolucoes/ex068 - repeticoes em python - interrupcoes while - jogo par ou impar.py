'''
Faça um programa que jogue par ou ímpar com o seu computador.
O jogo só será interrompido quando o jogador PERDER, mostrando
o total de vitórias consecutivas que ele conquistou no final do
jogo.
'''

import random
vitorias = 0
print(20 * "=-")
print("VAMOS JOGAR PAR OU ÍMPAR ...")
while True:
    print(20 * "=-")
    valor = int(input("Diga um valor: "))
    escolha = input("Você escolhe PAR ou ÍMPAR? [P/I] ").strip().upper()
    print(20 * "-")
    pc = random.randint(0,10)
    soma = valor + pc
    if (soma % 2 == 0):
        print(f"Você jogou {valor} e o computador {pc}. Total de {soma} deu PAR.")
        print(20 * "-")
    else:
        print(f"Você jogou {valor} e o computador {pc}. Total de {soma} deu ÍMPAR.")
        print(20 * "-")
    if (soma % 2 == 0) and (escolha == "P"):
        vitorias = vitorias + 1
        print("Você VENCEU!")
        print("Vamos jogar novamente ...")
    elif (soma % 2 != 0) and (escolha == "I"):
        vitorias = vitorias + 1
        print("Você VENCEU!")
        print("Vamos jogar novamente ...")
    else:
        print(f"Você PERDEU! Você venceu {vitorias} vez(es) consecutiva(s).")
        print(20 * "=-")
        break
    
    
    

