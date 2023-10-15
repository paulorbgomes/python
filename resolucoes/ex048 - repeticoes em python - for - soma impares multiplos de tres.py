'''
Faça um programa que calcule a soma entre todos os números
ímpares que são múltiplos de três e que se encontram no
intervalo de 1 até 500.
'''

print("")
soma = 0
cont = 0
for i in range(1,501,2):
    if (i % 3 == 0):
        soma = soma + i
        cont = cont + 1
print(f"""A soma dos {cont} números ímpares que são
múltiplos de três entre 1 e 500 vale: {soma}.""")
