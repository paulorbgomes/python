"""
Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostrar
as notas de cada aluno individualmente.
"""
print("")

from time import sleep
lista = []
while True:
    aluno = []
    nome = str(input("Nome: ")).strip()
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    aluno.append(nome)
    aluno.append(nota1)
    aluno.append(nota2)
    lista.append(aluno)
    del aluno
    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
    if resp == "N":
        break
print(25 * "-=")
print("{:<5}".format("No."), end = " ")
print("{:^10}".format("NOME"), end = " ")
print("{:>15}".format("MÉDIA"))
print(50 * "-")
cont = 0
for p in lista:
    print("{:<6}".format(cont), end = "")
    cont = cont + 1
    print("{:^12}".format(p[0]), end = "")
    print("{:>12.1f}".format((p[1] + p[2])/2), end = "")
    print()
print(50 * "-")
while True:
    resp = int(input("Mostrar notas de qual aluno? (999 interrompe): "))
    if resp == 999:
        print("FINALIZANDO ...")
        sleep(1)
        print("<<< VOLTE SEMPRE >>>")
        break
    print(f"Notas de {lista[resp][0]} são [{lista[resp][1]}, {lista[resp][2]}]")
    print(50 * "-")







    




