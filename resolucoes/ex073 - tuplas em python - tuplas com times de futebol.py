'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela
do campeonato brasileiro de futebol, na ordem de colocação. Depois
moste:
-> Apenas os 5 primeiros colocados.
-> Os 4 últimos colocados da tabela.
-> Uma lista com os times em ordem alfabética.
-> Em que posição na tebela está o time da Chapecoense.
'''
print("")

tabela = ("Cruzeiro", "Grêmio", "Bahia", "Vasco da Gama",
          "Sampaio Corrêa", "Ituano", "Sport Recife",
          "Criciúma", "Londrina", "Guarani", "CRB",
          "Ponte Preta", "Vila Nova", "Chapecoense",
          "Tombense", "Novorizontino", "CSA", "Brusque",
          "Operário", "Náutico")

print(20 * "-=")
print(f"Lista de times do Brasileirão Série B (2022): {tabela}")
print(20 * "-=")
print(f"Os 5 primeiros são: {tabela[0:5]}")
print(20 * "-=")
print(f"Os 4 últimos são: {tabela[16:21]}")
print(20 * "-=")
print(f"Times em ordem alfabética: {sorted(tabela)}")
print(20 * "-=")
print(f"O Chapecoense está na {tabela.index('Chapecoense') + 1}ª posição")
print(20 * "-=")
