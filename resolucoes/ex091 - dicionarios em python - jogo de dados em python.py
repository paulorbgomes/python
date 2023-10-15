'''
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o
vencedor tirou o maior número no dado.
'''
print("")

resultado = {}
import random
from time import sleep
print("Valores sorteados:")
for i in range(1,5):
    valor = random.randint(1,6)
    nome = (f"Jogador{i}")
    resultado[nome] = valor
    print(f"   O {nome} tirou {valor} no dado.")
    sleep(1)
print(30 * "-=")
print("  == RANKING DOS JOGADORES ==  ")
cont = 1
for i in sorted(resultado, key = resultado.get, reverse=True):
    print(f"   {cont}º lugar: {i} com {resultado[i]}.")
    cont = cont + 1
    sleep(1)

