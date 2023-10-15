'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
-> A média de idade do grupo.
-> Qual é o nome do homem mais velho.
-> Quantas mulheres têm menos de 20 anos.
'''

print("")
soma_idade = 0
h_velho = 0
q_mulheres = 0

for i in range(1,5):
    print(f"----- {i}ª PESSOA -----")
    nome = str(input("Nome Completo: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip().upper()

    soma_idade = soma_idade + idade
    
    if (sexo == "M") and idade >= h_velho:
        h_velho = idade
        nome_velho = nome

    if sexo == "F" and idade < 20:
        q_mulheres = q_mulheres + 1

print("")
print("----- ANÁLISE DO GRUPO -----")
media_idade = soma_idade / 4
print(f"A média de idade do grupo é de {media_idade} anos.")
print(f"O homem mais velho é o {nome_velho} e ele tem {h_velho} anos.")
print(f"Essa lista possui {q_mulheres} mulher(es) com menos de 20 anos.")
