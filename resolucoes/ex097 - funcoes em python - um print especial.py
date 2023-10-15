'''
Faça um programa que tenha uma função chamada escreva(), que
receba um texto qualquer como parâmetro e mostre uma mensagem
com tamanho adaptável.
Ex:
~~~~~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~~~~~
'''
print("")

# Rotinas
def escreva(texto):
    l = len(texto) + 4
    print(l * "~")
    print(f"{texto:^{l}}")
    print(l * "~")

# Programa principal
escreva("Prof. Dr. Paulo R. B. Gomes")
escreva("Curso de Python")
escreva("IFCE - campus Tauá")
