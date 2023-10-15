'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser
que quer mostrar 0 termos.
'''

print("")
a1 = int(input("Primeiro termo da PA: "))
r = int(input("Razão da PA: "))
print("")
print(f"10 primeiros termos da PA com primeiro termo {a1} e razão {r}:")
print("")
i = 0
qtermos = 0
flag = True
while flag == True:
    while i <= 9:
        print(a1)
        a1 = a1 + r
        i = i + 1
        qtermos = qtermos + 1
    print("")
    termos = int(input("Quantos termos você quer mostrar a mais? "))
    print("")
    if termos == 0:
        flag = False
    else:
        j = 0
        while j < termos:
            print(a1)
            a1 = a1 + r
            j = j + 1
            qtermos = qtermos + 1
print("")
print(f"A PA foi finalizada com {qtermos} termos mostrados.")
