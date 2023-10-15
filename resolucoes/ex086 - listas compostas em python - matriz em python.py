"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
print("")

matriz = []
for i in range(0,3):
    linha = []
    for j in range(0,3):
        valor = int(input(f"Digite um valor para [{i},{j}]: "))
        linha.append(valor)
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
            

        
