'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
-> Quantas pessoas tem mais de 18 anos.
-> Quantos homens foram cadastrados.
-> Quantas mulheres tem menos de 20 anos.
'''
print("")
cont_18 = 0
homens = 0
mulheres = 0

while True:
    print(29 * "-")
    print("     CADASTRE UMA PESSOA     ")
    print(29 * "-")

    idade = int(input("Idade: "))
    if idade > 18:
        cont_18 = cont_18 + 1

    while True:
        sexo = str(input("Sexo: [M/F] ")).strip().upper()
        if sexo == "M" or sexo == "F":
            break
    if sexo == "M":
        homens = homens + 1
    if sexo == "F" and idade < 20:
        mulheres = mulheres + 1
    print(29 * "-")

    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()
        if resp == "S" or resp == "N":
            break

    if resp == "N":
        print("===== FIM DO PROGRAMA =====")
        print(f"Total de pessoas com mais de 18 anos: {cont_18}")
        print(f"Ao todo temos {homens} homens cadastrados")
        print(f"E temos {mulheres} mulheres com menos de 20 anos")
        break
