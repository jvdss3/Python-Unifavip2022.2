'''
19) Crie um programa para preencher um vetor (lista) com números inteiros e solicitar um número do 
teclado. Pesquisar se esse número existe no vetor. Se existir, imprimir em qual posição do vetor (lista) 
foi digitado. Se não existir, imprimir mensagem que não existe.
'''
import random


list = [0,1,2,3,4,5,6,7,8,9]    
i = int(input("Insira um número entre 0 e 9: "))
while i not in list:
    i = int(input("Insira um número entre 0 e 9: "))
if i in list:
    index = list.index(i)        
    print("O número {} está na lista e está na posição {}".format(i, index))  

