'''
Crie um programa onde o usuário digite uma expressão qualquer
que use parênteses. Seu aplicativo deverá analisar se a
expressão passada está com os parênteses abertos e
fechados na ordem correta.
'''
print("")

exp = str(input("Digite uma expressão: ")).strip()
exp = list(exp)
t1 = 0 # t1 equivale a (
t2 = 0 # t2 equivale a )
post1 = []
post2 = []
for i in range(0,len(exp)):
    if exp[i] == "(":
        t1 = t1 + 1
        post1.append(exp[i])
    elif exp[i] == ")":
        t2 = t2 + 1
        post2.append(exp[i])
cont = 0
if t1 == t2:
    for i in range(0,len(post1)):
        if post1[i] == "(" and post2[i] == ")":
            cont = cont +1
if cont == len(post1):
    print("Sua expressão está válida!")
else:
    print("Sua expressão está errada!")
        

    


