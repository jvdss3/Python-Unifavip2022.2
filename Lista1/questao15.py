'''
15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

w , h = float(input("Quando você ganha por hora:")), int(input("Quantas horas você trabalha por mês:"))
allh = w * h    
ir = allh * 0.11
inss = allh * 0.08
sindicato = allh * 0.05
print ('+ Salário Bruto : R$ {:.2f}'.format(allh))
print ('- IR: R$ {:.2f}'.format(ir)) 
print ('- INSS: R$ {:.2f}'.format(inss))
print ('- Sindicato: R$ {:.2f}'.format(sindicato))
print ('= Salário Liquido : R$ {:.2f}'.format( allh - ir - inss - sindicato))

