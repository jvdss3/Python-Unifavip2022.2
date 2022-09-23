'''
32) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
a. "Telefonou para a vítima?"
b. "Esteve no local do crime?"
c. "Mora perto da vítima?"
d. "Devia para a vítima?"
e. "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a 
pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 
como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''


r = []

ligacao = input('Telefonou para a vítima?(S/N)').upper()
while ligacao not in ('S', 'N'):
    ligacao = input('Telefonou para a vítima?').upper()
r.append(ligacao)

cena = input('Esteve no local do crime?(S/N)').upper()
while cena not in ('S', 'N'):
    cena = input('Esteve no local do crime?').upper()
r.append(cena)

moradia = input('Mora perto da vítima?(S/N)').upper()
while moradia not in ('S', 'N'):
    moradia = input('Mora perto da vítima?').upper()
r.append(moradia)

devia = input('Devia para a vítima?(S/N)').upper()
while devia not in ('S', 'N'):
    devia = input('Devia para a vítima?').upper()
r.append(devia)

trabalho = input('Já trabalhou com a vítima?(S/N)').upper()
while trabalho not in ('S', 'N'):
    trabalho = input('Já trabalhou com a vítima?').upper()
r.append(trabalho)

result = r.count('S')

if result == 2:
    print("Suspeita")
elif result == 3 or result == 4:
    print("Cúmplice")
elif result == 5:
    print("Assassino")
else:
    print("Inocente")