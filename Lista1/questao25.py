'''
25) Faça um Programa que leia três números e mostre o maior e o menor deles
'''

a, b, c = int(input('Insira um número: ')), int(input('Insira um número: ')), int(input('Insira um número: '))
if a > b and a > c:
    print('O maior número é o "{}"'.format(a))
elif b > a and b > c:
    print('O maior número é o "{}"'.format(b))
elif c > a and c > b:
    print('O maior número é o "{}"'.format(c))
else:
    print("Os números são iguais!")
if a < b and a < c:
    print('O menor número é o "{}"'.format(a))
elif b < a and b < c:
    print('O menor número é o "{}"'.format(b))
elif c < a and c < b:
    print('O menor número é o "{}"'.format(c))
else:
    print("Os números são iguais!")    
    
