'''
Faça um algoritmo que leia o preço de um produto e mostre seu
novo preço, com 5% de desconto.
'''

preco = float(input("Digite o preço do produto: R$ "))
print(f"Preço com 5% de desconto: R$ {preco - (preco*0.05):.2f}")
