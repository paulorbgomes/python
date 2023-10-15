'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''
print("")
val1 = int(input("Primeiro valor: "))
val2 = int(input("Segundo valor: "))
flag = True
while flag == True:
    print(5* " " + "[ 1 ] somar")
    print(5* " " +"[ 2 ] multiplicar")
    print(5* " " +"[ 3 ] maior")
    print(5* " " +"[ 4 ] novos números")
    print(5* " " +"[ 5 ] sair do programa")
    op = int(input(">>>>> Qual é a sua opção? "))
    if op != 1 and op !=2 and op != 3 and op != 4 and op != 5:
        print("Opção inválida. Tente novamente")
        print(15 * "-=")
    if op == 5:
        flag = False
        print("Saindo do programa ... Até a próxima!")
        print(15 * "-=")
    else:
        if op == 1:
            soma = val1 + val2
            print(f"O resultado de {val1} + {val2} é {soma}")
            print(15 * "-=")
        if op == 2:
            mult = val1 * val2
            print(f"O resultado de {val1} x {val2} é {mult}")
            print(15 * "-=")
        if op == 3:
            maior = val1
            if val2 > val1:
                maior = val2
            print(f"Entre {val1} e {val2} o maior é {maior}")
            print(15 * "-=")
        if op == 4:
            print("Informe os números novamente:")
            val1 = int(input("Primeiro valor: "))
            val2 = int(input("Segundo valor: "))
