'''
Um professor quer sortear um dos seus quatro alunos para apagar
o quadro. Faça um programa que ajude ele, lendo o nome deles e
escrevendo o nome do escolhido.
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

print(f"Quem vai apagar o quadro é: {alunos[random.randint(0,3)]}")              
