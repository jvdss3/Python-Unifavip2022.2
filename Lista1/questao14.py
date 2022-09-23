'''
14) João Papo-de-Pescador, homem de bem, comprou um computador para controlar o rendimento
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por
quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na
variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as
mensagens adequadas.
'''


p = int(input("Digite o peso do peixe:"))
    
if p > 50:
    e = p - 50
    m = e * 4
else:
    e = 0
    m = 0
print("Excesso de peso foi de {}kg, a multa aplicada foi de R$:{}".format(e, m))
