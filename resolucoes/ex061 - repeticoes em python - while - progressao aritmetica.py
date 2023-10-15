'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da PA usando a estrutura while.
'''

print("")
a1 = int(input("Digite o primeiro termo da PA: "))
r = int(input("Digite a razão da PA: "))
print("")
print(f"Os 10 primeiros termos de uma PA com primeiro termo {a1} e razão {r} são:")
print("")
i = 1
while i <= 10:
    if i == 1:
        print(a1)
    else:
        a1 = a1 + r
        print(a1)
    i = i + 1
