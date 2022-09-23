'''
28) Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor 
Inválido!", conforme o caso.
'''

lista = ['M', 'V', 'N']    
puts = input('Insira o turno que você estuda(M-matutino ou V-Vespertino ou N- Noturno): ').upper()
while True:
    if puts not in lista:
        puts = input('Insira o turno que você estuda(M-matutino ou V-Vespertino ou N- Noturno): ').upper()
        continue
    else:
        break
if puts == 'M':
    print('Bom Dia!')

elif puts == 'V':
    print('Boa Tarde!')
else:
    print('Boa Noite!')    

