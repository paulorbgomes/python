'''
O mesmo professor do desafio anterior quer sortear a ordem de
apresentação de trabalhos dos alunos. Faça um programa que leia
o nome dos quatro alunos e mostre a ordem sorteada.
'''

import random

alunos = []
a1 = str(input("Nome do 1º aluno: "))
alunos.append(a1)
a2 = str(input("Nome do 2º aluno: "))
alunos.append(a2)
a3 = str(input("Nome do 3º aluno: "))
alunos.append(a3)
a4 = str(input("Nome do 4º aluno: "))
alunos.append(a4)
random.shuffle(alunos)
print(f"A ordem de apresentação será: \n {alunos}")


