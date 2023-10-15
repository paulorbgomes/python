'''
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80 Km/h, mostre uma mensagem dizendo que ele
foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
'''

vel = float(input("Velocidade do carro (Km/h): "))
if vel > 80:
    valor = (vel - 80) * 7
    print(f"Velocidade igual a {vel:.2f} Km/h: MULTADO")
    print(f"Valor da multa: R$ {valor:.2f}")
