'''
Faça um programa que tenha uma função notas() que pode receber
várias notas de alunos e vai retornar um dicionário com as
seguintes informações:
-> Quantidade de notas.
-> A maior nota.
-> A menor nota.
-> A média da turma.
-> A situação (opcional).
Adicione também as docstrings da função.
'''
print("")

def notas(*args, sit=False):
    """
    Docstring da função notas ...
    """
    dicionario = {}
    dicionario['total'] = len(args)
    soma = 0
    for i in range(0,len(args)):
        soma = soma + args[i]
        if i == 0:
            menor = args[0]
            maior = args[0]
        else:
            if args[i] < menor:
                menor = args[i]
            if args[i] > maior:
                maior = args[i]
    dicionario['maior'] = maior
    dicionario['menor'] = menor
    media = soma / len(args)
    dicionario['media'] = media
    print(30 * "-")
    if sit == True:
        if media >= 7:
            dicionario['situação'] = "BOA"
        elif 5 <= media < 7:
            dicionario['situação'] = "RAZOÁVEL"
        else:
            dicionario['situação'] = "RUIM"
    return dicionario
            
# Programa principal
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
