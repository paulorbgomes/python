import moeda

valor = float(input("Digite o preço: R$ "))

metade = moeda.moeda(moeda.metade(valor))
print(f"A metade de R$ {valor:.2f} é R$ {metade}")

dobro = moeda.moeda(moeda.dobro(valor))
print(f"O dobro de R$ {valor:.2f} é R$ {dobro}")

valorAumentado = moeda.moeda(moeda.aumentar(valor, 10))
print(f"Aumentando 10%, temos R$ {valorAumentado}")

valorDiminuido = moeda.moeda(moeda.diminuir(valor, 13))
print(f"Reduzindo 13%, temos R$ {valorDiminuido}")




