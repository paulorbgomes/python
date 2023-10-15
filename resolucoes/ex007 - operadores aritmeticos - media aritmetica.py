'''
Desenvolva um programa que leia as duas notas de um aluno,
calcule e mostre a sua média.
'''

nota1 = float(input("Prezado aluno(a), digite sua primeira nota: "))
nota2 = float(input("Prezado aluno(a), digite sua segunda nota: "))
media = (nota1 + nota2) / 2   # média aritmética
print(f"Sua média é: {media:.1f}")
