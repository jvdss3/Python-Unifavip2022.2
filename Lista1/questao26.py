'''
26) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve 
comprar, sabendo que a decisão é sempre pelo mais barato.
'''


a, b, c = int(input('Insira o preço do primeiro produto: ')), int(input('Insira o preço do segundo produto: ')), int(input('Insira o preço do terceiro produto: '))
if a < b and a < c:
    print('Você deve comprar o produto de preço "{}"'.format(a))
elif b < a and b < c:
    print('Você deve comprar o produto de preço "{}"'.format(b))
elif c < a and c < b:
    print('Você deve comprar o produto de preço "{}"'.format(c))
else:
    print("Os preços são iguais!")
    
    
