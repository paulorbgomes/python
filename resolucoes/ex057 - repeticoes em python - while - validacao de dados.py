'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite
os valores M ou F. Caso esteja errado, peça a digitação
novamente até ter um valor correto.
'''

print("")
sexo = str(input("Digite seu sexo [M/F]: "))
while (sexo != "M") and (sexo != "F"): 
    sexo = str(input("Opção inválida! Digite novamente [M/F]: "))
print(f"Sexo {sexo} cadastrado com sucesso!")
    
