'''
Reescreva a função leiaInt() que fizemos no desafio 104,
incluindo agora a possibilidade de digitação de um número de tipo
inválido. Aproveite e crie também uma função leiaFloat() com
a mesma funcionalidade.

Desafio 104: Crie um programa que tenha a função leiaInt(), que vai funcionar
de forma semelhante à função input() do Python, só que fazendo a
validação para aceitar apenas um valor numérico.
Ex:
n = leiaInt("Digite um número: ")
'''
print("")

def leiaInt():
    while True:
        try:
            n_int = int(input("Digite um número inteiro: "))
        except KeyboardInterrupt:
            print("Usuário preferiu não digitar esse número.")
            return 0
        except:
            print("ERRO: por favor, digite um número inteiro válido.")
        else:
            return n_int

def leiaFloat():
    while True:
        try:
            n_flo = float(input("Digite um número real: "))
        except KeyboardInterrupt:
            print("Usuário preferiu não digitar esse número.")
            return 0
        except:
            print("ERRO: por favor, digite um número real válido.")
        else:
            return n_flo
        
print(f"O valor inteiro digitado foi {leiaInt()} e o real foi {leiaFloat()}.")


