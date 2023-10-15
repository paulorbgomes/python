'''
Faça um programa que leia nome e média de um aluno, guardando
também a situação em um dicionário. No final, mostre o conteúdo
da estrutura na tela.
'''
print("")

dicionario = {}
nome = str(input("Nome: ")).strip()
media = float(input(f"Média de {nome}: "))
print(20 * "-=")
dicionario["Nome"] = nome
dicionario["Média"] = media
if media >= 7:
    dicionario["Situação"] = "Aprovado"
elif  5 <= media < 7:
    dicionario["Situação"] = "Recuperação"
else:
    dicionario["Situação"] = "Reprovado"
print(f"  - O nome é igual a {dicionario['Nome']}")
print(f"  - Média é igual a {dicionario['Média']}")
print(f"  - Situação é igual a {dicionario['Situação']}")
