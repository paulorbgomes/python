'''
Escreva um programa que faça o computador pensar em um número
inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

import random
num_comp = random.randint(0,5)
num = int(input("Digite um número inteiro de 0 a 5: "))
if num == num_comp:
    print(f"Eu pensei no número {num_comp}. Você VENCEU!")
else:
    print(f"Eu pensei no número {num_comp}. Você PERDEU!")

