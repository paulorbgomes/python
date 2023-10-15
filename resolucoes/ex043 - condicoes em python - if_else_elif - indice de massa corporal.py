'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela
abaixo:
-> Abaixo de 18.5: Abaixo do peso
-> Entre 18.5 e 25: Peso ideal
-> 25 até 30: Sobrepeso
-> 30 até 40: Obesidade
-> Acima de 40: Obesidade mórbida
'''

print("")
print(16 * "*=")
print(" ÍNDICE DE MASSA CORPORAL (IMC)")
print(16 * "*=")

peso = float(input("Digite seu peso (em Kg): "))
altura = float(input("Digite sua altura (em metros): "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print(f"IMC = {imc:.1f}: abaixo do peso (magreza).")
elif imc >= 18.5 and imc <= 24.9:
    print(f"IMC = {imc:.1f}: peso normal.")
elif imc >= 25 and imc <= 29.9:
    print(f"IMC = {imc:.1f}: Sobrepeso.")
elif imc >= 30 and imc <= 34.9:
    print(f"IMC = {imc:.1f}: Obesidade grau I.")
elif imc >= 35 and imc <= 40:
    print(f"IMC = {imc:.1f}: Obesidade grau II.")
elif imc > 40:
    print(f"IMC = {imc:.1f}: Obesidade grau III.")
print(16 * "*=")
