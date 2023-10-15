'''
Crie um programa que faça o computador jogar Pedra Papel Tesoura
com você.
'''

print("")
print(20 * "=*")
print("   VAMOS JOGAR PEDRA, PAPEL E TESOURA   ")
print(20 * "=*")
print("")

import random
import time
opcoes = ["PEDRA", "PAPEL", "TESOURA"]
pc = opcoes[random.randint(0,2)]
jogador = str(input("Escolha uma opção [PEDRA, PAPEL ou TESOURA]: ")).strip().upper()
print("")

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PÔ!!!")
time.sleep(1)
print("")

if pc == "PEDRA" and jogador == "PAPEL":
    print("Eu escolhi PEDRA e você PAPEL: VOCÊ VENCEU!")
elif pc == "PEDRA" and jogador == "TESOURA":
    print("Eu escolhi PEDRA e você TESOURA: EU VENCI!")
elif pc == "PEDRA" and jogador == "PEDRA":
    print("Ambos escolheram PEDRA. Jogue novamente!")
elif pc == "PAPEL" and jogador == "PEDRA":
    print("Eu escolhi PAPEL e você PEDRA: EU VENCI!")
elif pc == "PAPEL" and jogador == "TESOURA":
    print("Eu escolhi PAPEL e você TESOURA: VOCÊ VENCEU!")
elif pc == "PAPEL" and jogador == "PAPEL":
    print("Ambos escolheram PAPEL. Jogue novamente!")
elif pc == "TESOURA" and jogador == "PEDRA":
    print("Eu escolhi TESOURA e você PEDRA: VOCÊ VENCEU!")
elif pc == "TESOURA" and jogador == "PAPEL":
    print("Eu escolhi TESOURA e você PAPEL: EU VENCI!")
elif pc == "TESOURA" and jogador == "TESOURA":
    print("Ambos escolheram TESOURA. jogue novamente!")
else:
    print("Opção inválida! Jogue novamente.")

