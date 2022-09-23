'''
29) As Organizações PLP LTDAresolveram dar um aumento de salário aos seus colaboradores e lhe 
contraram para desenvolver o programa que calculará os reajustes. O reajuste acontecerá segundo o 
seguinte critério, baseado no salário atual:
• salários até R$ 280,00 (incluindo) : aumento de 20%
• salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
• salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
• salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na 
tela:
• o salário antes do reajuste;
• o percentual de aumento aplicado;
• o valor do aumento;
• o novo salário, após o aumento.
'''


sa = float(input('Insira o salário atual: '))

if sa < 280:
    ajuste = 1.2
    novo_salario = sa * ajuste
elif sa >= 280 and sa < 700:
    ajuste = 1.15
    novo_salario = sa * ajuste
elif sa >= 700 and sa < 1500:
    ajuste = 1.1
    novo_salario = sa * ajuste
elif sa >= 1500:
    ajuste = 1.05
    novo_salario = sa * ajuste

print("O salário antes do reajuste era de R$ {:.2f}, o percentual do aumento aplicado foi {:.2f}, o valor aumentado foi {:.2f} e o novo sálario é de R${:.2f}".format(sa , ajuste, novo_salario - sa, novo_salario))


