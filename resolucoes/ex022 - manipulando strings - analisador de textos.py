'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
-> O nome com todas as letras maiúsculas;
-> O nome com todas as letras minúsculas;
-> Quantas letras ao todo (sem considerar espaços);
-> Quantas letras tem o primeiro nome.
'''

nome = str(input("Digite seu nome completo: ")).strip()
print(" ")
print("Analisando seu nome ...")
print(" ")
print(nome.upper())
print(nome.lower())
letras = len(nome) - nome.count(" ")
print(f"Seu nome possui {letras} letras")
nome = nome.split()
print(f"Seu primeiro nome é {nome[0]} e tem {len(nome[0])} letras")
