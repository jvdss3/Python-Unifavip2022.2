'''
27) Faça um Programa que leia três números e mostre-os em ordem decrescente.

'''


n = []
n1 = int(input('Insert the first integer: '))
n.append(n1)
n2 = int(input('Insert the second interger: '))
n.append(n2)
n3 = int(input('Insert the third integer: '))
n.append(n3)
n.sort(reverse=True)
print(n) 
