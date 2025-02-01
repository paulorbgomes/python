from utilidadesCeV import moeda

valor = float(input("Digite o preço: R$ "))

metade = moeda.metade(valor, True)
print(f"A metade de R$ {moeda.moeda(valor)} é R$ {metade}")

dobro = moeda.dobro(valor, True)
print(f"O dobro de R$ {moeda.moeda(valor)} é R$ {dobro}")

valorAumentado = moeda.aumentar(valor, 10, True)
print(f"Aumentando 10%, temos R$ {valorAumentado}")

valorDiminuido = moeda.diminuir(valor, 13, True)
print(f"Reduzindo 13%, temos R$ {valorDiminuido}")




