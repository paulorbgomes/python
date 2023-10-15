'''
Desenvolva um programa que leia o primeiro termo e a razão de
uma progressão aritmética (PA). No final, mostre os 10 primeiros
termos dessa progressão.
'''

print("")
print(14 * "-=")
print(" PROGRESSÃO ARITMÉTICA (PA) ")
print(14 * "-=")
t1 = int(input("-> Digite o primeiro termo da PA: "))
r = int(input("-> Digite a razão da PA: "))
print("")
print("Os 10 primeiros termos da PA são:")
for i in range(1,11):
    print(t1)
    t1 = t1 + r
print(14 * "-=")
