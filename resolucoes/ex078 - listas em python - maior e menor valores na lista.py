'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma
lista.
No final, mostre qual foi o maior e o menor valor digitado e as
suas respectivas posições na lista.
'''
print("")

lista = []
for i in range(0,5):
    lista.append(int(input(f"Digite um valor para a Posição {i}: ")))
print(30 * "=-")
print(f"Você digitou os valores {lista}")
minimo = min(lista)
maximo = max(lista)
print(f"O maior valor digitado foi {maximo} nas posições", end = " ")
for i in range(0,len(lista)):
    if lista[i] == maximo:
        print(i, end = "... ")
print(f"\nO menor valor digitado foi {minimo} nas posições", end = " ")
for i in range(0,len(lista)):
    if lista[i] == minimo:
        print(i, end = "... ")



        
  
