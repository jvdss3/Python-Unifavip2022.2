'''
22) Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

while True:
    letra = input('Insira uma letra: ').upper()
    if not letra.isalpha():
        print('Insira apenas letras!')
        continue
    else:
        break
vogal = ['A', 'E', 'I', 'O', 'U']
if letra in vogal:
    print('A letra "{}" é uma vogal!'.format(letra))
else:
    print('A letra "{}" não é uma vogal!'.format(letra))
