'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
guardando os dados de cada pessoa em um dicionário e todos os
dicionários em uma lista. No final, mostre:
-> Quantas pessoas foram cadastradas.
-> A média de idade do grupo.
-> Uma lista com todas as mulheres.
-> Uma lista com todas as pessoas com idade acima da média.
'''
print("")

lista = []
while True:
    dicionario = {}
    nome = str(input("Nome: ")).strip()
    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()[0]
        if sexo not in "MF":
            print("ERRO! Por favor, digite apenas M ou F.")
        if sexo in "MF":
            break
    idade = int(input("Idade: "))
    while True:
         resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
         if resp not in "SN":
             print("ERRO! Responda apenas S ou N.")
         if resp in "SN":
             break
    dicionario["Nome"] = nome
    dicionario["Sexo"] = sexo
    dicionario["Idade"] = idade
    lista.append(dicionario)
    if resp == "N":
        break
print(30 * "-=")
print(f"A) Ao todo temos {len(lista)} pessoas cadastradas.")
soma_idade = 0
for i in range(0,len(lista)):
    soma_idade = soma_idade + lista[i]['Idade']
media_idade = soma_idade/len(lista)
print(f"B) A média de idade é de {media_idade:.2f} anos.")
print(f"C) As mulheres cadastradas foram: ", end="")
for i in range(0,len(lista)):
    if lista[i]["Sexo"] == "F":
        print(f"{lista[i]['Nome']}", end=" ")
print()
print(f"D) Lista das pessoas que estão acima da média de idade:")
for i in range(0,len(lista)):
    if lista[i]["Idade"] > media_idade:
        print(f"   nome = {lista[i]['Nome']}; sexo = {lista[i]['Sexo']}; idade = {lista[i]['Idade']};")
print("<< ENCERRADO >>")
print(30 * "-=")








    

