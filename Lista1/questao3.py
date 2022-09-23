# 3) Faça um Programa que peça dois números e mostre como resultado a soma.


a , b = int(input("Digite um número: ")), int(input("Digite outro número:"))
if a > b:
    print("O maior número digitado é {}".format(a))
else:
    print("O maior número digitado é {}".format(b))
