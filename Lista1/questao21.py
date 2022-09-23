'''
21) Faça um programa que peça do usuário o nome de 6 cidades, depois de inseridas verifique se há
nomes iguais e havendo peça para que sejam inseridos novamente, e também crie a opção do usuário
concatenar dados ao nome da cidade. E por fim, exiba qual o nome de cidade mais extenso.
'''

c = []
for i in range (0,6):
    
    a = input("Digite o nome de {} cidade: ".format(i+1))
    if a in c:
        ("O nome da cidade já está na lista, insira outra.")
        a = input("O nome da cidade já está na lista, insira outra.")
    c.append(a)
    
    answer = input("Você gostaria de concatenar dados ao nome da cidade?"(S/N))
    if answer in ('S', 's'):
        
        e = input("Coloque o nome da extenção da cidade.")
        c[i] = c[i] + e
        print(c[i])

print("O nome das cidades são: ", c)
longest = max(c,key=len)
print("O nome da cidade mais extensa é: ", longest)


