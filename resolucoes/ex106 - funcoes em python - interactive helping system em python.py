'''
Faça um mini-sistema que utilize o interactive help do Python.
O usuário vai digitar o comando e o manual vai aparecer. Quando o
usuário digitar a palavra "FIM", o programa se encerrará.
'''
print("")

def PyHelp():
    while True:
        frase = 'SISTEMA DE AJUDA PYHELP'
        c = len(frase) + 4 
        print(c * "~")
        print(f"{frase:^{c}}")
        print(c * "~")
        resp = str(input("Função ou Biblioteca > ")).strip()
        if resp in ["FIM", "fim", "Fim"]:
            frase = "ATÉ LOGO!"
            c = len(frase) + 4 
            print(c * "~")
            print(f"{frase:^{c}}")
            print(c * "~")
            break
        else:
            frase = "Acessando o manual do comando" + " " + resp
            c = len(frase) + 4 
            print(c * "~")
            print(f"{frase:^{c}}")
            print(c * "~")
            help(resp)

PyHelp()
