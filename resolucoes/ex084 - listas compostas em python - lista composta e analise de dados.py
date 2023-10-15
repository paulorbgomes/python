'''
Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
-> Quantas pessoas foram cadastradas.
-> Uma listagem com as pessoas mais pesadas.
-> Uma listagem com as pessoas mais leves.
'''
print("")

geral = list()
cadastros = 0
while True:
    pessoas = []
    nome = str(input("Nome: ")).strip()
    peso = float(input("Peso [Kg]: "))
    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
        if resp in "SN":
            break
    pessoas.append(nome)
    pessoas.append(peso)
    geral.append(pessoas)
    del pessoas
    cadastros = cadastros + 1
    if resp == "N":
        break
print(30 * "-=")
print(f"Ao todo, você cadastrou {cadastros} pessoas.")
idx, minimo = min(geral, key=lambda item: item[1])
idx, maximo = max(geral, key=lambda item: item[1])
print(f"O maior peso foi de {maximo:.1f} Kg. Peso de", end=" ")
for i in geral:
    if i[1] == maximo:
        print(f"[{i[0]}]", end=" ")
print(f"\nO menor peso foi de {minimo:.1f} Kg. Peso de", end=" ")
for i in geral:
    if i[1] == minimo:
        print(f"[{i[0]}]", end=" ")
