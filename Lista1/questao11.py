'''
11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo.
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
'''

a , b , c = int(input("Digite o valor de A:")), int(input("Digite o valor de B:")), float(input("Digite o valor de C:"))
print("Soma:", (2*a) * (b/2))
print("Produto:", (3*a) + c)
print("Cubo:", c ** 3)

