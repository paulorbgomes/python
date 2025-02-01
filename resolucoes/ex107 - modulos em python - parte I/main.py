import moeda

valor = float(input("Digite o preço: R$ "))

metade = moeda.metade(valor)
print(f"A metade de {valor} é {metade}")

dobro = moeda.dobro(valor)
print(f"O dobro de {valor} é {dobro}")

valorAumentado = moeda.aumentar(valor, 10)
print(f"Aumentando 10%, temos {valorAumentado}")

valorDiminuido = moeda.diminuir(valor, 13)
print(f"Reduzindo 13%, temos {valorDiminuido}")




