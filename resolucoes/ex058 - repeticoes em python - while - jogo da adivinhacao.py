'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em
um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram
necessários para vencer.
'''

print("")
import random
pc = random.randint(0,10)
pal = 0
print(11 * "-=")
print(" JOGO DA ADIVINHAÇÃO ")
print(11 * "-=")
print("Sou seu computador ...")
print("Acabei de pensar em um número entre 0 e 10.")
print("Será que você consegue adivinhar qual foi?")
jog = int(input("Digite seu palpite: "))
while jog != pc:
    jog = int(input("Que pena, você errou! Tente novamente: "))
    pal = pal + 1
if pal == 0:
    pal = 1
print(f"Você acertou em {pal} tentativas. PARABÉNS!")

