'''
16) Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a
quantidades de latas de tinta a serem compradas e o preço total.

'''


m = float(input("Tamanho em metros quadrados da área a ser pintada:"))
li = m / 3
price = 80.0
la = 18    
latas = li / la
total = latas * price
print("Você usara {:.2f} litros de tinta".format(latas))
print("O preço total é de R$ {:.2f}".format(total))

