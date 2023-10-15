'''
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
-> Qual é o total gasto na compra.
-> Quantos produtos custam mais de R$ 1000,00.
-> Qual é o nome do produto mais barato.
'''
print("")

total = 0
mais_mil = 0
nome_barato = ""
i = 1

print(35 * "-")
print("        LOJA SUPER BARATÃO        ")
print(35 * "-")

while True:
    nome = str(input("Nome do produto: ")).strip()
    preco = float(input("Preço: R$ "))

    total = total + preco

    if preco > 1000:
        mais_mil = mais_mil + 1

    if i == 1:
        barato = preco
        nome_barato = nome
        i = i + 1
    else:
        if preco < barato:
            barato = preco
            nome_barato = nome

    while True:
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()
        if resp == "S" or resp == "N":
            break

    if resp == "N":
        break
    
print(12 * "-" + " FIM DO PROGRAMA " + 12 * "-")
print("O total da compra foi R$ {:.2f}".format(total))
print("Temos {} produtos custando mais de R$ 1000.00".format(mais_mil))
print("O produto mais barato foi {} que custa R$ {:.2f}".format(nome_barato,barato))

