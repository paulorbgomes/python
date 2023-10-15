'''
Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a
validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt("Digite um número: ")
'''
print("")

def leiaInt(frase):
    print(30 * "-")
    while True:
        n = str(input(f"{frase}")).strip()
        if n.isnumeric():
            return int(n)
        else:
            print("ERRO! Digite um número inteiro válido.")
    
    
# Programa principal
n = leiaInt("Digite um número: ")
print(f"Você acabou de digitar o número {n}.")
