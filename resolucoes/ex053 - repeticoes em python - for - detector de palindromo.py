'''
Crie um programa que leia uma frase qualquer e diga se ela é
um palindromo, desconsiderando os espaços.

EXEMPLOS:
apos a sopa
a sacada da casa
a torre da derrota
o lobo ama o bolo
anotaram a data da maratona
'''

print("")
frase = str(input("Digite uma frase qualquer sem acentos: ")).strip().upper()
frase_limpa = []
for i in frase:
    if (i != " "):
        frase_limpa.append(i)
invertida = []
for i in range(len(frase_limpa)-1,-1,-1):
    invertida.append(frase_limpa[i])
if frase_limpa == invertida:
    print("A frase É PALÍNDROMO")
else:
    print("A frase NÃO É PALÍNDROMO")





