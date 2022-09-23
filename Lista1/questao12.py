'''
12) Tendo como dados de entrada a altura de uma pessoa, construa um programa que calcule seu
peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

'''


h, p = float(input("Digite sua altura em metros:")),float(input("Digite seu peso:"))    
h1 = (72.7 * h) - 58
print("Seu peso ideal é {:.2f}kg".format(h1))

