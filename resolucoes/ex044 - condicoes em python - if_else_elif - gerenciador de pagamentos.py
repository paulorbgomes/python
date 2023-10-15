'''
Elabore um programa que calcule o valor a ser pago por um
produto, considerando o seu preço normal e condição de
pagamento:
-> à vista dinheiro/cheque: 10% de desconto
-> à vista no cartão: 5% de desconto
-> em até 2x no cartão: preço normal
-> 3X ou mais no cartão: 20% de juros
'''

print("")
print(14 * "=*")
print(" GERENCIADOR DE PAGAMENTOS ")
print(14 * "=*")
print("     Forma de Pagamento     ")
print("[1] à vista dinheiro/cheque")
print("[2] à vista no cartão")
print("[3] em até 2x no cartão")
print("[4] 3x ou mais no cartão")
print(14 * "=*")
preco = float(input("Preço normal do produto: R$ "))
pag = int(input("Forma de Pagamento: "))
print(14 * "=*")
if pag == 1:
    print(f"Valor a ser pago: R$ {preco - (preco * 10/100):.2f}.")
elif pag == 2:
    print(f"Valor a ser pago: R$ {preco - (preco * 5/100):.2f}.")
elif pag == 3:
    print(f"Valor a ser pago: R$ {preco:.2f}.")
elif pag == 4:
    print(f"Valor a ser pago: R$ {preco + (preco * 20/100):.2f}.")
else:
    print("Forma de pagamento inválida!")
    print("Escolha as opções [1], [2], [3] ou [4]")
print(14 * "=*")
