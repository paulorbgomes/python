"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
Ao final, mostre:
-> A soma de todos os valores pares digitados.
-> A soma dos valores da terceira coluna.
-> O maior valor da segunda linha.
"""
print("")

matriz = []
soma_pares = 0
outra_soma = 0
for i in range(0,3):
    linha = []
    for j in range(0,3):
        valor = int(input(f"Digite um valor para [{i},{j}]: "))
        linha.append(valor)
        if (valor % 2 == 0):
            soma_pares = soma_pares + valor
    matriz.append(linha)
print(25 * "-=")
for l in range(0,3):
    if l == 0:
        for c in range(0,3):
            print(f"[{matriz[l][c]:^5}]", end="" )
    elif l == 1:
        print()
        for c in range(0,3):
            print(f"[{matriz[l][c]:^5}]", end="" )
    else:
        print()
        for c in range(0,3):
            print(f"[{matriz[l][c]:^5}]", end="" )
print()
print(25 * "-=")
print(f"A soma dos valores pares é {soma_pares}.")
for i in range(0,3):
    outra_soma = outra_soma + matriz[i][2]
print(f"A soma dos valores da terceira coluna é {outra_soma}.")
print(f"O maior valor da segunda linha é {max(matriz[1])}.")











            

        
