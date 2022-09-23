'''
13) Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu
peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
'''

print("Digite seu sexo")
s, h, p  = int(input("[1] para sexo masculino\n[2] para feminino\n>:")),float(input("Digite sua altura em metros:")), float(input("Digite seu peso:"))
if s == 1:
    peso_ideal = (72.7 * h) - 58
    print("Seu peso ideal é {:.2f}kg".format(peso_ideal))
else:
    peso_ideal = (62.1 * h) - 44.7
    print("Seu peso ideal é {:.2f}kg".format(peso_ideal))
