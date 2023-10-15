'''
Faça um programa que tenha uma função chamada area(), que receba
as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.
'''
print("")

# Rotinas
def cabecalho(frase):
    l = int(len(frase)) + 4
    print(l * "-")
    print(f"{frase:^{l}}")
    print(l * "-")

def area(a, b):
    # Calcula a área de um terreno retangular.
    # Entradas: largura = a, comprimento = b
    # Saída: área do terreno = c
    c = a * b
    print(f"A área de um terreno {a:.2f}x{b:.2f} é de {c:.2f} m².")

# Programa principal
cabecalho("CONTROLE DE TERRENOS")
larg = float(input("LARGURA (m): "))
comp = float(input("COMPRIMENTO (m): "))
area(larg, comp)


