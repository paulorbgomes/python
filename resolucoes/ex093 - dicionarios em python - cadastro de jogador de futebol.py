'''
Crie um programa que gerencie o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''
print("")

dicionario = {}
lista = []
nome = str(input("Nome do jogador: ")).strip()
num_partidas = int(input(f"Quantas partidas {nome} jogou? "))
soma_gols = 0
for i in range(1,num_partidas + 1):
    gols = int(input(f"   Quantos gols na partida {i}? "))
    soma_gols = soma_gols + gols
    lista.append(gols)
print(30 * "-=")
dicionario["Nome"] = nome
dicionario["Gols"] = lista
dicionario["Total"] = soma_gols
print(dicionario)
print(30 * "-=")
for k, v in dicionario.items():
    print(f"O campo {k} tem o valor {v}.")
print(30 * "-=")
print(f"O jogador {nome} jogou {num_partidas} partidas:")
for i in range(1, num_partidas + 1):
    print(f"    => Na partida {i}, fez {dicionario['Gols'][i-1]} gols.")
print(f"Foi um total de {dicionario['Total']} gols.")
print(30 * "-=")

