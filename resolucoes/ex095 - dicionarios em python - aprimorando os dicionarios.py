'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores
incluindo um sistema de visualização de detalhes de aproveitamento
de cada jogador

DESAFIO 093:
Crie um programa que gerencie o aproveitamento de um jogador de
futebol. O programa vai ler o nome do jogador e quantas partidas
ele jogou. Depois vai ler a quantidade de gols feitos em cada
partida. No final, tudo isso será guardado em um dicionário,
incluindo o total de gols feitos durante o campeonato.
'''
print("")

codigo = 0
lista = []
while True:
    print(30 * "-")
    registro = {}
    registro["Código"] = codigo
    codigo = codigo + 1
    nome = str(input("Nome do Jogador: ")).strip()
    registro["Nome"] = nome
    partidas = int(input(f"Quantas partidas {nome} jogou? "))
    registro["Partidas"] = partidas
    num_gols = []
    soma_gols = 0
    for i in range(1,partidas + 1):
        gols = int(input(f"Quantos gols na partida {i}? "))
        num_gols.append(gols)
        soma_gols = soma_gols + gols
    registro["Gols"] = num_gols
    registro["Total"] = soma_gols
    lista.append(registro)
    resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(60 * "-=")
print(f"{'COD.':<20} {'NOME':<20} {'PARTIDAS':<20} {'GOLS':20} {'TOTAL':20}")
print(120 * "-")
for i in range(0,len(lista)):
    cada_jog = list(lista[i].values())
    for j in range(0,len(cada_jog)):
        print(f"{str(cada_jog[j]):<20} ",end="")
    print()
print(120 * "-")
codigos = []
codigos.append(999)
for i in range(0,len(lista)):
    codigos.append(lista[i]["Código"])
while True:
    resp = int(input("Mostrar dados de qual jogador (999 para parar)? "))
    if resp == 999:
        break
    while resp not in codigos:
        print(f"ERRO! Não existe jogador com o código {resp}! Tente novamente.")
        print(120 * "-")
        resp = int(input("Mostrar dados de qual jogador (999 para parar)? "))
    if resp == 999:
        break
    print(f"-- LEVANTAMENTO DO JOGADOR {lista[resp]['Nome']}:")
    for i in range(0,len(lista[resp]["Gols"])):
        print(f"   No jogo {i+1} fez {lista[resp]['Gols'][i]} gols.")
    print(120 * "-")
print("<< VOLTE SEMPRE >>")
