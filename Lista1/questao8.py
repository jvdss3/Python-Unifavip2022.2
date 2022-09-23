'''
8) Faça um Programa que pergunte quanto você ganha por hora
e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.

'''



s ,h = float(input("Digite o quanto você ganha por hora:")), float(input("Digite quantas horas você trabalha por mês:"))
t = s * h
print("O seu salário é R${:.2f}".format(t))

