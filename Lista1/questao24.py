'''
24) Faça um Programa que leia três palavras e mostre a maior palavra entre eles, além de apresentar 
quantos caracteres tem na palavra.
'''


a, b, c = input('Insira uma palavra: '),input('Insira uma palavra: '),input('Insira uma palavra: ')   
if len(a) > len(b) and len(a) > len(c):
    print('A palavra "{}" é a maior, com {} caracteres!'.format(a, len(a)))
elif len(b) > len(a) and len(b) > len(c):
    print('A palavra "{}" é a maior, com {} caracteres!'.format(b, len(b)))
elif len(c) > len(a) and len(c) > len(b):
    print('A palavra "{}" é a maior, com {} caracteres!'.format(c, len(c)))
else:
    print("As palavras são de tamanhos iguais!")


