'''
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma sequência de
Fibonacci.
Ex: 0 1 1 2 3 5 8
'''

#print("")
#print(13 * "=*")
#print(" SEQUÊNCIA DE FIBONACCI ")
#print(13 * "=*")
#n = int(input("Digite quantos termos devem aparecer: "))
#numA = 1
#numB = 0
#i = 1
#while i <= n:
#    print(numB)
#    num = numA + numB
#    numB = numA
#    numA = num
#    i = i +1 

# Sequência de Fibonacci usando listas ...
print("")
print(13 * "=*")
print(" SEQUÊNCIA DE FIBONACCI ")
print(13 * "=*")
n = int(input("Digite quantos termos devem aparecer: "))
seq = []
seq.append(0)
seq.append(1)
i = 2
while i <= n - 1:
    seq.append(seq[i - 1] + seq[i - 2])
    i = i + 1
print(seq)
