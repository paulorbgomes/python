'''
Faça um programa que tenha uma função chamada ficha(), que
receba dois parâmetros opcionais: o nome de um jogador e quantos
gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo
que algum dado não tenha sido informado corretamente.
'''
print("")

def ficha(nome="", gols=""):
    if (nome != "") and (gols != ""):
        print(f"O jogador {nome} fez {gols} gol(s) no campeonato.")
    elif (nome == "") and (gols != ""):
        print(f"O jogador <desconhecido> fez {gols} gol(s) no campeonato.")
    elif (nome == "") and (gols == ""):
        print(f"O jogador <desconhecido> fez 0 gol(s) no campeonato.")


# Programa principal
print(30 * "-")
nome = str(input("Nome do jogador: "))
gols = str(input("Número de Gols: "))
ficha(nome, gols)
