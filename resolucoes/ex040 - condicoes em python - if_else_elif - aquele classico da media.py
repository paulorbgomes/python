'''
Crie um programa que leia duas notas de um aluno e calcule sua
média, mostrando uma mensagem no final, de acordo com a média
atingida:
-> Média abaixo de 5.0: REPROVADO
-> Média entre 5.0 e 6.9: RECUPERAÇÃO
-> Média 7.0 ou superior: APROVADO
'''

print("")
print(10 * "=*")
print(" BOLETIM DO ALUNO ")
print(10 * "=*")

n1 = float(input("Primeira Nota (N1): "))
n2 = float(input("Segunda Nota (N2): "))
media = (n1 + n2) / 2
if media < 5:
    print(f"Média {media:.2f}: REPROVADO")
elif media >= 5 and media <= 6.9:
    print(f"Média {media:.2f}: RECUPERAÇÃO")
elif media >= 7:
    print(f"Média {media:.2f}: APROVADO")
