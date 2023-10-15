'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos). Depois disso, você deve mostrar, para cada
palavra, quais são as suas vogais.
'''

palavras = ("aprender", "programar", "linguagem", "python",
            "curso", "gratis", "estudar", "praticar",
            "trabalhar", "mercado", "programar", "futuro")

for i in range(0,len(palavras)):
    print(f"\nNa palavra {palavras[i].upper()} temos", end=" ")
    for j in palavras[i].upper():
        if j == "A" or j == "E" or j == "I" or j == "O" or j == "U":
            print(j.lower(), end=" ")
        
    
