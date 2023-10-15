"""
Faça um programa que ajude um jogador da mega sena a criar
palpites. O programa vai perguntar quantos jogos serão gerados
e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
tudo em uma lista composta.
"""
print("")

from time import sleep
import random
print(30 * "-")
print("{:^30}".format("JOGA NA MEGA SENA"))
print(30 * "-")

jogos = int(input("Quantos jogos você quer que eu sorteie? "))
print(f"SORTEANDO {jogos} JOGOS ...")
for i in range(1,jogos + 1):
    print(f"Jogo {i}: ", end="")
    jogo = []
    for i in range(0,6):
        if i == 0:
            valor = random.randint(1,60)
            jogo.append(valor)
        else:
            while valor in jogo:
                valor = random.randint(1,60)
            jogo.append(valor)
    print(f"{sorted(jogo)}")
    sleep(1)
print("{:=^30}".format("< BOA SORTE! >"))
