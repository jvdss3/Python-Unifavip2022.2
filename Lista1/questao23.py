'''
23) Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular
a média alcançada por aluno e apresentar:
• A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
• A mensagem "Reprovado", se a média for menor do que sete;
• A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''


a , b = int(input("Digite sua primeira nota:")), int(input("Digite sua segunda nota:"))
media = (a + b) / 2
    
if media >= 7:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
else:
    print("Aprovado com Distinção")   
        
