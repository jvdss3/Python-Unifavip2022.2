'''
20) Faça um programa que exiba na tela a quantidade de acertos de cada aluno em uma prova, e 
caso a nota seja igual ou maior que 60% da quantidade de questões exiba “Classificado”, se não 
“Desclassificado”. Para isso crie uma TUPLA que receba o cartão gabarito com as 20 questões, cada 
uma com cinco alternativas identificadas por A, B, C, D e E., Depois crie uma lista para cada Aluno e 
receba as 20 questões da prova dele e diga se o aluno está Classificado ou Desclassificado. Ao final, 
pergunte se o usuário deseja cadastrar outro aluno ou finalizar o programa.
'''


c = ("A", "B", "C", "D", "E","A", "B", "C", "D", "E","A", "B", "C", "D", "E","A", "B", "C", "D", "E")    
a = []
for i in range(0,20):
    x = input("Digite a resposta da questão %d:" %(i+1))
    a.append(x)
c = sum(a == b for a, b in zip(a, c))
z = c / len(a) * 100

if z >= 60:
    print("Classificado")
else:
    print("Desclassificado")

while True:
        x = input("Deseja cadastrar outro aluno? (S/N):")
    if x == "S":
        
    elif x == "N":
            break
    else:
        print("Digite S ou N")
        continue
        
